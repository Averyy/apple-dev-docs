# INRequestRideIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INRequestRideIntentResponseCode
```

```c
enum INRequestRideIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INRequestRideIntentResponseCode.unspecified](./inrequestrideintentresponsecode/unspecified.md)
  There is no specified response code.
- [INRequestRideIntentResponseCode.ready](./inrequestrideintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INRequestRideIntentResponseCode.inProgress](./inrequestrideintentresponsecode/inprogress.md)
  You are in the process of handling the intent.
- [INRequestRideIntentResponseCode.success](./inrequestrideintentresponsecode/success.md)
  You successfully handled the intent.
- [INRequestRideIntentResponseCode.failure](./inrequestrideintentresponsecode/failure.md)
  You were unable to book the ride.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunch](./inrequestrideintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to book the ride.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunchMustVerifyCredentials](./inrequestrideintentresponsecode/failurerequiringapplaunchmustverifycredentials.md)
  The user must launch your app and verify their credentials to continue.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunchNoServiceInArea](./inrequestrideintentresponsecode/failurerequiringapplaunchnoserviceinarea.md)
  You do not provide rides in the area requested by the user.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./inrequestrideintentresponsecode/failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunchPreviousRideNeedsCompletion](./inrequestrideintentresponsecode/failurerequiringapplaunchpreviousrideneedscompletion.md)
  An existing ride is currently in progress and the app can’t book a new ride.
- [INRequestRideIntentResponseCode.failureRequiringAppLaunchRideScheduledTooFar](./inrequestrideintentresponsecode/failurerequiringapplaunchridescheduledtoofar.md)
  The scheduled ride is out of the ride area and requires the user to open the app to fix the problem.
### Initializers
- [init?(rawValue: Int)](./inrequestrideintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INRequestRideIntentResponseCode](./inrequestrideintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintentresponsecode)*