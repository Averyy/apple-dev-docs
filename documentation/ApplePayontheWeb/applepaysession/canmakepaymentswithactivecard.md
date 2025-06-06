# canMakePaymentsWithActiveCard

**Framework**: Apple Pay on the Web  
**Kind**: method

Indicates whether the device supports Apple Pay and whether the user has an active card in Wallet.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
static Promise <boolean> canMakePaymentsWithActiveCard(
	DOMString merchantIdentifier
);
```

#### Return Value

`true` if the device supports Apple Pay and there is at least one active card in Wallet that is qualified for payments on the web; otherwise, `false`.

#### Discussion

This method asynchronously contacts the Apple Pay servers as part of the verification process.

Per the [`Apple Pay on the Web Acceptable Use Guidelines`](https://developer.apple.comhttps://developer.apple.com/go/?id=apple-pay-guidelines), if you invoke the [`canMakePaymentsWithActiveCard`](applepaysession/canmakepaymentswithactivecard.md) API and determine that a user has an active card provisioned into Wallet, then Apple Pay must automatically be set as the default or sole payment option on any webpage where payments are accepted, such as the checkout page or product detail page. In all other situations, use [`canMakePayments`](applepaysession/canmakepayments.md) instead.

Note that some cards, such as transit cards, are only enabled for POS payments and therefore won’t qualify for payments on the web.

The following code is an example of calling this method before displaying an Apple Pay button.

Determining whether to display an Apple Pay button

```javascript
if (window.ApplePaySession) {
   var merchantIdentifier = 'example.com.store';
   var promise = ApplePaySession.canMakePaymentsWithActiveCard(merchantIdentifier);
   promise.then(function (canMakePayments) {
      if (canMakePayments)
         // Display Apple Pay Buttons here…
}); }
```

## Parameters

- `merchantIdentifier`: The merchant ID created when the merchant enrolled in Apple Pay.

## See Also

- [Checking for Apple Pay availability](checking-for-apple-pay-availability.md)
  Use the Apple Pay JS API to check whether Apple Pay is available, to check whether a device has a payment credential provisioned in Wallet, and to determine when to display an Apple Pay button.
- [canMakePayments](applepaysession/canmakepayments.md)
  Indicates whether the device supports Apple Pay.
- [applePayCapabilities](applepaysession/applepaycapabilities.md)
  Indicates whether the device supports Apple Pay and whether the person has an active card in Wallet that qualifies for web payments.
- [PaymentCredentialStatus](paymentcredentialstatus.md)
  Information about whether the device supports Apple Pay and the possible payment credentials the person has provisioned in Wallet.
- [PaymentCredentialStatusResponse](paymentcredentialstatusresponse.md)
  The response for information about the device’s support for Apple Pay and the payment credential status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/canmakepaymentswithactivecard)*