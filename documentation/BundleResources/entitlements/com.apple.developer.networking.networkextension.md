# Network Extensions Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The APIs an app can use to customize networking features.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Details

- **Name**: `com.apple.developer.networking.networkextension` (Network Extensions)
- **Type**: array of string 

## Possible Values

- `dns-proxy`: The APIs you use to proxy DNS queries.
- `app-proxy-provider`: The APIs you use to proxy TCP and UDP connections.
- `content-filter-provider`: The filter APIs you use to allow or deny network connections created by other apps on the system.
- `packet-tunnel-provider`: The APIs you use to tunnel IP packets to a remote network using any custom tunneling protocol.
- `dns-proxy-systemextension`: The APIs you use to proxy DNS queries, when signed with a Developer ID profile.
- `app-proxy-provider-systemextension`: The APIs you use to proxy TCP and UDP connections, when signed with a Developer ID profile.
- `content-filter-provider-systemextension`: The filter APIs you use to allow or deny network connections created by other apps on the system, when signed with a Developer ID profile.
- `packet-tunnel-provider-systemextension`: The APIs you use to tunnel IP packets to a remote network using any custom tunneling protocol, when signed with a Developer ID profile.
- `dns-settings`: The APIs you use to create and manage a system-wide DNS configuration.
- `app-push-provider`: The APIs you use for providing functionality similar to Apple Push Notification Service when access to the wider internet is unavailable.
- `relay`: The APIs you use to relay TCP and UDP connections, when signed with a Developer ID profile.
- `url-filter-provider`: The APIs you use to create and manage [URL filters](../../NetworkExtension/url-filters.md).

## Discussion

To add this entitlement to an App Store app, enable the Network Extensions capability in Xcode.

To add this entitlement to a macOS app distributed outside of the Mac App Store, perform the following steps:

1. In the Certificates, Identifiers and Profiles section of the developer site, enable the Network Extension capability for your Developer ID–signed app. Generate a new provisioning profile and download it.
2. On your Mac, drag the downloaded provisioning profile to Xcode to install it.
3. In your Xcode project, enable manual signing and select the provisioning profile downloaded earlier and its associated certificate.
4. Update the project’s `entitlements.plist` to include the `com.apple.developer.networking.networkextension` key and the values of the entitlement.

## See Also

### Networking
- [Personal VPN Entitlement](./com.apple.developer.networking.vpn.api.md)
  The API an app can use to create and control a custom system VPN configuration.
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

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.networkextension)*