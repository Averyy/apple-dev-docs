# ASImportableCredential.CreditCard

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

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
- [var number: ASImportableEditableField?](./creditcard/number.md)
  The card number.
- [var fullName: ASImportableEditableField?](./creditcard/fullname.md)
  The full name of the card owner.
- [var cardType: ASImportableEditableField?](./creditcard/cardtype.md)
  The card type, if any.
- [var verificationNumber: ASImportableEditableField?](./creditcard/verificationnumber.md)
  The verification number, such as the CVC code.
- [var expiryDate: ASImportableEditableField?](./creditcard/expirydate.md)
  The expiration date, if any, in MM/DD format.
- [var validFrom: ASImportableEditableField?](./creditcard/validfrom.md)
  The date from which the card is valid, if any.
### Initializers
- [init(number: ASImportableEditableField?, fullName: ASImportableEditableField?, cardType: ASImportableEditableField?, verificationNumber: ASImportableEditableField?, pin: ASImportableEditableField?, expiryDate: ASImportableEditableField?, validFrom: ASImportableEditableField?)](./creditcard/init%28number,fullname,cardtype,verificationnumber,pin,expirydate,validfrom%29.md)
### Instance Properties
- [var pin: ASImportableEditableField?](./creditcard/pin.md)
  Optional: The PIN number.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identity credential types
- [case creditCard(ASImportableCredential.CreditCard)](./creditcard%28_%29.md)
  A credit card credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/creditcard)*