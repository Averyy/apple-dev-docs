# INStartVideoCallIntentResponseCode.continueInApp

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Your extension is ready to transfer control to the app so that your app can place the call.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: INStartVideoCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
case continueInApp
```

```c
INStartVideoCallIntentResponseCodeContinueInApp
```

#### Discussion

Upon returning this code, Siri launches your app and passes it the NSUserActivity object you provided at initialization time. (If you didn’t provide a user activity object, Siri creates one for you.) Siri adds an INInteraction object with the intent and your response to the user activity object before delivering it. Your app should use the information in the user activity object to place the call.

## See Also

### Constants
- [INStartVideoCallIntentResponseCode.unspecified](./unspecified.md)
  Your app can’t provide a more specific response.
- [INStartVideoCallIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INStartVideoCallIntentResponseCode.failure](./failure.md)
  You were unable to initiate the call.
- [INStartVideoCallIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to initiate the call.
- [INStartVideoCallIntentResponseCode.failureAppConfigurationRequired](./failureappconfigurationrequired.md)
  The user must perform additional configuration steps before initiating a call is possible.
- [INStartVideoCallIntentResponseCode.failureCallingServiceNotAvailable](./failurecallingservicenotavailable.md)
  Your app’s calling service isn’t currently available.
- [INStartVideoCallIntentResponseCode.failureContactNotSupportedByApp](./failurecontactnotsupportedbyapp.md)
  Your app can’t use the specified contact to place the call.
- [INStartVideoCallIntentResponseCode.failureInvalidNumber](./failureinvalidnumber.md)
  The specified number doesn’t support video calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintentresponsecode/continueinapp)*