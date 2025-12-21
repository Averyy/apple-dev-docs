# com.apple.developer.in-app-identity-presentment.merchant-identifiers

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement for the merchant identifier associated with the in-app identity presentment entitlement.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

#### Discussion

For identity verification, you must add this entitlement even if you’re using the same merchant ID for Apple Pay. Apple Pay’s [`Merchant IDs Entitlement`](entitlements/com.apple.developer.in-app-payments.md) entitlement isn’t recognized for identity verification.

## See Also

- [Pass Type IDs Entitlement](entitlements/com.apple.developer.pass-type-identifiers.md)
  A list of identifiers that specify pass types that your app can access in Wallet.
- [Merchant IDs Entitlement](entitlements/com.apple.developer.in-app-payments.md)
  A list of merchant IDs your app uses for Apple Pay support.
- [com.apple.developer.in-app-identity-presentment](entitlements/com.apple.developer.in-app-identity-presentment.md)
  An entitlement that verifies age or identity.
- [ID Verifier - Display Only](entitlements/com.apple.developer.proximity-reader.identity.display.md)
- [ID Verifier - Data Transfer](entitlements/com.apple.developer.proximity-reader.identity.read.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.in-app-identity-presentment.merchant-identifiers)*