# INGetRideStatusIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to retrieve information about the current ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failure
```

```c
INGetRideStatusIntentResponseCodeFailure
```

## Discussion

Use this code for both transient and unrecoverable errors that prevented you from retrieving the information.

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
- [INGetRideStatusIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to get information about the current ride.
- [INGetRideStatusIntentResponseCode.failureRequiringAppLaunchMustVerifyCredentials](./failurerequiringapplaunchmustverifycredentials.md)
  The user must launch your app and verify their credentials to continue.
- [INGetRideStatusIntentResponseCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintentresponsecode/failure)*