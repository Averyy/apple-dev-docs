# PKAddressField

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

Billing or shipping address fields.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct PKAddressField
```

## Topics

### Constants
- [static var postalAddress: PKAddressField](pkaddressfield/postaladdress.md)
  The buyer’s full street address, including name, street, city, state or province, postal code, and country or region.
- [static var phone: PKAddressField](pkaddressfield/phone.md)
  The buyer’s telephone number.
- [static var email: PKAddressField](pkaddressfield/email.md)
  The buyer’s email address.
- [static var name: PKAddressField](pkaddressfield/name.md)
  The buyer’s first and last name.
- [static var all: PKAddressField](pkaddressfield/all.md)
  All fields.
### Initializers
- [init(rawValue: UInt)](pkaddressfield/init(rawvalue:).md)

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

- [var applePayLaterAvailability: PKPaymentRequest.ApplePayLaterAvailability](pkpaymentrequest/applepaylateravailability-3dxrt.md)
  A value that indicates whether Apple Pay Later is available for a transaction.
- [PKPaymentRequest.ApplePayLaterAvailability](pkpaymentrequest/applepaylateravailability-swift.enum.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.
- [enum PKApplePayLaterAvailability](pkapplepaylateravailability.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddressfield)*