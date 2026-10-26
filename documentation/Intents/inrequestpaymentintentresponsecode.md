# INRequestPaymentIntentResponseCode

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
enum INRequestPaymentIntentResponseCode
```

```c
enum INRequestPaymentIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INRequestPaymentIntentResponseCode.unspecified](./inrequestpaymentintentresponsecode/unspecified.md)
  The response didn’t specify a response code.
- [INRequestPaymentIntentResponseCode.ready](./inrequestpaymentintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INRequestPaymentIntentResponseCode.inProgress](./inrequestpaymentintentresponsecode/inprogress.md)
  You are in the process of handling the intent.
- [INRequestPaymentIntentResponseCode.success](./inrequestpaymentintentresponsecode/success.md)
  You successfully handled the intent.
- [INRequestPaymentIntentResponseCode.failure](./inrequestpaymentintentresponsecode/failure.md)
  You were unable to deliver the payment request.
- [INRequestPaymentIntentResponseCode.failureRequiringAppLaunch](./inrequestpaymentintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to make the payment request.
- [INRequestPaymentIntentResponseCode.failureCredentialsUnverified](./inrequestpaymentintentresponsecode/failurecredentialsunverified.md)
  The request failed because you couldn’t verify one of the user’s credentials.
- [INRequestPaymentIntentResponseCode.failurePaymentsAmountBelowMinimum](./inrequestpaymentintentresponsecode/failurepaymentsamountbelowminimum.md)
  The request failed because the specified amount was below the required minimum established by your app.
- [INRequestPaymentIntentResponseCode.failurePaymentsAmountAboveMaximum](./inrequestpaymentintentresponsecode/failurepaymentsamountabovemaximum.md)
  The request failed because the specified amount was above the allowed maximum established by your app.
- [INRequestPaymentIntentResponseCode.failurePaymentsCurrencyUnsupported](./inrequestpaymentintentresponsecode/failurepaymentscurrencyunsupported.md)
  The request failed because your app does not support the specified currency.
- [INRequestPaymentIntentResponseCode.failureNoBankAccount](./inrequestpaymentintentresponsecode/failurenobankaccount.md)
  The request failed because you couldn’t determine a user’s bank account information.
- [INRequestPaymentIntentResponseCode.failureNotEligible](./inrequestpaymentintentresponsecode/failurenoteligible.md)
  The request failed because a user was not eligible to perform the transaction.
- [INRequestPaymentIntentResponseCode.failureTermsAndConditionsAcceptanceRequired](./inrequestpaymentintentresponsecode/failuretermsandconditionsacceptancerequired.md)
  The request failed because the user must accept the app’s terms and conditions.
### Initializers
- [init?(rawValue: Int)](./inrequestpaymentintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INRequestPaymentIntentResponseCode](./inrequestpaymentintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintentresponsecode)*