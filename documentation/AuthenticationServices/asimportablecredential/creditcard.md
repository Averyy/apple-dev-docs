# ASImportableCredential.CreditCard

**Framework**: Authentication Services  
**Kind**: struct

A type to represent credit card information.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct CreditCard
```

#### Overview

This type is a representation of `CreditCard` as defined in the Credential Exchange Format (CXF) specification.

## Topics

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
### Initializers
- [init(number: ASImportableEditableField?, fullName: ASImportableEditableField?, cardType: ASImportableEditableField?, verificationNumber: ASImportableEditableField?, pin: ASImportableEditableField?, expiryDate: ASImportableEditableField?, validFrom: ASImportableEditableField?)](asimportablecredential/creditcard/init(number:fullname:cardtype:verificationnumber:pin:expirydate:validfrom:).md)
### Instance Properties
- [var pin: ASImportableEditableField?](asimportablecredential/creditcard/pin.md)
  Optional: The PIN number.

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