# com.apple.developer.networking.manage-thread-network-credentials

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app can use ThreadNetwork.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- visionOS 1.0+

#### Discussion

Use this entitlement while developing and testing your app. Update your Xcode project by opening the Capabilities library to add Managed Thread Network Credentials (development) to your app.

Once you’re ready to publish your app, request distribution permission for this entitlement from the [`ThreadNetwork Framework Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/threadnetwork) page. If approved, go to the Developer Portal and enable the assigned Manage Thread Network Credentials entitlement that includes the new distribution access.

For implementation issues and questions about API and tools, please submit a [`support request`](https://developer.apple.comhttps://developer.apple.com/support/technical/).

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
- [5G Network Slicing App Category](entitlements/com.apple.developer.networking.slicing.appcategory.md)
  The key that defines the app category entitlement to enable Cellular Network Slicing.
- [5G Network Slicing Traffic Category](entitlements/com.apple.developer.networking.slicing.trafficcategory.md)
  The key that defines the traffic category entitlement to enable Cellular Network Slicing.
- [com.apple.developer.networking.vmnet](entitlements/com.apple.developer.networking.vmnet.md)
- [com.apple.developer.networking.carrier-constrained.appcategory](entitlements/com.apple.developer.networking.carrier-constrained.appcategory.md)
  The key that defines an app’s category for accessing a carrier-provided satellite network.
- [com.apple.developer.networking.carrier-constrained.app-optimized](entitlements/com.apple.developer.networking.carrier-constrained.app-optimized.md)
  A Boolean value that indicates whether your app is optimized for a carrier-provided satellite network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.manage-thread-network-credentials)*