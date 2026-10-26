# INStartVideoCallIntentResponseCode.failureInvalidNumber

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The specified number doesn’t support video calls.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
case failureInvalidNumber
```

```c
INStartVideoCallIntentResponseCodeFailureInvalidNumber
```

#### Discussion

Use this code when the recipient’s call identifier isn’t valid for audio calls on your service.

## See Also

### Constants
- [INStartVideoCallIntentResponseCode.unspecified](./unspecified.md)
  Your app can’t provide a more specific response.
- [INStartVideoCallIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INStartVideoCallIntentResponseCode.continueInApp](./continueinapp.md)
  Your extension is ready to transfer control to the app so that your app can place the call.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintentresponsecode/failureinvalidnumber)*