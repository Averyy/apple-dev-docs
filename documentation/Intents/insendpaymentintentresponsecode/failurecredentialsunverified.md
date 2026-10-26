# INSendPaymentIntentResponseCode.failureCredentialsUnverified

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to deliver the request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureCredentialsUnverified
```

```c
INSendPaymentIntentResponseCodeFailureCredentialsUnverified
```

#### Discussion

Use this response code when you are unable to verify the credentials of the sender or recipient of the payment.

## See Also

### Constants
- [INSendPaymentIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INSendPaymentIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSendPaymentIntentResponseCode.inProgress](./inprogress.md)
  You are in the process of handling the intent.
- [INSendPaymentIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSendPaymentIntentResponseCode.failure](./failure.md)
  You were unable to send the funds.
- [INSendPaymentIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to send the funds.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintentresponsecode/failurecredentialsunverified)*