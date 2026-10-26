# INGetRideStatusIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You are in the process of handling the intent.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: INGetRideStatusIntentResponseCodeInProgress is deprecated.

## Declaration

```swift
case inProgress
```

```c
INGetRideStatusIntentResponseCodeInProgress
```

#### Discussion

Avoid using this response code when possible unless you are actively retrieving the ride status information but are unable to return that information in a timely manner.

## See Also

### Constants
- [INGetRideStatusIntentResponseCode.unspecified](./unspecified.md)
  There is no specified response code.
- [INGetRideStatusIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INGetRideStatusIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INGetRideStatusIntentResponseCode.failure](./failure.md)
  You were unable to retrieve information about the current ride.
- [INGetRideStatusIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to get information about the current ride.
- [INGetRideStatusIntentResponseCode.failureRequiringAppLaunchMustVerifyCredentials](./failurerequiringapplaunchmustverifycredentials.md)
  The user must launch your app and verify their credentials to continue.
- [INGetRideStatusIntentResponseCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintentresponsecode/inprogress)*