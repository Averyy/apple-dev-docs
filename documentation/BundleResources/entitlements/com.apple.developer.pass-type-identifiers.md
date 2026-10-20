# Pass Type IDs Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A list of identifiers that specify pass types that your app can access in Wallet.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- visionOS 1.0+
- watchOS 2.0+

## Details

- **Name**: `com.apple.developer.pass-type-identifiers` (Pass Type IDs)
- **Type**: array of string 

#### Discussion

The value for this key is an array of pass type identifiers.

To add this entitlement to your app, enable the Wallet capability in Xcode. If your provisioning profile is associated with multiple pass type identifiers, specify which of the identifiers your app can interact with. Use `$(TeamIdentifierPrefix)*` to access all of the passes for your team.

For more information, see [Configure Wallet (iOS, watchOS)](https://help.apple.com/xcode/mac/current/#/devfc3f493bb).

> **Note**:  In iOS 17 and later, App Clips can use the Wallet capability. For more information on functionality that’s available to App Clips, see [Choosing the right functionality for your App Clip](../../AppClip/choosing-the-right-functionality-for-your-app-clip.md).

## See Also

### Wallet
- [Merchant IDs Entitlement](./com.apple.developer.in-app-payments.md)
  A list of merchant IDs your app uses for Apple Pay support.
- [com.apple.developer.in-app-identity-presentment](./com.apple.developer.in-app-identity-presentment.md)
  An entitlement that verifies age or identity.
- [com.apple.developer.in-app-identity-presentment.merchant-identifiers](./com.apple.developer.in-app-identity-presentment.merchant-identifiers.md)
  An entitlement for the merchant identifier associated with the in-app identity presentment entitlement.
- [ID Verifier - Display Only](./com.apple.developer.proximity-reader.identity.display.md)
- [ID Verifier - Data Transfer](./com.apple.developer.proximity-reader.identity.read.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.pass-type-identifiers)*