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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3165-packet-filter-is-not-api)*