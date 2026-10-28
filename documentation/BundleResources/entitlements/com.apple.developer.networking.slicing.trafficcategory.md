# 5G Network Slicing Traffic Category

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The key that defines the traffic category entitlement to enable Cellular Network Slicing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Details

- **Name**: `com.apple.developer.networking.slicing.trafficcategory`
- **Type**: array of string 

## Possible Values

- `defaultslice-1`: A service type for Cellular Network Slicing when not setting the other service types.
- `video-2`: A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- `background-3`: A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.
- `voice-4`: A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- `callsignaling-5`: A service for low-loss tolerant, inelastic-flow, jitter tolerant, bursty but short rate, and variable size connections.
- `responsivedata-6`: A service type for medium-delay tolerant, elastic and inelastic flow, bursty, and long-lived connections.
- `avstreaming-7`: A service type for medium-delay tolerant, low-medium-loss tolerant, elastic flow, constant packet interval, variable rate, and size connections.
- `responsiveav-8`: A service type for low-delay tolerant, low-to-medium-loss tolerant, elastic flow, variable packet interval, rate, and size responsive (time-sensitive) connections.

## Discussion

To enable Cellular Network Slicing, you need to set the appropriate entitlements and properties.

Set this entitlement and the [5G Network Slicing App Category](./com.apple.developer.networking.slicing.appcategory.md) entitlement in your property list. If you don’t entitle your app by specifying both these entitlements, your apps network connections won’t use Cellular Network Slicing, even if supported by the carrier.

Use this array to define the different slice types your app’s entitled to. For example, if your app opens network connections using the network service types video, voice, and call signaling, the entitlement property must include `video-2`, `voice-4,` and `callsignaling-5` values for this entitlement key.

Also set one of the following properties, depending on your app’s networking implementation:

- Set [`serviceClass`](../../Network/nwparameters/serviceclass-swift.property.md) when using the Networking framework.
- Set [`networkServiceType`](../../Foundation/urlsessionconfiguration/networkservicetype.md) when using [`URLSessionConfiguration`](../../Foundation/urlsessionconfiguration.md).
- Set [`networkServiceType`](../../Foundation/urlrequest/networkservicetype-swift.property.md) when using [`URLRequest`](../../Foundation/urlrequest.md).

If your app uses sockets, set this entitlement to `defaultslice-1`. With sockets, all your app traffic uses a slice defined by the carrier to accept all traffic categories. You should still set the [5G Network Slicing App Category](./com.apple.developer.networking.slicing.appcategory.md) entitlement.

> **Note**:  Cellular Network Slicing is only available on supported carriers. Check with individual carriers for availability.

## See Also

### Networking
- [Network Extensions Entitlement](./com.apple.developer.networking.networkextension.md)
  The APIs an app can use to customize networking features.
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
- [com.apple.developer.networking.vmnet](./com.apple.developer.networking.vmnet.md)
- [Configuring your app for ultra-constrained networks](../configuring-your-app-for-ultra-constrained-networks.md)
  Prepare to deliver data over resource-limited data networks.
- [com.apple.developer.networking.carrier-constrained.appcategory](./com.apple.developer.networking.carrier-constrained.appcategory.md)
  The key that defines an app’s category for accessing a carrier-provided satellite network.
- [com.apple.developer.networking.carrier-constrained.app-optimized](./com.apple.developer.networking.carrier-constrained.app-optimized.md)
  A Boolean value that indicates whether your app is optimized for a carrier-provided satellite network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.slicing.trafficcategory)*