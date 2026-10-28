# INStartVideoCallIntentResponseCode.failureAppConfigurationRequired

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must perform additional configuration steps before initiating a call is possible.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: INStartVideoCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
case failureAppConfigurationRequired
```

```c
INStartVideoCallIntentResponseCodeFailureAppConfigurationRequired
```

## Discussion

Use this response code when your app isn’t configured to start a video call. For example, you might return this code if the user hasn’t yet set up a calling account. Don’t use it for general errors or to force the user to launch your app.

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
- [INStartVideoCallIntentResponseCode.failureCallingServiceNotAvailable](./failurecallingservicenotavailable.md)
  Your app’s calling service isn’t currently available.
- [INStartVideoCallIntentResponseCode.failureContactNotSupportedByApp](./failurecontactnotsupportedbyapp.md)
  Your app can’t use the specified contact to place the call.
- [INStartVideoCallIntentResponseCode.failureInvalidNumber](./failureinvalidnumber.md)
  The specified number doesn’t support video calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintentresponsecode/failureappconfigurationrequired)*