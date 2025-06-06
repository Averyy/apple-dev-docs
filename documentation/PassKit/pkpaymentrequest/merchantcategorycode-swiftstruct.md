# PKPaymentRequest.MerchantCategoryCode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

An optional four-digit struct, in ISO 18245 format, that represents the type of goods or service the merchant provides for the transaction.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
struct MerchantCategoryCode
```

#### Overview

The four-digit merchant category codes are in ISO 18245 format and range from 1 to 9999.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [LosslessStringConvertible](../Swift/LosslessStringConvertible.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var merchantIdentifier: String](pkpaymentrequest/merchantidentifier.md)
  Your merchant identifier.
- [var merchantCapabilities: PKMerchantCapability](pkpaymentrequest/merchantcapabilities.md)
  A bit field of the payment-processing protocols and card types that you support.
- [struct PKMerchantCapability](pkmerchantcapability.md)
  Capabilities for processing payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/merchantcategorycode-swift.struct)*