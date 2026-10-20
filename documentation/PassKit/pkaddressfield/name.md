# name

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

The buyer’s first and last name.

**Availability**:
- iOS 8.3+ - Deprecated in 11.0
- iPadOS 8.3+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 4.0

## Declaration

```swift
static var name: PKAddressField { get }
```

```c
PKAddressFieldName
```

#### Discussion

This constant lets you request the name used for shipping or billing. The name is also included as part of the postal address field. The system only handles the name as a separate field when the postal address is not requested.

## See Also

### Constants
- [static var postalAddress: PKAddressField](./postaladdress.md)
  The buyer’s full street address, including name, street, city, state or province, postal code, and country or region.
- [static var phone: PKAddressField](./phone.md)
  The buyer’s telephone number.
- [static var email: PKAddressField](./email.md)
  The buyer’s email address.
- [static var all: PKAddressField](./all.md)
  All fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddressfield/name)*