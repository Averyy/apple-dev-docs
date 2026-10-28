# INGetRideStatusIntentResponseCode.failureRequiringAppLaunchMustVerifyCredentials

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app and verify their credentials to continue.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureRequiringAppLaunchMustVerifyCredentials
```

```c
INGetRideStatusIntentResponseCodeFailureRequiringAppLaunchMustVerifyCredentials
```

## Discussion

Use this code when you require authentication to retrieve information and the user is not currently authenticated. Don’t use this response code for general errors or to force the user to launch your app.

## See Also

### Constants
- [INGetRideStatusIntentResponseCode.unspecified](./unspecified.md)
  There is no specified response code.
- [INGetRideStatusIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INGetRideStatusIntentResponseCode.inProgress](./inprogress.md)
  You are in the process of handling the intent.
- [INGetRideStatusIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INGetRideStatusIntentResponseCode.failure](./failure.md)
  You were unable to retrieve information about the current ride.
- [INGetRideStatusIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to get information about the current ride.
- [INGetRideStatusIntentResponseCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintentresponsecode/failurerequiringapplaunchmustverifycredentials)*