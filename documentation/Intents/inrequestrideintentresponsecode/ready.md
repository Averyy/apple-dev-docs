# INRequestRideIntentResponseCode.ready

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
INRequestRideIntentResponseCodeReady
```

#### Discussion

During the confirmation phase of an intent, use this code to signal that your Intents extension is ready and able to act on the intent.

## See Also

### Constants
- [INRequestRideIntentResponseCode.unspecified](./unspecified.md)
  There is no specified response code.
- [INRequestRideIntentResponseCode.inProgress](./inprogress.md)
  You are in the process of handling the intent.
- [INRequestRideIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INRequestRideIntentResponseCode.failure](./failure.md)
  You were unable to book the ride.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to book the ride.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunchMustVerifyCredentials](./failurerequiringapplaunchmustverifycredentials.md)
  The user must launch your app and verify their credentials to continue.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunchNoServiceInArea](./failurerequiringapplaunchnoserviceinarea.md)
  You do not provide rides in the area requested by the user.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunchPreviousRideNeedsCompletion](./failurerequiringapplaunchpreviousrideneedscompletion.md)
  An existing ride is currently in progress and the app can’t book a new ride.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunchRideScheduledTooFar](./failurerequiringapplaunchridescheduledtoofar.md)
  The scheduled ride is out of the ride area and requires the user to open the app to fix the problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintentresponsecode/ready)*