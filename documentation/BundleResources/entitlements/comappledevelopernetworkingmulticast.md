# com.apple.developer.networking.multicast

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an app can send or receive IP multicast traffic.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- visionOS 1.0+

#### Discussion

Your app must have this entitlement to send or receive IP multicast or broadcast on iOS. It also allows your app to browse and advertise arbitrary Bonjour service types.

This entitlement requires permission from Apple before you can use it in your app. Request permission from the [`Multicast Networking Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/networking-multicast) page.

## See Also

- [Network Extensions Entitlement](entitlements/com.apple.developer.networking.networkextension.md)
  The APIs an app can use to customize networking features.
- [Personal VPN Entitlement](entitlements/com.apple.developer.networking.vpn.api.md)
  The API an app can use to create and control a custom system VPN configuration.
- [Associated Domains Entitlement](entitlements/com.apple.developer.associated-domains.md)
  The associated domains for specific services, such as shared web credentials, universal links, and App Clips.
- [com.apple.developer.associated-domains.applinks.read-write](entitlements/com.apple.developer.associated-domains.applinks.read-write.md)
  A Boolean value that indicates whether the app can use universal links.
- [com.apple.developer.networking.manage-thread-network-credentials](entitlements/com.apple.developer.networking.manage-thread-network-credentials.md)
  A Boolean value that indicates whether the app can use ThreadNetwork.
- [5G Network Slicing App Category](entitlements/com.apple.developer.networking.slicing.appcategory.md)
  The key that defines the app category entitlement to enable Cellular Network Slicing.
- [5G Network Slicing Traffic Category](entitlements/com.apple.developer.networking.slicing.trafficcategory.md)
  The key that defines the traffic category entitlement to enable Cellular Network Slicing.
- [com.apple.developer.networking.vmnet](entitlements/com.apple.developer.networking.vmnet.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.multicast)*