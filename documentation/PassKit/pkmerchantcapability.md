# PKMerchantCapability

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

Capabilities for processing payment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct PKMerchantCapability
```

## Topics

### Initializers
- [init(rawValue: UInt)](pkmerchantcapability/init(rawvalue:).md)
  Creates a merchant capability using the raw value you provide.
### Constants
- [static var instantFundsOut: PKMerchantCapability](pkmerchantcapability/instantfundsout.md)
  The value that indicates the merchant supports disbursing funds using Instant Funds Out.
- [static var threeDSecure: PKMerchantCapability](pkmerchantcapability/threedsecure.md)
  Support for the 3-D Secure protocol.
- [static var emv: PKMerchantCapability](pkmerchantcapability/emv.md)
  Support for the EMV protocol.
- [static var credit: PKMerchantCapability](pkmerchantcapability/credit.md)
  Support for credit cards.
- [static var debit: PKMerchantCapability](pkmerchantcapability/debit.md)
  Support for debit cards.
### Type Properties
- [static var capability3DS: PKMerchantCapability](pkmerchantcapability/capability3ds.md)
- [static var capabilityCredit: PKMerchantCapability](pkmerchantcapability/capabilitycredit.md)
- [static var capabilityDebit: PKMerchantCapability](pkmerchantcapability/capabilitydebit.md)
- [static var capabilityEMV: PKMerchantCapability](pkmerchantcapability/capabilityemv.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [PKPaymentRequest.MerchantCategoryCode](pkpaymentrequest/merchantcategorycode-swift.struct.md)
  An optional four-digit struct, in ISO 18245 format, that represents the type of goods or service the merchant provides for the transaction.
- [var merchantIdentifier: String](pkpaymentrequest/merchantidentifier.md)
  Your merchant identifier.
- [var merchantCapabilities: PKMerchantCapability](pkpaymentrequest/merchantcapabilities.md)
  A bit field of the payment-processing protocols and card types that you support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkmerchantcapability)*