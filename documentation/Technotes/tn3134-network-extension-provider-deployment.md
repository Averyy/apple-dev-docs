# TN3134: Network Extension provider deployment

**Framework**: Technotes  
**Role**: Technote

Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.

## Overview

Network Extension providers extend the networking stack in various ways.  You might implement a custom VPN protocol with a packet tunnel provider, or add a content filter provider as part of a parental control app.  Network Extension supports many different provider types and each type has different deployment requirements.  The tables below summarise these requirements for each provider type.

When reading these tables:

- The Mac Catalyst platform refers to a provider embedded in a Mac Catalyst app running on Mac.  For more information, see [Mac Catalyst](../UIKit/mac-catalyst.md).
- The iOS Apps on Mac platform refers to a provider embedded in an iOS app running on an Apple silicon Mac.  For more information, see [Running your iOS apps in macOS](../apple-silicon/running-your-ios-apps-in-macos.md).
- On macOS most Network Extension provider types can be packaged as either an app extension or a system extension.  App extensions run in a user context; if the user logs out, the provider is terminated.  System extensions run in a global context, completely independent of the logged in user.
- When a provider’s per-app configuration is restricted to managed devices, the targeted apps must be installed using MDM.
- If a macOS row doesn’t mention the “App Store only” restriction, the provider supports both App Store distribution and direct distribution using Developer ID signing.

For more information about using the Network Extension framework as a whole, see [Network Extension](../NetworkExtension/NetworkExtension.md).

## Deploying a packet tunnel provider

When building a packet tunnel provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| iOS | app extension | 9.0 | per-app mode requires managed device |
| visionOS | app extension | 1.0 | per-app mode not supported |
|  | app extension | 1.1 | per-app mode requires managed device |
| tvOS | app extension | 17.0 | per-app mode not supported |
| macOS | app extension | 10.11 | App Store only |
|  | system extension | 10.15 |  |
| Mac Catalyst | app extension | 10.15 | App Store only |
| iOS Apps on Mac | app extension | 11.0 | App Store only |

For more information, see [Packet tunnel provider](../NetworkExtension/packet-tunnel-provider.md).

Before you decide to implement a packet tunnel provider, read [TN3120: Expected use cases for Network Extension packet tunnel providers](./tn3120-expected-use-cases-for-network-extension-packet-tunnel-providers.md).

## Deploying an app proxy provider

When building an app proxy provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| iOS | app extension | 9.0 | managed devices only |
| visionOS | app extension | 1.1 | managed devices only |
| macOS | app extension | 10.11 | App Store only |
|  | system extension | 10.15 |  |
| Mac Catalyst | app extension | 10.15 | App Store only |
| iOS Apps on Mac | app extension | 11.0 | App Store only |

For more information, see [App proxy provider](../NetworkExtension/app-proxy-provider.md).

## Deploying a URL filter provider

When building a URL filter provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS |
| --- | --- | --- |
| iOS | app extension | 26.0 |
| macOS | app extension | 26.0 |

For more information, see [URL filters](../NetworkExtension/url-filters.md).

## Deploying a content filter provider

When building a content filter provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| iOS | app extension | 9.0 | supervised devices only |
|  | app extension | 15.0 | apps using Screen Time APIs |
|  | app extension | 16.0 | per-app on managed devices |
| visionOS | app extension | 1.1 | per-app on managed devices |
|  | app extension | 2.0 | supervised devices |
| macOS | system extension | 10.15 |  |

For more information, see [Content filter providers](../NetworkExtension/content-filter-providers.md).

In the Screen Time case, content filters are only supported on child devices.  To enable a content filter:

1. Add the Family Controls capability to your app.  See [Adding capabilities to your app](../Xcode/adding-capabilities-to-your-app.md).
2. Run it on a device where the user has signed in as an under 18 child member of an iCloud family.
3. Request child authorization. On iOS 16 and later, call [`requestAuthorization(for:)`](../FamilyControls/authorizationcenter/requestauthorization%28for%29.md), passing in the `.child` option. On iOS 15, call [`requestAuthorization(completionHandler:)`](../FamilyControls/authorizationcenter/requestauthorization%28completionhandler%29.md), which always requests child authorization.
4. Authorize that as the child’s parent or guardian.

Before submitting your app to the App Store, you must request permission to use the [`Family Controls`](../BundleResources/entitlements/com.apple.developer.family-controls.md) entitlement for distribution.

## Deploying a DNS proxy provider

When building a DNS proxy provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| iOS | app extension | 11.0 | supervised devices only |
|  | app extension | 16.0 | per-app on managed devices |
| visionOS | app extension | 1.1 | per-app on managed devices |
|  | app extension | 2.0 | supervised devices |
| macOS | system extension | 10.15 |  |

For more information, see [DNS proxy provider](../NetworkExtension/dns-proxy-provider.md).

## Deploying a transparent proxy provider

When building a transparent proxy provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| macOS | app extension | 10.15 | App Store only |
|  | system extension | 10.15 |  |

For more information, see the discussion of transparent proxies within [App proxy provider](../NetworkExtension/app-proxy-provider.md).

macOS 11.0 introduced significant improvements to the transparent proxy feature; for the details, see [`NETransparentProxyProvider`](../NetworkExtension/netransparentproxyprovider.md).

## Deploying a packet filter provider

When building a packet filter provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS |
| --- | --- | --- |
| macOS | system extension | 10.15 |

For more information, see [Content filter providers](../NetworkExtension/content-filter-providers.md).

## Deploying an Ethernet tunnel provider

When building an Ethernet tunnel provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS | Restrictions |
| --- | --- | --- | --- |
| macOS | app extension | 13.0 | App Store only |
|  | system extension | 13.0 |  |

For more information, see [`NEEthernetTunnelProvider`](../NetworkExtension/neethernettunnelprovider.md).

## Deploying an app push provider

When building an app push provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS |
| --- | --- | --- |
| iOS | app extension | 14.0 |
| visionOS | app extension | 1.0 |

For more information, see [Local push connectivity](../NetworkExtension/local-push-connectivity.md).

## Deploying a hotspot provider

When building a hotspot provider, use the following table to plan your deployment:

| Platform | Packaged as | Minimum OS |
| --- | --- | --- |
| iOS | app extension | 26.0 |
| visionOS | app extension | 26.0 |

For more information about hotspot providers, see [Hotspot helper](../NetworkExtension/hotspot-helper.md).

Before starting development, request permission to use the `com.apple.developer.networking.HotspotHelper` entitlement.  See [Hotspot helper](../NetworkExtension/hotspot-helper.md) for the details.

## Revision History

- **2025-08-19** Added sections for URL filter and hotspot providers.  Added visionOS entries to the appropriate tables.  Clarified the role of MDM in per-app configurations.  Made other minor editorial changes.
- **2023-11-28** Clarified the Family Controls behaviour for content filter providers on iOS.
- **2023-10-03** Updated for tvOS 17.
- **2022-09-06** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3134-network-extension-provider-deployment)*