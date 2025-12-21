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

- Do not use a packet tunnel provider to implement a network content filter. Packets that are read from [`NEPacketTunnelFlow`](https://developer.apple.com/documentation/NetworkExtension/NEPacketTunnelFlow) are meant to be sent over a tunnel connection to a remote server for injection into a remote network. They are not meant to be dropped or re-injected back into the system. Doing so is a content filter action, as supported by one of the Network Extension [`Content filter providers`](https://developer.apple.com/documentation/NetworkExtension/content-filter-providers). On iOS, implement a connection-based content filter using [`NEFilterDataProvider`](https://developer.apple.com/documentation/NetworkExtension/NEFilterDataProvider) and [`NEFilterControlProvider`](https://developer.apple.com/documentation/NetworkExtension/NEFilterControlProvider). On macOS, implement a connection-based content filter with `NEFilterDataProvider` or a packet-based content filter with [`NEFilterPacketProvider`](https://developer.apple.com/documentation/NetworkExtension/NEFilterPacketProvider). On macOS, using both providers at the same time is supported. For information on how to deploy a content filter, see [`TN3134: Network Extension provider deployment`](tn3134-network-extension-provider-deployment.md).  If those options don’t work for your product, consider creating a [`URL filters`](https://developer.apple.com/documentation/NetworkExtension/url-filters).
- Do not use a packet tunnel provider to intercept all DNS traffic on the system.
For small sets of DNS traffic inside your isolated network, this is reasonable. However, trying to intercept all DNS traffic on the system can result in endless edge cases and problems during development and deployment. As an alternative use the [`NEDNSProxyProvider`](https://developer.apple.com/documentation/NetworkExtension/NEDNSProxyProvider) or the [`DNS settings`](https://developer.apple.com/documentation/NetworkExtension/dns-settings) APIs.  These APIs were built for handling all DNS traffic on the system.
- Do not use a packet tunnel provider to selectively claim traffic for the packet tunnel and proxy all other traffic elsewhere. Traffic that is claimed by a `NEPacketTunnelProvider` is meant to be sent through the tunnel connection and not be routed through another interface via a proxy.  The recommended alternative is to implement a [`NETransparentProxyProvider`](https://developer.apple.com/documentation/NetworkExtension/NETransparentProxyProvider) on macOS.  On iOS, consider either claiming the network traffic that’s needed for your tunnel with [`NETunnelProviderManager`](https://developer.apple.com/documentation/NetworkExtension/NETunnelProviderManager) or claiming traffic by destination IP with [`includedRoutes`](https://developer.apple.com/documentation/NetworkExtension/NEIPv4Settings/includedRoutes).  To learn more about how the system routes VPN traffic, see [`Routing your VPN network traffic`](https://developer.apple.com/documentation/NetworkExtension/routing-your-vpn-network-traffic).
- Do not use a packet tunnel provider to host a network listener or proxy server.
There is no reasonable alternative here other than using one of the [`App proxy provider`](https://developer.apple.com/documentation/NetworkExtension/app-proxy-provider) APIs.  This path is simply not a recommended use case for a packet tunnel provider or any other Network Extension.

Avoiding the unsupported scenarios will save your project many edges cases and bugs during the development and deployment process.

#### Revision History

-  Added a reference to the new [`URL filters`](https://developer.apple.com/documentation/NetworkExtension/url-filters) mechanism.  Added links to documents that further explain specific topics.  Fixed a broken link.  Made other minor editorial changes.
-  Made minor editorial changes.
-  Added additional links to APIs.
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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3120-expected-use-cases-for-network-extension-packet-tunnel-providers)*