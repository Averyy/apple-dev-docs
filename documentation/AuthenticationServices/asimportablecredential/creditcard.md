# ASImportableCredential.CreditCard

**Framework**: Authentication Services  
**Kind**: struct

A type to represent credit card information.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct CreditCard
```

#### Overview

This type is a representation of `CreditCard` as defined in the Credential Exchange Format (CXF) specification.

## Topics

### Creating a credit card instance
- [init(number: ASImportableEditableField?, fullName: ASImportableEditableField?, cardType: ASImportableEditableField?, verificationNumber: ASImportableEditableField?, expiryDate: ASImportableEditableField?, validFrom: ASImportableEditableField?)](asimportablecredential/creditcard/init(number:fullname:cardtype:verificationnumber:expirydate:validfrom:).md)
  Creates a credit card instance.
### Accessing credit card properties
- [var number: ASImportableEditableField?](asimportablecredential/creditcard/number.md)
  The card number.
- [var fullName: ASImportableEditableField?](asimportablecredential/creditcard/fullname.md)
  The full name of the card owner.
- [var cardType: ASImportableEditableField?](asimportablecredential/creditcard/cardtype.md)
  The card type, if any.
- [var verificationNumber: ASImportableEditableField?](asimportablecredential/creditcard/verificationnumber.md)
  The verification number, such as the CVC code.
- [var expiryDate: ASImportableEditableField?](asimportablecredential/creditcard/expirydate.md)
  The expiration date, if any, in MM/DD format.
- [var validFrom: ASImportableEditableField?](asimportablecredential/creditcard/validfrom.md)
  The date from which the card is valid, if any.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case creditCard(ASImportableCredential.CreditCard)](asimportablecredential/creditcard(_:).md)
  A credit card credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/creditcard)*