# TN3120: Expected use cases for Network Extension packet tunnel providers

**Framework**: Technotes

Learn the expected use cases for Network Extension packet tunnel providers, and about use cases that are not supported.

#### Overview

[`NEPacketTunnelProvider`](https://developer.apple.com/documentation/NetworkExtension/NEPacketTunnelProvider) is very powerful and useful on Apple platforms. It has many valid use cases such as providing users access to secure resources and securing network traffic on an insecure network. While this API is very powerful, there are certain use cases that do not line up with its intended purpose. This technote briefly explains the recommended use cases for packet tunnel providers, along with common scenarios that are unsupported.

#### Recommended Use Cases for Packet Tunnel Providers

Recommended use cases for a packet tunnel provider include:

- Do use a packet tunnel provider to access secure resources on an isolated network. For example, use `NEPacketTunnelProvider` to implement an iOS or macOS VPN client that tunnels network traffic through a VPN connection into a private enterprise network. This can be done by tunneling specific destination IP and DNS traffic to the isolated network.
- Do use a packet tunnel provider to secure network access while on an insecure network.  For example, use `NEPacketTunnelProvider` to implement an iOS or macOS VPN client that tunnels network traffic through a public VPN service that provides access to the wider internet.  Common techniques used to achieve this functionality include creating a full tunnel VPN that routes all traffic to the remote VPN server that then forwards the traffic to its final destination.

#### Unsupported Uses of Packet Tunnel Providers

While there are many reasons to use a packet tunnel provider, there are also many unsupported uses of this API. If you find yourself implementing any one of the code paths below, consider using one of the suggested alternatives:

- Do not use a packet tunnel provider to implement a network content filter. Packets that are read from [`NEPacketTunnelFlow`](https://developer.apple.com/documentation/NetworkExtension/NEPacketTunnelFlow) are meant to be sent over a tunnel connection to a remote server for injection into a remote network. They are not meant to be dropped or re-injected back into the system. Doing so is a content filter action, as supported by one of the Network Extension [`Content filter providers`](https://developer.apple.com/documentation/NetworkExtension/content-filter-providers) APIs. On iOS, implement a connection-based content filter using [`NEFilterDataProvider`](https://developer.apple.com/documentation/NetworkExtension/NEFilterDataProvider) and [`NEFilterControlProvider`](https://developer.apple.com/documentation/NetworkExtension/NEFilterControlProvider). On macOS, implement a connection-based content filter with `NEFilterDataProvider` or a packet-based content filter with [`NEFilterPacketProvider`](https://developer.apple.com/documentation/NetworkExtension/NEFilterPacketProvider). On macOS, using both providers at the same time is supported. There are two ways to deploy a content filter on iOS. In a managed environment, use MDM to deploy a content filter to supervised devices. In an unmanaged environment, deploy your content filter as part of a Screen Time app.
- Do not use a packet tunnel provider to intercept all DNS traffic on the system.
For small sets of DNS traffic inside your isolated network, this is reasonable. However, trying to intercept all DNS traffic on the system can result in endless edge cases and problems during development and deployment. As an alternative use the [`NEDNSProxyProvider`](https://developer.apple.com/documentation/NetworkExtension/NEDNSProxyProvider) or the [`DNS settings`](https://developer.apple.com/documentation/NetworkExtension/dns-settings) APIs.  These APIs were built for handling all DNS traffic on the system.
- Do not use a packet tunnel provider to selectively claim traffic for the packet tunnel and proxy all other traffic elsewhere. Traffic that is claimed by a `NEPacketTunnelProvider` is meant to be sent through the tunnel connection and not be routed through another interface via a proxy.  The recommended alternative is to implement a [`NETransparentProxyProvider`](https://developer.apple.com/documentation/NetworkExtension/NETransparentProxyProvider) on macOS.  On iOS, consider either claiming the network traffic that is needed for your tunnel with [`Per-App VPN`](https://developer.apple.comhttps://developer.apple.com/documentation/networkextension/netunnelprovidermanager#2110139), or claiming traffic by destination IP with [`includedRoutes`](https://developer.apple.com/documentation/NetworkExtension/NEIPv4Settings/includedRoutes).
- Do not use a packet tunnel provider to host a network listener or proxy server.
There is no reasonable alternative here other than using one of the [`App proxy provider`](https://developer.apple.com/documentation/NetworkExtension/app-proxy-provider) APIs.  This path is simply not a recommended use case for a packet tunnel provider or any other Network Extension.

Avoiding the unsupported scenarios will save your project many edges cases and bugs during the development and deployment process.

#### Revision History

-  Made minor editorial changes.
-  Added additional links to APIs.
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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3120-expected-use-cases-for-network-extension-packet-tunnel-providers)*