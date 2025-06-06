# canMakePayments

**Framework**: Apple Pay on the Web  
**Kind**: method

Indicates whether the device supports Apple Pay.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
static boolean canMakePayments();
```

## Mentions

- [Checking for Apple Pay availability](checking-for-apple-pay-availability.md)

#### Return Value

`true` if the device supports making payments with Apple Pay; otherwise, `false`.

#### Discussion

This method only checks to ensure that the device supports processing payments with Apple Pay. It doesn’t verify whether or not the user has any provisioned cards in Wallet.

This method can be called any time.

## See Also

- [Checking for Apple Pay availability](checking-for-apple-pay-availability.md)
  Use the Apple Pay JS API to check whether Apple Pay is available, to check whether a device has a payment credential provisioned in Wallet, and to determine when to display an Apple Pay button.
- [applePayCapabilities](applepaysession/applepaycapabilities.md)
  Indicates whether the device supports Apple Pay and whether the person has an active card in Wallet that qualifies for web payments.
- [canMakePaymentsWithActiveCard](applepaysession/canmakepaymentswithactivecard.md)
  Indicates whether the device supports Apple Pay and whether the user has an active card in Wallet.
- [PaymentCredentialStatus](paymentcredentialstatus.md)
  Information about whether the device supports Apple Pay and the possible payment credentials the person has provisioned in Wallet.
- [PaymentCredentialStatusResponse](paymentcredentialstatusresponse.md)
  The response for information about the device’s support for Apple Pay and the payment credential status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/canmakepayments)*