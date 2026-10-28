# merchantCapabilities

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A bit field of the payment-processing protocols and card types that you support.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var merchantCapabilities: PKMerchantCapability { get set }
```

```objc
@property (nonatomic, assign) PKMerchantCapability merchantCapabilities;
```

## Discussion

The [`threeDSecure`](../pkmerchantcapability/threedsecure.md) and [`emv`](../pkmerchantcapability/emv.md) values of [`PKMerchantCapability`](../pkmerchantcapability.md) specify the supported cryptographic payment protocols. At least one of these two values is required.

Check with your payment processors about the cryptographic payment protocols they support. As a general rule, if you want to support China UnionPay cards, you use `capabilityEMV`. To support cards from other networks—like American Express, Visa, or Mastercard—use `capability3DS`.

To filter the types of cards to make available for the transaction, pass the [`credit`](../pkmerchantcapability/credit.md) and [`debit`](../pkmerchantcapability/debit.md) values. If neither is passed, all card types will be available.

## See Also

### Setting merchant information
- [PKPaymentRequest.MerchantCategoryCode](./merchantcategorycode-swift.struct.md)
  An optional four-digit struct, in ISO 18245 format, that represents the type of goods or service the merchant provides for the transaction.
- [var merchantIdentifier: String](./merchantidentifier.md)
  Your merchant identifier.
- [struct PKMerchantCapability](../pkmerchantcapability.md)
  Capabilities for processing payment.
- [PKMerchantCategoryCode](../pkmerchantcategorycode.md)
  The optional four-digit type, in ISO 18245 format, that represents the type of goods or service the merchant provides for the transaction.
- [merchantCategoryCode](./merchantcategorycode-7vg6z.md)
  An optional four-digit property, in ISO 18245 format, that represents the type of goods or service the merchant provides for the transaction.
- [PKMerchantCategoryCodeNone](../pkmerchantcategorycodenone.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/merchantcapabilities)*