# merchantIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A string that identifies the merchant.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var merchantIdentifier: String { get set }
```

#### Discussion

This string needs to match one of the merchant IDs you registered with the Developer Portal or in Xcode, which the [`Merchant IDs Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.in-app-payments) specifies in the app’s entitlements. For more information on adding merchant IDs, see [`Configure Apple Pay (iOS, watchOS)`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/deva43983eb7?sub=dev171483d6e).

## See Also

- [var merchantCapabilities: PKMerchantCapability](pkdisbursementrequest/merchantcapabilities.md)
  A value that represents the payment-processing capabilities of the merchant.
- [var supportedNetworks: [PKPaymentNetwork]](pkdisbursementrequest/supportednetworks.md)
  An array of payment networks the merchant supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/merchantidentifier)*