# INGetRideStatusIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You are ready to handle the intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case ready
```

```c
INGetRideStatusIntentResponseCodeReady
```

## Discussion

During the confirmation phase of an intent, use this code to signal that your Intents extension is ready and able to act on the intent.

## See Also

### Constants
- [INGetRideStatusIntentResponseCode.unspecified](./unspecified.md)
  There is no specified response code.
- [INGetRideStatusIntentResponseCode.inProgress](./inprogress.md)
  You are in the process of handling the intent.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintentresponsecode/ready)*