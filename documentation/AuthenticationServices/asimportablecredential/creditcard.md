# ASImportableCredential.CreditCard

**Framework**: Authentication Services  
**Kind**: struct

A type to represent credit card information.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
struct CreditCard
```

#### Overview

This type is a representation of `CreditCard` as defined in the Credential Exchange Format (CXF) specification.

## Topics

### Creating a credit card instance
- [init(number: String, fullName: String, cardType: String?, verificationNumber: String?, expiryDate: String?, validFrom: String?)](asimportablecredential/creditcard/init(number:fullname:cardtype:verificationnumber:expirydate:validfrom:).md)
  Creates a credit card instance.
### Accessing credit card properties
- [var number: String](asimportablecredential/creditcard/number.md)
  The card number.
- [var fullName: String](asimportablecredential/creditcard/fullname.md)
  The full name of the card owner.
- [var cardType: String?](asimportablecredential/creditcard/cardtype.md)
  The card type, if any.
- [var verificationNumber: String?](asimportablecredential/creditcard/verificationnumber.md)
  The verification number, such as the CVC code.
- [var expiryDate: String?](asimportablecredential/creditcard/expirydate.md)
  The expiration date, if any, in MM/DD format.
- [var validFrom: String?](asimportablecredential/creditcard/validfrom.md)
  The date from which the card is valid, if any.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [case creditCard(ASImportableCredential.CreditCard)](asimportablecredential/creditcard(_:).md)
  A credit card credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/creditcard)*