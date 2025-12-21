# TN3102: HTTP/3 in your app

**Framework**: Technotes

Get started with iOS 15’s new HTTP/3 support.

#### Overview

HTTP/3 is a major new feature in iOS 15. While you wait for your server to add support for it, here’s how you can test it today in your app:

1. Make sure your test device is running iOS 15 or later (`HTTP/3` is not supported in the simulator).
2. In Settings > Developer, under the Networking group, enable `HTTP/3`.
3. Using Xcode 13.0 or later, create a new project from the iOS > App template. Set the Language popup to Swift and the Interface popup to SwiftUI.
4. Change the `HTTP3App.swift` and the `ContentView.swift` files to the code shown below.
5. Run the app on your device.
6. Tap your Test button.

```swift

// HTTP3App.swift

@main
struct HTTP3App: App {
    let networkManager = NetworkManager()
    var body: some Scene {
        WindowGroup {
            ContentView(networkManager: networkManager)
        }
    }
}

// ContentView.swift

import SwiftUI
import os.log

struct ContentView: View {
    var networkManager: NetworkManager
    
    var body: some View {
        VStack(alignment: .leading) {
            Button("Test HTTP3") {
                networkManager.testHTTP3Request()
            }.padding(.vertical, 20)
        }.padding(40)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

class NetworkManager: NSObject, URLSessionDataDelegate {
    
    private var session: URLSession!
    
    func testHTTP3Request() {
        
        if self.session == nil {
            let config = URLSessionConfiguration.default
            config.requestCachePolicy = .reloadIgnoringLocalCacheData
            self.session = URLSession(configuration: config, delegate: self, delegateQueue: .main)
        }
        
        let urlStr = "https://google.com"
        let url = URL(string: urlStr)!
        var request = URLRequest(url: url, cachePolicy: .reloadIgnoringLocalCacheData, timeoutInterval: 60.0)
        request.assumesHTTP3Capable = true
        os_log("task will start, url: \(url.absoluteString)")
        self.session.dataTask(with: request) { (data, response, error) in
            if let error = error as NSError? {
                os_log("task transport error \(error.domain) / \(error.code)")
                return
            }
            guard let data = data, let response = response as? HTTPURLResponse else {
                os_log("task response is invalid")
                return
            }

            guard 200 ..< 300 ~= response.statusCode else {
                print("task response status code is invalid; received \(response.statusCode), but expected 2xx")
                return
            }
            os_log("task finished with status \(response.statusCode), bytes \(data.count)")
        }.resume()
        
    }
}

extension NetworkManager {
    
    func urlSession(_ session: URLSession, task: URLSessionTask, didFinishCollecting metrics: URLSessionTaskMetrics) {
        let protocols = metrics.transactionMetrics.map { $0.networkProtocolName ?? "-" }
        os_log("protocols: \(protocols)")
    }
}
```

#### Testing Notes

After running the code above, your app will print something similar to:

```None
task will start, url: <# Your H3 URL Here #>
protocols: ["h3-29"] // ["h3", "h2"]
task finished with status 200, bytes 703
```

The protocols array shows the protocol used for each HTTP transaction. In this case there was a single `HTTP/3` transaction. In some cases you may see the protocol being returned as `h2` or even `http1.1`. If this is the case then run the transaction again. This gives URLSession the opportunity to apply the `HTTP/3` service discovery option that your server sent back on the previous HTTP response.

Service discovery for `HTTP/3` is performed in one of the following ways:

- The recommended approach is to configure your DNS server to advertise the HTTPS resource record for `alpn="h3,h2"`.
- Alternatively, configure your server to respond back with the `Alt-Svc` header that advertises `HTTP/3`. For example, `Alt-Srv: h3=":443"; ma=2592000`.

To attempt to use `HTTP/3` on the first transaction, set the [`assumesHTTP3Capable`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/urlrequest/3738175-assumeshttp3capable) property on the [`URLRequest`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/urlrequest) being used to execute the data task in [`URLSession`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/urlsession).

For cases where `HTTP/3` is not supported on the server, or over the network, you will see the protocol fall back to `h2` or `http1.1`. For more information on this, please see the WWDC session for [`Accelerate networking with HTTP/3 and QUIC`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10094/).

> **Note**: Servers that support `HTTP/3` need to be based on Draft 29 or later.

If you experience issues while debugging your network transactions, take a look at these requests in the Network Instruments tool to debug what you are seeing being sent back from your server. For more on this, see the article for [`Analyzing HTTP Traffic with Instruments`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/url_loading_system/analyzing_http_traffic_with_instruments).

#### Revision History

-  Made minor editorial changes.
-  Republished as TN3102.
-  First published as “HTTP/3 in Your App” on the Apple Developer Forums.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3102-http3-in-your-app)*