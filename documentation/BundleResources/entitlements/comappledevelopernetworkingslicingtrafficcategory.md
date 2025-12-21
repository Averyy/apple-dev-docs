# 5G Network Slicing Traffic Category

**Framework**: Bundle Resources  
**Kind**: typealias

The key that defines the traffic category entitlement to enable Cellular Network Slicing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

#### Discussion

To enable Cellular Network Slicing, you need to set the appropriate entitlements and properties.

Set this entitlement and the [`5G Network Slicing App Category`](entitlements/com.apple.developer.networking.slicing.appcategory.md) entitlement in your property list. If you don’t entitle your app by specifying both these entitlements, your apps network connections won’t use Cellular Network Slicing, even if supported by the carrier.

Use this array to define the different slice types your app’s entitled to. For example, if your app opens network connections using the network service types video, voice, and call signaling, the entitlement property must include `video-2`, `voice-4,` and `callsignaling-5` values for this entitlement key.

Also set one of the following properties, depending on your app’s networking implementation:

- Set [`serviceClass`](https://developer.apple.com/documentation/Network/NWParameters/serviceClass-swift.property) when using the Networking framework.
- Set [`networkServiceType`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/networkServiceType) when using [`URLSessionConfiguration`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration).
- Set [`networkServiceType`](https://developer.apple.com/documentation/Foundation/URLRequest/networkServiceType-swift.property) when using [`URLRequest`](https://developer.apple.com/documentation/Foundation/URLRequest).

If your app uses sockets, set this entitlement to `defaultslice-1`. With sockets, all your app traffic uses a slice defined by the carrier to accept all traffic categories. You should still set the [`5G Network Slicing App Category`](entitlements/com.apple.developer.networking.slicing.appcategory.md) entitlement.

> **Note**:  Cellular Network Slicing is only available on supported carriers. Check with individual carriers for availability.

## See Also

- [Network Extensions Entitlement](entitlements/com.apple.developer.networking.networkextension.md)
  The APIs an app can use to customize networking features.
- [Personal VPN Entitlement](entitlements/com.apple.developer.networking.vpn.api.md)
  The API an app can use to create and control a custom system VPN configuration.
- [Associated Domains Entitlement](entitlements/com.apple.developer.associated-domains.md)
  The associated domains for specific services, such as shared web credentials, universal links, and App Clips.
- [com.apple.developer.networking.multicast](entitlements/com.apple.developer.networking.multicast.md)
  A Boolean value that indicates whether an app can send or receive IP multicast traffic.
- [com.apple.developer.associated-domains.applinks.read-write](entitlements/com.apple.developer.associated-domains.applinks.read-write.md)
  A Boolean value that indicates whether the app can use universal links.
- [com.apple.developer.networking.manage-thread-network-credentials](entitlements/com.apple.developer.networking.manage-thread-network-credentials.md)
  A Boolean value that indicates whether the app can use ThreadNetwork.
- [5G Network Slicing App Category](entitlements/com.apple.developer.networking.slicing.appcategory.md)
  The key that defines the app category entitlement to enable Cellular Network Slicing.
- [com.apple.developer.networking.vmnet](entitlements/com.apple.developer.networking.vmnet.md)
- [Configuring your app for ultra-constrained networks](configuring-your-app-for-ultra-constrained-networks.md)
  Prepare to deliver data over resource-limited data networks.
- [com.apple.developer.networking.carrier-constrained.appcategory](entitlements/com.apple.developer.networking.carrier-constrained.appcategory.md)
  The key that defines an app’s category for accessing a carrier-provided satellite network.
- [com.apple.developer.networking.carrier-constrained.app-optimized](entitlements/com.apple.developer.networking.carrier-constrained.app-optimized.md)
  A Boolean value that indicates whether your app is optimized for a carrier-provided satellite network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.slicing.trafficcategory)*