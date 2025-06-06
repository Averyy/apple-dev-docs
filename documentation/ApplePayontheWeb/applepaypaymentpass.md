# ApplePayPaymentPass

**Framework**: Apple Pay on the Web  
**Kind**: struct

A provisioned payment card for Apple Pay payments.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayPaymentPass {
	required DOMString primaryAccountIdentifier;
	required DOMString primaryAccountNumberSuffix;
	DOMString deviceAccountIdentifier;
	DOMString deviceAccountNumberSuffix;
	required ApplePayPaymentPassActivationState activationState;
};
```

#### Overview

Payment pass information is populated only for cobranded or private label cards, for specially registered websites.

## Topics

### Account Identity
- [primaryAccountIdentifier](applepaypaymentpass/primaryaccountidentifier.md)
  The unique identifier for the primary account number for the payment card.
- [primaryAccountNumberSuffix](applepaypaymentpass/primaryaccountnumbersuffix.md)
  A version of the primary account number suitable for display in your UI.
- [deviceAccountIdentifier](applepaypaymentpass/deviceaccountidentifier.md)
  The unique identifier for the device-specific account number.
- [deviceAccountNumberSuffix](applepaypaymentpass/deviceaccountnumbersuffix.md)
  A version of the device account number suitable for display in your UI.
### Activation State
- [activationState](applepaypaymentpass/activationstate.md)
  The activation state of the pass.
- [ApplePayPaymentPassActivationState](applepaypaymentpassactivationstate.md)
  Payment pass activation states.

## See Also

- [token](applepaypayment/token.md)
  The encrypted information for an authorized payment.
- [ApplePayPaymentToken](applepaypaymenttoken.md)
  An object that contains the user’s payment credentials.
- [ApplePayPaymentMethod](applepaypaymentmethod.md)
  A dictionary that describes an Apple Pay payment method.
- [ApplePayPaymentMethodType](applepaypaymentmethodtype.md)
  A string that represents the type of the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentpass)*