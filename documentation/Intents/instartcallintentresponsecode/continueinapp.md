# INStartCallIntentResponseCode.continueInApp

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates your app extension is ready to transfer control to the app to start the call.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case continueInApp
```

```c
INStartCallIntentResponseCodeContinueInApp
```

#### Discussion

Returning this code during the confirm phase causes Siri to display an error button labeled “Continue in `<appName>`”.

Upon returning this code during the handle phase, Siri launches your app and passes it the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object you provided at initialization. (If you didn’t provide a user activity object, Siri creates one for you). Siri adds an [`INInteraction`](../ininteraction.md) object with the intent and your response to the user activity object before delivering it. Your app should use the information in the user activity object to start the call.

Return this code after successfully handling the start call intent instead of using [`INStartCallIntentResponseCode.ready`](./ready.md).

## See Also

### Response Code
- [INStartCallIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates an unknown state.
- [INStartCallIntentResponseCode.ready](./ready.md)
  A response code that indicates app readiness.
- [INStartCallIntentResponseCode.userConfirmationRequired](./userconfirmationrequired.md)
  A response code that indicates the user must confirm the call information before starting the call.
- [INStartCallIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to perform the search.
- [INStartCallIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start a call.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintentresponsecode/continueinapp)*