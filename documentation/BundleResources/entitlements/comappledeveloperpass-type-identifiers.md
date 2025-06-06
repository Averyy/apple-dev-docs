# Pass Type IDs Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A list of identifiers that specify pass types that your app can access in Wallet.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- visionOS 1.0+
- watchOS 2.0+

#### Discussion

The value for this key is an array of pass type identifiers.

To add this entitlement to your app, enable the Wallet capability in Xcode. If your provisioning profile is associated with multiple pass type identifiers, specify which of the identifiers your app can interact with. Use `$(TeamIdentifierPrefix)*` to access all of the passes for your team.

For more information, see [`Configure Wallet (iOS, watchOS)`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devfc3f493bb).

> **Note**:  In iOS 17 and later, App Clips can use the Wallet capability. For more information on functionality that’s available to App Clips, see [`Choosing the right functionality for your App Clip`](https://developer.apple.com/documentation/AppClip/choosing-the-right-functionality-for-your-app-clip).

 In iOS 17 and later, App Clips can use the Wallet capability. For more information on functionality that’s available to App Clips, see [`Choosing the right functionality for your App Clip`](https://developer.apple.com/documentation/AppClip/choosing-the-right-functionality-for-your-app-clip).

## See Also

- [Merchant IDs Entitlement](entitlements/com.apple.developer.in-app-payments.md)
  A list of merchant IDs your app uses for Apple Pay support.
- [com.apple.developer.in-app-identity-presentment](entitlements/com.apple.developer.in-app-identity-presentment.md)
- [com.apple.developer.in-app-identity-presentment.merchant-identifiers](entitlements/com.apple.developer.in-app-identity-presentment.merchant-identifiers.md)
- [ID Verifier - Display Only](entitlements/com.apple.developer.proximity-reader.identity.display.md)
- [ID Verifier - Data Transfer](entitlements/com.apple.developer.proximity-reader.identity.read.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.pass-type-identifiers)*