# Merchant IDs Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A list of merchant IDs your app uses for Apple Pay support.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- visionOS 1.0+
- watchOS 2.0+

#### Discussion

The value for this key is an array of strings containing the merchant IDs—typically in reverse domain name notation, starting with the string ‘`merchant`’.

To add this entitlement, enable the Apple Pay capability in Xcode and select the merchant IDs you want to use in your app. Alternatively, see [`Setting up Apple Pay`](https://developer.apple.com/documentation/PassKit/setting-up-apple-pay) for how to create merchant IDs in your developer account.

## See Also

- [Pass Type IDs Entitlement](entitlements/com.apple.developer.pass-type-identifiers.md)
  A list of identifiers that specify pass types that your app can access in Wallet.
- [com.apple.developer.in-app-identity-presentment](entitlements/com.apple.developer.in-app-identity-presentment.md)
- [com.apple.developer.in-app-identity-presentment.merchant-identifiers](entitlements/com.apple.developer.in-app-identity-presentment.merchant-identifiers.md)
- [ID Verifier - Display Only](entitlements/com.apple.developer.proximity-reader.identity.display.md)
- [ID Verifier - Data Transfer](entitlements/com.apple.developer.proximity-reader.identity.read.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.in-app-payments)*