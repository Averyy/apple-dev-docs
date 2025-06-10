# Network Extensions Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

The APIs an app can use to customize networking features.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

#### Discussion

To add this entitlement to an App Store app, enable the Network Extensions capability in Xcode.

To add this entitlement to a macOS app distributed outside of the Mac App Store, perform the following steps:

1. In the Certificates, Identifiers and Profiles section of the developer site, enable the Network Extension capability for your Developer ID–signed app. Generate a new provisioning profile and download it.
2. On your Mac, drag the downloaded provisioning profile to Xcode to install it.
3. In your Xcode project, enable manual signing and select the provisioning profile downloaded earlier and its associated certificate.
4. Update the project’s `entitlements.plist` to include the `com.apple.developer.networking.networkextension` key and the values of the entitlement.

## See Also

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
- [5G Network Slicing Traffic Category](entitlements/com.apple.developer.networking.slicing.trafficcategory.md)
  The key that defines the traffic category entitlement to enable Cellular Network Slicing.
- [com.apple.developer.networking.vmnet](entitlements/com.apple.developer.networking.vmnet.md)
- [com.apple.developer.networking.carrier-constrained.appcategory](entitlements/com.apple.developer.networking.carrier-constrained.appcategory.md)
  The key that defines an app’s category for accessing a carrier-provided satellite network.
- [com.apple.developer.networking.carrier-constrained.app-optimized](entitlements/com.apple.developer.networking.carrier-constrained.app-optimized.md)
  A Boolean value that indicates whether your app is optimized for a carrier-provided satellite network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.networkextension)*