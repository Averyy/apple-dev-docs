# init(number:fullName:cardType:verificationNumber:expiryDate:validFrom:)

**Framework**: Authentication Services  
**Kind**: init

Creates a credit card instance.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
init(number: String, fullName: String, cardType: String? = nil, verificationNumber: String? = nil, expiryDate: String? = nil, validFrom: String? = nil)
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