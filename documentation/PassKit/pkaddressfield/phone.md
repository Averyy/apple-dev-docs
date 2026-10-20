# phone

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

The buyer’s telephone number.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use PKContactField and -requiredShippingContactFields / -requiredBillingContactFields

## Declaration

```swift
static var phone: PKAddressField { get }
```

```c
PKAddressFieldPhone
```

## See Also

### Constants
- [static var postalAddress: PKAddressField](./postaladdress.md)
  The buyer’s full street address, including name, street, city, state or province, postal code, and country or region.
- [static var email: PKAddressField](./email.md)
  The buyer’s email address.
- [static var name: PKAddressField](./name.md)
  The buyer’s first and last name.
- [static var all: PKAddressField](./all.md)
  All fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddressfield/phone)*