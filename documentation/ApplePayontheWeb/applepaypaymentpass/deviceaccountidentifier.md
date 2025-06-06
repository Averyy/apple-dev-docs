# deviceAccountIdentifier

**Framework**: Apple Pay on the Web  
**Kind**: property

The unique identifier for the device-specific account number.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
DOMString deviceAccountIdentifier;
```

#### Discussion

This number is not the account number itself. If the pass has not been provisioned, the value of this property is `nil`.

## See Also

- [primaryAccountIdentifier](applepaypaymentpass/primaryaccountidentifier.md)
  The unique identifier for the primary account number for the payment card.
- [primaryAccountNumberSuffix](applepaypaymentpass/primaryaccountnumbersuffix.md)
  A version of the primary account number suitable for display in your UI.
- [deviceAccountNumberSuffix](applepaypaymentpass/deviceaccountnumbersuffix.md)
  A version of the device account number suitable for display in your UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentpass/deviceaccountidentifier)*