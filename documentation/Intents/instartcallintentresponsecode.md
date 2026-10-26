# INStartCallIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the response state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INStartCallIntentResponseCode
```

```c
enum INStartCallIntentResponseCode : NSInteger;
```

## Topics

### Response Code
- [INStartCallIntentResponseCode.unspecified](./instartcallintentresponsecode/unspecified.md)
  A response code that indicates an unknown state.
- [INStartCallIntentResponseCode.ready](./instartcallintentresponsecode/ready.md)
  A response code that indicates app readiness.
- [INStartCallIntentResponseCode.continueInApp](./instartcallintentresponsecode/continueinapp.md)
  A response code that indicates your app extension is ready to transfer control to the app to start the call.
- [INStartCallIntentResponseCode.userConfirmationRequired](./instartcallintentresponsecode/userconfirmationrequired.md)
  A response code that indicates the user must confirm the call information before starting the call.
- [INStartCallIntentResponseCode.failure](./instartcallintentresponsecode/failure.md)
  A response code that indicates you were unable to perform the search.
- [INStartCallIntentResponseCode.failureRequiringAppLaunch](./instartcallintentresponsecode/failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start a call.
- [INStartCallIntentResponseCode.failureCallingServiceNotAvailable](./instartcallintentresponsecode/failurecallingservicenotavailable.md)
  A response code that indicates your app’s calling service isn’t currently available.
- [INStartCallIntentResponseCode.failureContactNotSupportedByApp](./instartcallintentresponsecode/failurecontactnotsupportedbyapp.md)
  A response code that indicates the app doesn’t support the specified contact.
- [INStartCallIntentResponseCode.failureAirplaneModeEnabled](./instartcallintentresponsecode/failureairplanemodeenabled.md)
  A response code that indicates the call can’t start due to the user’s device being in airplane mode.
- [INStartCallIntentResponseCode.failureUnableToHandOff](./instartcallintentresponsecode/failureunabletohandoff.md)
  A response code that indicates the app can’t hand off the call.
- [INStartCallIntentResponseCode.failureAppConfigurationRequired](./instartcallintentresponsecode/failureappconfigurationrequired.md)
  A response code that indicates the user must perform additional configuration steps before creating a call is possible.
- [INStartCallIntentResponseCode.failureCallInProgress](./instartcallintentresponsecode/failurecallinprogress.md)
  A response code that indicates the current call failed.
### Enumeration Cases
- [INStartCallIntentResponseCode.failureRequiringInAppAuthentication](./instartcallintentresponsecode/failurerequiringinappauthentication.md)
- [INStartCallIntentResponseCodeFailureCallRinging](./instartcallintentresponsecode/instartcallintentresponsecodefailurecallringing.md)
### Initializers
- [init?(rawValue: Int)](./instartcallintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INStartCallIntentResponseCode](./instartcallintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintentresponsecode)*