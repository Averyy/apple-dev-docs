# merchantCategoryCode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An optional four-digit property, in ISO 18245 format, that represents the type of goods or service the merchant provides for the transaction.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
@property (nonatomic, assign) PKMerchantCategoryCode merchantCategoryCode;
```

## See Also

### Setting merchant information
- [PKMerchantCategoryCode](../pkmerchantcategorycode.md)
  The optional four-digit type, in ISO 18245 format, that represents the type of goods or service the merchant provides for the transaction.
- [PKMerchantCategoryCodeNone](../pkmerchantcategorycodenone.md)
- [var merchantIdentifier: String](./merchantidentifier.md)
  Your merchant identifier.
- [var merchantCapabilities: PKMerchantCapability](./merchantcapabilities.md)
  A bit field of the payment-processing protocols and card types that you support.
- [struct PKMerchantCapability](../pkmerchantcapability.md)
  Capabilities for processing payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/merchantcategorycode-7vg6z)*