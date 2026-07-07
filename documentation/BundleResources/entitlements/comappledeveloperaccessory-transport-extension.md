# com.apple.developer.accessory-transport-extension

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that enables your app extension to send sensitive data to an accessory.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+



**Type**: boolean

#### Discussion

If your app implements [`AccessoryTransportAppExtension`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportAppExtension), the framework requires the extension to have this entitlement with a value of `true` in its signature.

For more information, see [`Receiving iOS notifications on an accessory`](https://developer.apple.com/documentation/AccessoryTransportExtension/receiving-ios-notifications-on-an-accessory).

For information on adding entitlements to your app, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

## See Also

- [com.apple.developer.accessory-transport-security](entitlements/com.apple.developer.accessory-transport-security.md)
  An entitlement that enables your app extension to exchange cryptographic keys with an accessory.
- [com.apple.developer.accessory-data-provider](entitlements/com.apple.developer.accessory-data-provider.md)
  An entitlement that enables your app extension to receive data for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.accessory-transport-extension)*