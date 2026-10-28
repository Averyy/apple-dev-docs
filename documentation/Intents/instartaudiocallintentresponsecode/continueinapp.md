# INStartAudioCallIntentResponseCode.continueInApp

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Your extension is ready to transfer control so your app can place the call.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: INStartAudioCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
case continueInApp
```

```c
INStartAudioCallIntentResponseCodeContinueInApp
```

## Discussion

Upon returning this code, Siri launches your app and passes it the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object you provided at initialization time. (If you didn’t provide a user activity object, Siri creates one for you.) Siri adds an [`INInteraction`](../ininteraction.md) object with the intent and your response to the user activity object before delivering it. Your app should use the information in the user activity object to place the call.

## See Also

### Constants
- [INStartAudioCallIntentResponseCode.unspecified](./unspecified.md)
  Your app can’t provide a specific status.
- [INStartAudioCallIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INStartAudioCallIntentResponseCode.failure](./failure.md)
  You were unable to initiate the call.
- [INStartAudioCallIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to initiate the call.
- [INStartAudioCallIntentResponseCode.failureAppConfigurationRequired](./failureappconfigurationrequired.md)
  The user must perform additional configuration steps before initiating a call is possible.
- [INStartAudioCallIntentResponseCode.failureCallingServiceNotAvailable](./failurecallingservicenotavailable.md)
  Your app’s calling service isn’t currently available.
- [INStartAudioCallIntentResponseCode.failureContactNotSupportedByApp](./failurecontactnotsupportedbyapp.md)
  You can’t use the specified contact to place the call.
- [INStartAudioCallIntentResponseCode.failureNoValidNumber](./failurenovalidnumber.md)
  The specified number doesn’t support audio calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartaudiocallintentresponsecode/continueinapp)*