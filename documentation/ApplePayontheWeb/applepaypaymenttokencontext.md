# ApplePayPaymentTokenContext

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that defines the context for a single payment token in a payment request for multimerchant payments.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayPaymentTokenContext {
	required DOMString merchantIdentifier;
	required DOMString externalIdentifier;
	required DOMString merchantName;
	DOMString merchantDomain;
	required DOMString amount;
};
```

#### Overview

> ❗ **Important**:  You must include the [`multiTokenContexts`](applepaymodifier/multitokencontexts.md) array in the [`ApplePayPaymentRequest`](applepaypaymentrequest.md) object to request multimerchant payments.

 You must include the [`multiTokenContexts`](applepaymodifier/multitokencontexts.md) array in the [`ApplePayPaymentRequest`](applepaypaymentrequest.md) object to request multimerchant payments.

Use [`ApplePayPaymentTokenContext`](applepaypaymenttokencontext.md) to authorize a payment amount for each payment token in a multimerchant payment request. To enable multiple merchants for a transaction, use one [`ApplePayPaymentTokenContext`](applepaypaymenttokencontext.md) object for each merchant.

You can optionally associate each payment token with the merchant’s top-level domain.

## Topics

### Specifying the merchant
- [merchantIdentifier](applepaypaymenttokencontext/merchantidentifier.md)
  The Apply Pay merchant identifier.
- [merchantName](applepaypaymenttokencontext/merchantname.md)
  The merchant’s display name that the Apple Pay server associates with the payment token.
- [merchantDomain](applepaypaymenttokencontext/merchantdomain.md)
  The merchant’s top-level domain that the Apple Pay server associates with the payment token.
- [externalIdentifier](applepaypaymenttokencontext/externalidentifier.md)
  An external identifier for the merchant.
### Indicating a payment amount
- [amount](applepaypaymenttokencontext/amount.md)
  The amount to authorize for the payment token context.

## See Also

- [multiTokenContexts](applepaypaymentrequest/multitokencontexts.md)
  An array of payment token contexts that requests multiple payment tokens to support a multimerchant payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymenttokencontext)*