# Checking for Apple Pay availability

**Framework**: Applepayontheweb

Use the Apple Pay JS API to check whether Apple Pay is available, to check whether a device has a payment credential provisioned in Wallet, and to determine when to display an Apple Pay button.

#### Overview

Before displaying an Apple Pay button or creating an Apple Pay session, ensure that the Apple Pay JS API is available and enabled on the current device. To check whether the Apple Pay JS API is available in the browser, verify that the `window`.`ApplePaySession` class exists:

```javascript
if (window.ApplePaySession) {
   // The Apple Pay JS API is available.
}
```

Next, check whether payments are possible. Call either the [`canMakePayments`](applepaysession/canmakepayments.md) or [`applePayCapabilities`](applepaysession/applepaycapabilities.md) methods, as follows:

##### Verify Whether the Device Supports Apple Pay

According to the [`Apple Pay on the Web Acceptable Use Guidelines`](https://developer.apple.comhttps://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/), if you invoke the [`applePayCapabilities`](applepaysession/applepaycapabilities.md) API and determine that a person has an active card provisioned into Wallet, then Apple Pay should be the primary, but not necessarily sole payment option on any webpage that accepts payments, like the checkout page or product detail page. In all other situations, use [`canMakePayments`](applepaysession/canmakepayments.md) instead.

The [`applePayCapabilities`](applepaysession/applepaycapabilities.md) method asynchronously contacts Apple Pay servers as part of the verification process and returns the [`paymentCredentialStatus`](paymentcredentialstatusresponse/paymentcredentialstatus.md) of the device. This verifies on Safari and third-party browsers that the device is capable of making Apple Pay payments. It also verifies on Safari browsers that the device has at least one payment credential provisioned in Wallet. Depending on the response, you can determine if the device supports Apple Pay and whether to display an Apple Pay button.

The following are possible return values:

The following code shows how to check that a payment method is available before displaying an Apple Pay button:

```javascript
// Check if the Apple Pay JS API is available.
  if (window.ApplePaySession) {
    var merchantIdentifier = 'YOUR MERCHANT IDENTIFIER';
    var promise = ApplePaySession.applePayCapabilities(merchantIdentifier);
    promise.then(function(capabilities) {
      // Check if the person has an active payment credential provisioned in Wallet.
      switch (capabilities.paymentCredentialStatus) {
        case "paymentCredentialsAvailable":
          // Display an Apple Pay button and offer Apple Pay as the primary payment option. 
        case "paymentCredentialStatusUnknown":
          // Display an Apple Pay button and offer Apple Pay as a payment option.
        case "paymentCredentialsUnavailable":
          // Consider displaying an Apple Pay button.
        case "applePayUnsupported":
          // Don't show an Apple Pay button or offer Apple Pay.
      }
    })
  }
```

##### Verify Apple Pay Availability in China

To provide Apple Pay on the web for customers in China, you must first verify compatibility by checking the browser’s `userAgent` string. This string provides information about the customer’s device and operating system.

For the Chinese market, you need to check the user agent string to confirm that:

- The person’s device is an `“iPhone`” or an `“iPad`”.
- The device is running iOS 11.2 or later.

For example, the following shows a user agent string received from Safari on an iPhone running iOS 11.2:

```other
Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko)CriOS/64.0.3282.112 Mobile/15C202 Safari/604.1
```

After verifying the person’s device type and iOS version, call [`canMakePayments`](applepaysession/canmakepayments.md) or [`applePayCapabilities`](applepaysession/applepaycapabilities.md) as shown earlier, and display the Apple Pay button if the call returns `paymentCredentialsAvailable`.

> **Note**:  Don’t display the Apple Pay button if the device is a Mac, if the iOS version is earlier than 11.2, or if the call to [`canMakePayments`](applepaysession/canmakepayments.md) returns `false`.

## See Also

- [canMakePayments](applepaysession/canmakepayments.md)
  Indicates whether the device supports Apple Pay.
- [applePayCapabilities](applepaysession/applepaycapabilities.md)
  Indicates whether the device supports Apple Pay and whether the person has an active card in Wallet that qualifies for web payments.
- [canMakePaymentsWithActiveCard](applepaysession/canmakepaymentswithactivecard.md)
  Indicates whether the device supports Apple Pay and whether the user has an active card in Wallet.
- [PaymentCredentialStatus](paymentcredentialstatus.md)
  Information about whether the device supports Apple Pay and the possible payment credentials the person has provisioned in Wallet.
- [PaymentCredentialStatusResponse](paymentcredentialstatusresponse.md)
  The response for information about the device’s support for Apple Pay and the payment credential status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ApplePayontheWeb/checking-for-apple-pay-availability)*