# ApplePayPaymentPassActivationState

**Framework**: Apple Pay on the Web  
**Kind**: enum

Payment pass activation states.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
enum ApplePayPaymentPassActivationState
```

#### Overview

Use one of the following values for the activation state:

- **`activated`**: Active and ready to be used for payment.
- **`requiresActivation`**: Not active but may be activated by the issuer.
- **`activating`**: Not ready for use but activation is in progress.
- **`suspended`**: Not active and can’t be activated.
- **`deactivated`**: Not active because the issuer has disabled the account associated with the device.

## Topics

### Enumeration Cases
- [activated](applepaypaymentpassactivationstate/activated.md)
- [activating](applepaypaymentpassactivationstate/activating.md)
- [deactivated](applepaypaymentpassactivationstate/deactivated.md)
- [requiresActivation](applepaypaymentpassactivationstate/requiresactivation.md)
- [suspended](applepaypaymentpassactivationstate/suspended.md)

## See Also

- [activationState](applepaypaymentpass/activationstate.md)
  The activation state of the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentpassactivationstate)*