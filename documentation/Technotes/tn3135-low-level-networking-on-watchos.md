# TN3135: Low-level networking on watchOS

**Framework**: Technotes

Learn about the supported use cases for low-level networking on watchOS.

#### Overview

watchOS groups networking into two categories:

- High-level networking.  This includes the HTTP and HTTPS support in [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession), and any code layered on top of that.
- Low-level networking.  This includes [`Network`](https://developer.apple.com/documentation/Network) framework, [`NSStream`](https://developer.apple.com/documentation/foundation/nsstream), and any other API that runs a TCP connection or UDP session directly.  That includes the low-level aspects of [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession), namely [`URLSessionStreamTask`](https://developer.apple.com/documentation/Foundation/URLSessionStreamTask) and [`URLSessionWebSocketTask`](https://developer.apple.com/documentation/Foundation/URLSessionWebSocketTask).   It also includes APIs, like [`NWBrowser`](https://developer.apple.com/documentation/Network/NWBrowser) and [`NetService`](https://developer.apple.com/documentation/Foundation/NetService), that interact directly with Bonjour.

watchOS allows all apps to use high-level networking equally.  However, it only allows an app to use low-level networking under specific circumstances:

- It allows an audio streaming app to use low-level networking while actively streaming audio.  Support for this was introduced in watchOS 6.
- It allows a VoIP app to use low-level networking while running a call using [`CallKit`](https://developer.apple.com/documentation/CallKit).  Support for this was added in watchOS 9.
- It allows an app on watchOS to set up an application service listener so that the same app on tvOS can establish a low-level connection to it using the [`DeviceDiscoveryUI`](https://developer.apple.comhttps://developer.apple.com/documentation/devicediscoveryui) framework.  Support for this was added in watchOS 9 and tvOS 16.

watchOS blocks low-level networking outside of these specific circumstances.  For example, if a normal app attempts to start an [`NWConnection`](https://developer.apple.com/documentation/Network/NWConnection), that connection will stay in the [`NWConnection.State.waiting(_:)`](https://developer.apple.com/documentation/Network/NWConnection/State-swift.enum/waiting(_:)) state with an error of `ENETDOWN`.  Similarly, an [`NWPathMonitor`](https://developer.apple.com/documentation/Network/NWPathMonitor) will remain in the [`NWPath.Status.unsatisfied`](https://developer.apple.com/documentation/Network/NWPath/Status-swift.enum/unsatisfied) state.

> ❗ **Important**: watchOS versions 6 through 8 had a bug where low-level networking might work outside of these circumstances (r. 83682211).  That bug has been fixed in watchOS 9, which correctly enforces the rules described above.

watchOS versions 6 through 8 had a bug where low-level networking might work outside of these circumstances (r. 83682211).  That bug has been fixed in watchOS 9, which correctly enforces the rules described above.

The BSD sockets API doesn’t work for networking on watchOS under any circumstances.  Use Network framework instead.

Foundation has various APIs for synchronously creating a value using bytes loaded from a URL.  For example, [`init(contentsOf:)`](https://developer.apple.com/documentation/foundation/nsdata/1413892-init) creates a data value in this way.  Using these APIs with network URLs is not best practice on any Apple platform and is not supported by watchOS.  Instead, load network URLs with a dedicated asynchronous networking API, like [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession).

When writing watchOS networking code, test it on a real device; the simulator always allows low-level networking.

Also, test your networking code in a wide variety of network environments.  Specifically, test it when the paired iPhone is available  when the paired iPhone is not available.  The best way to test the latter is to turn off both Wi-Fi and Bluetooth in the Settings app on the iPhone.  Do not use Control Center for this.  For an explanation of the difference between these two mechanisms, see [`Use Bluetooth and Wi-Fi in Control Center`](https://developer.apple.comhttps://support.apple.com/HT208086).

For more information about building an audio streaming app for watchOS, see WWDC 2019 Session 716 [`Streaming Audio on watchOS 6`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2019/716/).

#### Revision History

-  Fixed a typo.
-  Added a discussion of the DeviceDiscoveryUI framework.
-  Republished as TN3135.  Updated with information about watchOS 9.  Made significant editorial changes.
-  Updated to call out that [`URLSessionStreamTask`](https://developer.apple.com/documentation/Foundation/URLSessionStreamTask) and [`URLSessionWebSocketTask`](https://developer.apple.com/documentation/Foundation/URLSessionWebSocketTask) are considered low-level networking.
-  First published as “Low-Level Networking on watchOS” on Apple Developer Forums.

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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3135-low-level-networking-on-watchos)*