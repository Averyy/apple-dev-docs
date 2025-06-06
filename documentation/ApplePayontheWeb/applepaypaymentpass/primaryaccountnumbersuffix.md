# primaryAccountNumberSuffix

**Framework**: Apple Pay on the Web  
**Kind**: property

A version of the primary account number suitable for display in your UI.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required DOMString primaryAccountNumberSuffix;
```

#### Discussion

Note that this value is typically the last four or five digits of the account number, but the number of digits can vary by issuer. This value is not related to the value of the [`primaryAccountIdentifier`](applepaypaymentpass/primaryaccountidentifier.md) value.

## See Also

- [primaryAccountIdentifier](applepaypaymentpass/primaryaccountidentifier.md)
  The unique identifier for the primary account number for the payment card.
- [deviceAccountIdentifier](applepaypaymentpass/deviceaccountidentifier.md)
  The unique identifier for the device-specific account number.
- [deviceAccountNumberSuffix](applepaypaymentpass/deviceaccountnumbersuffix.md)
  A version of the device account number suitable for display in your UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentpass/primaryaccountnumbersuffix)*