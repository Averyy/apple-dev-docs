# TN3134: Network Extension provider deployment

**Framework**: Technotes

Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.

#### Overview

Network Extension providers extend the networking stack in various ways.  You might implement a custom VPN protocol with a packet tunnel provider, or add a content filter provider as part of a parental control app.  Network Extension supports many different provider types and each type has different deployment requirements.  The tables below summarise these requirements for each provider type.

When reading these tables:

- The Mac Catalyst platform refers to a provider embedded in a Mac Catalyst app running on Mac.  For more information, see [`Mac Catalyst`](https://developer.apple.com/documentation/UIKit/mac-catalyst).
- The iOS Apps on Mac platform refers to a provider embedded in an iOS app running on an Apple silicon Mac.  For more information, see [`Running your iOS apps in macOS`](https://developer.apple.com/documentation/Apple-Silicon/running-your-ios-apps-in-macos).
- On macOS most Network Extension provider types can be packaged as either an app extension or a system extension.  App extensions run in a user context; if the user logs out, the provider is terminated.  System extensions run in a global context, completely independent of the logged in user.
- If a macOS row does not mention the “App Store only” restriction, the provider supports both App Store distribution and independent distribution using Developer ID signing.

For more information about using the Network Extension framework as a whole, see [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension).

#### Deploying a Packet Tunnel Provider

When building a packet tunnel provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| iOS | app extension | 9.0 | per-app mode requires managed device |
| tvOS | app extension | 17.0 | per-app mode not supported |
| macOS | app extension | 10.11 | App Store only |
|  | system extension | 10.15 |  |
| Mac Catalyst | app extension | 10.15 | App Store only |
| iOS Apps on Mac | app extension | 11.0 | App Store only |

For more information, see [`Packet tunnel provider`](https://developer.apple.com/documentation/NetworkExtension/packet-tunnel-provider).

Before you decide to implement a packet tunnel provider, read [`TN3120: Expected use cases for Network Extension packet tunnel providers`](tn3120-expected-use-cases-for-network-extension-packet-tunnel-providers.md).

#### Deploying an App Proxy Provider

When building an app proxy provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| iOS | app extension | 9.0 | managed devices only |
| macOS | app extension | 10.11 | App Store only |
|  | system extension | 10.15 |  |
| Mac Catalyst | app extension | 10.15 | App Store only |
| iOS Apps on Mac | app extension | 11.0 | App Store only |

For more information, see [`App proxy provider`](https://developer.apple.com/documentation/NetworkExtension/app-proxy-provider).

#### Deploying a Content Filter Provider

When building a content filter provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| iOS | app extension | 9.0 | supervised devices only |
|  | app extension | 15.0 | apps using Screen Time APIs |
|  | app extension | 16.0 | per-app on managed devices |
| macOS | system extension | 10.15 |  |

For more information, see [`Content filter providers`](https://developer.apple.com/documentation/NetworkExtension/content-filter-providers).

In the Screen Time case, content filters are only supported on child devices.  To enable a content filter:

1. Add the Family Controls capability to your app.  See [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).
2. Run it on a device where the user has signed in as an under 18 child member of an iCloud family.
3. Request child authorization. On iOS 16 and later, call [`requestAuthorization(for:)`](https://developer.apple.com/documentation/FamilyControls/AuthorizationCenter/requestAuthorization(for:)), passing in the `.child` option. On iOS 15, call [`requestAuthorization(completionHandler:)`](https://developer.apple.com/documentation/FamilyControls/AuthorizationCenter/requestAuthorization(completionHandler:)), which always requests child authorization.
4. Authorize that as the child’s parent or guardian.

Before submitting your app to the App Store, you must request permission to use the [`Family Controls`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.family-controls) entitlement for distribution.

#### Deploying a Dns Proxy Provider

When building a DNS proxy provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| iOS | app extension | 11.0 | supervised devices only |
|  | app extension | 16.0 | per-app on managed devices |
| macOS | system extension | 10.15 |  |

For more information, see [`DNS proxy provider`](https://developer.apple.com/documentation/NetworkExtension/dns-proxy-provider).

#### Deploying a Transparent Proxy Provider

When building a transparent proxy provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| macOS | app extension | 10.15 | App Store only |
|  | system extension | 10.15 |  |

For more information, see [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension).

macOS 11.0 introduced significant improvements to the transparent proxy feature; for the details, see the doc comments in `<NetworkExtension/NETransparentProxyProvider.h>`.

#### Deploying a Packet Filter Provider

When building a packet filter provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS |
| --- | --- | --- |
| macOS | system extension | 10.15 |

For more information, see [`Content filter providers`](https://developer.apple.com/documentation/NetworkExtension/content-filter-providers).

#### Deploying an Ethernet Tunnel Provider

When building an Ethernet tunnel provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| macOS | app extension | 13.0 | App Store only |
|  | system extension | 13.0 |  |

For more information, see [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension).

#### Deploying an App Push Provider

When building an app push provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS |
| --- | --- | --- |
| iOS | app extension | 14.0 |

For more information, see [`Local push connectivity`](https://developer.apple.com/documentation/NetworkExtension/local-push-connectivity).

#### Revision History

-  Clarified the Family Controls behaviour for content filter providers on iOS.
-  Updated for tvOS 17.
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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3134-network-extension-provider-deployment)*