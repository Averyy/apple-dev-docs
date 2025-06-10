# completeMerchantValidation

**Framework**: Apple Pay on the Web  
**Kind**: method

Completes the validation for a merchant session.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
undefined completeMerchantValidation(
	any merchantSession
);
```

## Mentions

- [Requesting an Apple Pay payment session](requesting-an-apple-pay-payment-session.md)
- [Providing Merchant Validation](providing-merchant-validation.md)

#### Discussion

Your server receives the merchant session object when it calls the `Payment Session` endpoint as described in [`Providing Merchant Validation`](providing-merchant-validation.md).

You must pass the valid merchant session object to the [`completeMerchantValidation`](applepaysession/completemerchantvalidation.md) method to enable the user to authorize a transaction.

The guidelines for working with a merchant session are:

- Request a new merchant session object for each transaction. You can only use a merchant session object a single time.
- The merchant session object expires five minutes after it is created.
- Never request the merchant session from the client. The request must be sent from your server.

## Parameters

- `merchantSession`: An opaque message session object, received from the Apple Pay server.

## See Also

- [begin](applepaysession/begin.md)
  Begins the merchant validation process.
- [onvalidatemerchant](applepaysession/onvalidatemerchant.md)
  An event handler the system calls when it displays the payment sheet.
- [ApplePayValidateMerchantEvent](applepayvalidatemerchantevent.md)
  An event object that contains the validation URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/completemerchantvalidation)*