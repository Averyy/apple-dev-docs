# com.apple.developer.accessory-transport-security

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An entitlement that enables your app extension to exchange cryptographic keys with an accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Details

- **Name**: `com.apple.developer.accessory-transport-security`
- **Type**: boolean

#### Discussion

If your app implements [`AccessoryTransportSecurity`](../../AccessoryTransportExtension/accessorytransportsecurity.md) in an app extension, the framework requires the extension to have this entitlement with a value of `true` in its signature.

For more information, see [Receiving iOS notifications on an accessory](../../AccessoryTransportExtension/receiving-ios-notifications-on-an-accessory.md).

For information on adding entitlements to your app, see [Adding capabilities to your app](../../Xcode/adding-capabilities-to-your-app.md).

## See Also

### Accessory Transport Extension
- [com.apple.developer.accessory-transport-extension](./com.apple.developer.accessory-transport-extension.md)
  An entitlement that enables your app extension to send sensitive data to an accessory.
- [com.apple.developer.accessory-data-provider](./com.apple.developer.accessory-data-provider.md)
  An entitlement that enables your app extension to receive data for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.accessory-transport-security)*