# PKAddressField

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct  
**Role**: Structure

Billing or shipping address fields.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: This field is deprecated. Use [`PKContactField`](./pkcontactfield.md) instead.

## Declaration

```swift
struct PKAddressField
```

```c
enum PKAddressField : NSUInteger;
```

## Topics

### Constants
- [static var postalAddress: PKAddressField](./pkaddressfield/postaladdress.md)
  The buyer’s full street address, including name, street, city, state or province, postal code, and country or region.
- [static var phone: PKAddressField](./pkaddressfield/phone.md)
  The buyer’s telephone number.
- [static var email: PKAddressField](./pkaddressfield/email.md)
  The buyer’s email address.
- [static var name: PKAddressField](./pkaddressfield/name.md)
  The buyer’s first and last name.
- [static var all: PKAddressField](./pkaddressfield/all.md)
  All fields.
### Initializers
- [init(rawValue: UInt)](./pkaddressfield/init%28rawvalue%29.md)
### Enumeration Cases
- [PKAddressFieldNone](./pkaddressfield/pkaddressfieldnone.md)
  No fields.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Deprecated
- [var applePayLaterAvailability: PKPaymentRequest.ApplePayLaterAvailability](./pkpaymentrequest/applepaylateravailability-3dxrt.md)
  A value that indicates whether Apple Pay Later is available for a transaction.
- [PKPaymentRequest.ApplePayLaterAvailability](./pkpaymentrequest/applepaylateravailability-swift.enum.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.
- [enum PKApplePayLaterAvailability](./pkapplepaylateravailability.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.
- [applePayLaterAvailability](./pkpaymentrequest/applepaylateravailability-inpf.md)
  A value that indicates whether Apple Pay Later is available for a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddressfield)*