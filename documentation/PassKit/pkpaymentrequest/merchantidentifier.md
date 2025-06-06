# merchantIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

Your merchant identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var merchantIdentifier: String { get set }
```

#### Discussion

This value must match one of the merchant identifiers specified by the [`Merchant IDs Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.in-app-payments) key in the app’s entitlements. For more information on adding merchant IDs, see [`Configure Apple Pay (iOS, watchOS)`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/deva43983eb7?sub=dev171483d6e).

## See Also

- [PKPaymentRequest.MerchantCategoryCode](pkpaymentrequest/merchantcategorycode-swift.struct.md)
  An optional four-digit struct, in ISO 18245 format, that represents the type of goods or service the merchant provides for the transaction.
- [var merchantCapabilities: PKMerchantCapability](pkpaymentrequest/merchantcapabilities.md)
  A bit field of the payment-processing protocols and card types that you support.
- [struct PKMerchantCapability](pkmerchantcapability.md)
  Capabilities for processing payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/merchantidentifier)*