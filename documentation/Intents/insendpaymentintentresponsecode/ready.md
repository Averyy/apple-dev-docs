# INSendPaymentIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You are ready to handle the intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case ready
```

```c
INSendPaymentIntentResponseCodeReady
```

#### Discussion

During the confirmation phase of an intent, use this code to signal that your Intents extension is ready and able to act on the intent.

## See Also

### Constants
- [INSendPaymentIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INSendPaymentIntentResponseCode.inProgress](./inprogress.md)
  You are in the process of handling the intent.
- [INSendPaymentIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSendPaymentIntentResponseCode.failure](./failure.md)
  You were unable to send the funds.
- [INSendPaymentIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to send the funds.
- [INSendPaymentIntentResponseCode.failureCredentialsUnverified](./failurecredentialsunverified.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failurePaymentsAmountBelowMinimum](./failurepaymentsamountbelowminimum.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failurePaymentsAmountAboveMaximum](./failurepaymentsamountabovemaximum.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failurePaymentsCurrencyUnsupported](./failurepaymentscurrencyunsupported.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failureInsufficientFunds](./failureinsufficientfunds.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failureNoBankAccount](./failurenobankaccount.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failureNotEligible](./failurenoteligible.md)
  The request failed because a user was not eligible to perform the transaction.
- [INSendPaymentIntentResponseCode.failureTermsAndConditionsAcceptanceRequired](./failuretermsandconditionsacceptancerequired.md)
  The request failed because the user must accept the app’s terms and conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintentresponsecode/ready)*