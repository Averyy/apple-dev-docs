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
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3102-http3-in-your-app)*