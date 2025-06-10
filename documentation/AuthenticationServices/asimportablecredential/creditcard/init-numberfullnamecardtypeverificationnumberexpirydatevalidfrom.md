# init(number:fullName:cardType:verificationNumber:expiryDate:validFrom:)

**Framework**: Authentication Services  
**Kind**: init

Creates a credit card instance.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(number: ASImportableEditableField?, fullName: ASImportableEditableField?, cardType: ASImportableEditableField?, verificationNumber: ASImportableEditableField?, expiryDate: ASImportableEditableField?, validFrom: ASImportableEditableField?)
```

## Parameters

- `number`: The card number.
- `fullName`: The full name of the card owner.
- `cardType`: The card type, if any.
- `verificationNumber`: The verification number, such as the CVC code.
- `expiryDate`: The expiration date, if any, in MM/DD format.
- `validFrom`: The date from which the card is valid, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/creditcard/init(number:fullname:cardtype:verificationnumber:expirydate:validfrom:))*