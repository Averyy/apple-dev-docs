# Personal VPN Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The API an app can use to create and control a custom system VPN configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- visionOS 1.0+

## Details

- **Name**: `com.apple.developer.networking.vpn.api` (Personal VPN)
- **Type**: array of string 

## Possible Values

- `allow-vpn`

## Discussion

With the [Personal VPN Entitlement](./com.apple.developer.networking.vpn.api.md) enabled, your app can use the [`NEVPNManager`](../../NetworkExtension/nevpnmanager.md) class to manage a Personal VPN configuration.

To add this entitlement to your app, enable the Personal VPN capability in Xcode. When the entitlement is enabled, Xcode sets the value to `allow-vpn`.

## See Also

### Networking
- [Network Extensions Entitlement](./com.apple.developer.networking.networkextension.md)
  The APIs an app can use to customize networking features.
- [Associated Domains Entitlement](./com.apple.developer.associated-domains.md)
  The associated domains for specific services, such as shared web credentials, universal links, and App Clips.
- [com.apple.developer.networking.multicast](./com.apple.developer.networking.multicast.md)
  A Boolean value that indicates whether an app can send or receive IP multicast traffic.
- [com.apple.developer.associated-domains.applinks.read-write](./com.apple.developer.associated-domains.applinks.read-write.md)
  A Boolean value that indicates whether the app can use universal links.
- [com.apple.developer.networking.manage-thread-network-credentials](./com.apple.developer.networking.manage-thread-network-credentials.md)
  A Boolean value that indicates whether the app can use ThreadNetwork.
- [5G Network Slicing App Category](./com.apple.developer.networking.slicing.appcategory.md)
  The key that defines the app category entitlement to enable Cellular Network Slicing.
- [5G Network Slicing Traffic Category](./com.apple.developer.networking.slicing.trafficcategory.md)
  The key that defines the traffic category entitlement to enable Cellular Network Slicing.
- [com.apple.developer.networking.vmnet](./com.apple.developer.networking.vmnet.md)
- [Configuring your app for ultra-constrained networks](../configuring-your-app-for-ultra-constrained-networks.md)
  Prepare to deliver data over resource-limited data networks.
- [com.apple.developer.networking.carrier-constrained.appcategory](./com.apple.developer.networking.carrier-constrained.appcategory.md)
  The key that defines an app’s category for accessing a carrier-provided satellite network.
- [com.apple.developer.networking.carrier-constrained.app-optimized](./com.apple.developer.networking.carrier-constrained.app-optimized.md)
  A Boolean value that indicates whether your app is optimized for a carrier-provided satellite network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.vpn.api)*