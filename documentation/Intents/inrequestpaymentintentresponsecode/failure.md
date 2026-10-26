# INRequestPaymentIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to deliver the payment request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failure
```

```c
INRequestPaymentIntentResponseCodeFailure
```

#### Discussion

Use this code for both transient and unrecoverable errors that prevented you from delivering the request.

## See Also

### Constants
- [INRequestPaymentIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INRequestPaymentIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INRequestPaymentIntentResponseCode.inProgress](./inprogress.md)
  You are in the process of handling the intent.
- [INRequestPaymentIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INRequestPaymentIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to make the payment request.
- [INRequestPaymentIntentResponseCode.failureCredentialsUnverified](./failurecredentialsunverified.md)
  The request failed because you couldn’t verify one of the user’s credentials.
- [INRequestPaymentIntentResponseCode.failurePaymentsAmountBelowMinimum](./failurepaymentsamountbelowminimum.md)
  The request failed because the specified amount was below the required minimum established by your app.
- [INRequestPaymentIntentResponseCode.failurePaymentsAmountAboveMaximum](./failurepaymentsamountabovemaximum.md)
  The request failed because the specified amount was above the allowed maximum established by your app.
- [INRequestPaymentIntentResponseCode.failurePaymentsCurrencyUnsupported](./failurepaymentscurrencyunsupported.md)
  The request failed because your app does not support the specified currency.
- [INRequestPaymentIntentResponseCode.failureNoBankAccount](./failurenobankaccount.md)
  The request failed because you couldn’t determine a user’s bank account information.
- [INRequestPaymentIntentResponseCode.failureNotEligible](./failurenoteligible.md)
  The request failed because a user was not eligible to perform the transaction.
- [INRequestPaymentIntentResponseCode.failureTermsAndConditionsAcceptanceRequired](./failuretermsandconditionsacceptancerequired.md)
  The request failed because the user must accept the app’s terms and conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintentresponsecode/failure)*