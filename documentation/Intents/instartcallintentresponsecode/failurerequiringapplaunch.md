# INStartCallIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates the user must launch your app to start a call.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INStartCallIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

Use this response code when you can’t handle the request through Siri for a reason not covered by any other response code. For example, you might use this code if the user hasn’t set up an account with your app. Don’t use it for general errors or to force the user to launch your app.

## See Also

### Response Code
- [INStartCallIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates an unknown state.
- [INStartCallIntentResponseCode.ready](./ready.md)
  A response code that indicates app readiness.
- [INStartCallIntentResponseCode.continueInApp](./continueinapp.md)
  A response code that indicates your app extension is ready to transfer control to the app to start the call.
- [INStartCallIntentResponseCode.userConfirmationRequired](./userconfirmationrequired.md)
  A response code that indicates the user must confirm the call information before starting the call.
- [INStartCallIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to perform the search.
- [INStartCallIntentResponseCode.failureCallingServiceNotAvailable](./failurecallingservicenotavailable.md)
  A response code that indicates your app’s calling service isn’t currently available.
- [INStartCallIntentResponseCode.failureContactNotSupportedByApp](./failurecontactnotsupportedbyapp.md)
  A response code that indicates the app doesn’t support the specified contact.
- [INStartCallIntentResponseCode.failureAirplaneModeEnabled](./failureairplanemodeenabled.md)
  A response code that indicates the call can’t start due to the user’s device being in airplane mode.
- [INStartCallIntentResponseCode.failureUnableToHandOff](./failureunabletohandoff.md)
  A response code that indicates the app can’t hand off the call.
- [INStartCallIntentResponseCode.failureAppConfigurationRequired](./failureappconfigurationrequired.md)
  A response code that indicates the user must perform additional configuration steps before creating a call is possible.
- [INStartCallIntentResponseCode.failureCallInProgress](./failurecallinprogress.md)
  A response code that indicates the current call failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintentresponsecode/failurerequiringapplaunch)*