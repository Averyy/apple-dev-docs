# INSendPaymentIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INSendPaymentIntentResponseCode
```

```c
enum INSendPaymentIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INSendPaymentIntentResponseCode.unspecified](./insendpaymentintentresponsecode/unspecified.md)
  The response didn’t specify a response code.
- [INSendPaymentIntentResponseCode.ready](./insendpaymentintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INSendPaymentIntentResponseCode.inProgress](./insendpaymentintentresponsecode/inprogress.md)
  You are in the process of handling the intent.
- [INSendPaymentIntentResponseCode.success](./insendpaymentintentresponsecode/success.md)
  You successfully handled the intent.
- [INSendPaymentIntentResponseCode.failure](./insendpaymentintentresponsecode/failure.md)
  You were unable to send the funds.
- [INSendPaymentIntentResponseCode.failureRequiringAppLaunch](./insendpaymentintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to send the funds.
- [INSendPaymentIntentResponseCode.failureCredentialsUnverified](./insendpaymentintentresponsecode/failurecredentialsunverified.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failurePaymentsAmountBelowMinimum](./insendpaymentintentresponsecode/failurepaymentsamountbelowminimum.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failurePaymentsAmountAboveMaximum](./insendpaymentintentresponsecode/failurepaymentsamountabovemaximum.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failurePaymentsCurrencyUnsupported](./insendpaymentintentresponsecode/failurepaymentscurrencyunsupported.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failureInsufficientFunds](./insendpaymentintentresponsecode/failureinsufficientfunds.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failureNoBankAccount](./insendpaymentintentresponsecode/failurenobankaccount.md)
  You were unable to deliver the request.
- [INSendPaymentIntentResponseCode.failureNotEligible](./insendpaymentintentresponsecode/failurenoteligible.md)
  The request failed because a user was not eligible to perform the transaction.
- [INSendPaymentIntentResponseCode.failureTermsAndConditionsAcceptanceRequired](./insendpaymentintentresponsecode/failuretermsandconditionsacceptancerequired.md)
  The request failed because the user must accept the app’s terms and conditions.
### Initializers
- [init?(rawValue: Int)](./insendpaymentintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INSendPaymentIntentResponseCode](./insendpaymentintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintentresponsecode)*