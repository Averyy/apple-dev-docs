# PaymentCredentialStatusResponse

**Framework**: Apple Pay on the Web  
**Kind**: struct

The response for information about the device’s support for Apple Pay and the payment credential status.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary PaymentCredentialStatusResponse {
	PaymentCredentialStatus paymentCredentialStatus;
};
```

#### Overview

The response contains the [`paymentCredentialStatus`](paymentcredentialstatusresponse/paymentcredentialstatus.md) of the device.

## Topics

### Payment credential status
- [paymentCredentialStatus](paymentcredentialstatusresponse/paymentcredentialstatus.md)
  The status of the possible payment credentials that a person has provisioned in Wallet.

## See Also

- [Checking for Apple Pay availability](checking-for-apple-pay-availability.md)
  Use the Apple Pay JS API to check whether Apple Pay is available, to check whether a device has a payment credential provisioned in Wallet, and to determine when to display an Apple Pay button.
- [canMakePayments](applepaysession/canmakepayments.md)
  Indicates whether the device supports Apple Pay.
- [applePayCapabilities](applepaysession/applepaycapabilities.md)
  Indicates whether the device supports Apple Pay and whether the person has an active card in Wallet that qualifies for web payments.
- [canMakePaymentsWithActiveCard](applepaysession/canmakepaymentswithactivecard.md)
  Indicates whether the device supports Apple Pay and whether the user has an active card in Wallet.
- [PaymentCredentialStatus](paymentcredentialstatus.md)
  Information about whether the device supports Apple Pay and the possible payment credentials the person has provisioned in Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/paymentcredentialstatusresponse)*