# TN3165: Packet Filter is not API

**Framework**: Technotes

Plan your migration from Packet Filter to Network Extension.

#### Overview

macOS implements the BSD Packet Filter mechanism. This has two expected use cases:

- As an implementation detail of various system services built-in to macOS
- As an advanced feature for users, site admins, and so on

It is not considered API.  Do not use Packet Filter in a software product that you distribute to a wide audience.  If you’re currently shipping software that relies on Packet Filter, plan to migrate to [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension).

#### Packet Filter Fundamentals

Packet Filter, oftened shorted to just PF or even pf, shows up in a number of places:

- The `/dev/pf` character device
- Various `/etc/pf*` configuration files
- The `pfctl` command-line tool
- The `pfctl` and `pf.conf` [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages)

PF implements rule-based filtering.  These rules are manipulated by various system services and, less commonly, by the user.  PF is not considered API because the PF rules you install might clash with those installed by:

- The user
- macOS system services, either now or in the future
- Other third-party products

#### Moving Off Packet Filter

If you’re currently shipping a product based on PF, plan to migrate it to a supported API.  In most cases that means creating a [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension) provider:

- If your product is a VPN, create either a [`Packet tunnel provider`](https://developer.apple.com/documentation/NetworkExtension/packet-tunnel-provider) or [`App proxy provider`](https://developer.apple.com/documentation/NetworkExtension/app-proxy-provider) provider.
- If your product looks at, and potentially blocks, TCP connections or UDP flows, create a [`Content filter providers`](https://developer.apple.com/documentation/NetworkExtension/content-filter-providers).
- If your product looks at, and potentially blocks, network packets, create a [`Content filter providers`](https://developer.apple.com/documentation/NetworkExtension/content-filter-providers).
- If your product wants to intercept DNS queries, create a [`DNS proxy provider`](https://developer.apple.com/documentation/NetworkExtension/dns-proxy-provider).
- If none of these providers meet your specific needs, create a [`NETransparentProxyProvider`](https://developer.apple.com/documentation/NetworkExtension/NETransparentProxyProvider).

For information about packaging and OS version constraints, see [`TN3134: Network Extension provider deployment`](tn3134-network-extension-provider-deployment.md).

If your product needs to do something that’s not covered by one of these providers, use [`Feedback Assistant`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/) to let us know what’s missing.

#### Test During the Transition

It may take you some time to migrate from PF to Network Extension.  In the meantime, test your existing product to ensure that it’s compatible with various macOS system services.  Specifically, test with:

- Mac Virtual Display for visionOS devices
- Xcode
- Internet Sharing
- AirDrop
- Other [`Continuity features`](https://developer.apple.comhttps://www.apple.com/macos/continuity/)

Also, consider testing with products from other third-party developers who work in this space.

When testing with Xcode, check that you can build, run, and debug an app on your iOS device over the network.  Then repeat this test with the device connected via USB.  Xcode 15 and later use the networking stack to communicate with the iOS device even when it’s directly connected.

If you set up these tests with your existing product, you’ll be able to reuse them to validate the functionality of your Network Extension based product.

#### Revision History

-  First published.

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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3165-packet-filter-is-not-api)*