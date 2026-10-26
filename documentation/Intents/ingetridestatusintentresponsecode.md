# INGetRideStatusIntentResponseCode

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
enum INGetRideStatusIntentResponseCode
```

```c
enum INGetRideStatusIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INGetRideStatusIntentResponseCode.unspecified](./ingetridestatusintentresponsecode/unspecified.md)
  There is no specified response code.
- [INGetRideStatusIntentResponseCode.ready](./ingetridestatusintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INGetRideStatusIntentResponseCode.inProgress](./ingetridestatusintentresponsecode/inprogress.md)
  You are in the process of handling the intent.
- [INGetRideStatusIntentResponseCode.success](./ingetridestatusintentresponsecode/success.md)
  You successfully handled the intent.
- [INGetRideStatusIntentResponseCode.failure](./ingetridestatusintentresponsecode/failure.md)
  You were unable to retrieve information about the current ride.
- [INGetRideStatusIntentResponseCode.failureRequiringAppLaunch](./ingetridestatusintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to get information about the current ride.
- [INGetRideStatusIntentResponseCode.failureRequiringAppLaunchMustVerifyCredentials](./ingetridestatusintentresponsecode/failurerequiringapplaunchmustverifycredentials.md)
  The user must launch your app and verify their credentials to continue.
- [INGetRideStatusIntentResponseCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./ingetridestatusintentresponsecode/failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.
### Initializers
- [init?(rawValue: Int)](./ingetridestatusintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INGetRideStatusIntentResponseCode](./ingetridestatusintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintentresponsecode)*