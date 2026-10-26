# INListRideOptionsIntentResponseCode

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
enum INListRideOptionsIntentResponseCode
```

```c
enum INListRideOptionsIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INListRideOptionsIntentResponseCode.unspecified](./inlistrideoptionsintentresponsecode/unspecified.md)
  No response didn’t specify a response code.
- [INListRideOptionsIntentResponseCode.ready](./inlistrideoptionsintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INListRideOptionsIntentResponseCode.inProgress](./inlistrideoptionsintentresponsecode/inprogress.md)
  You failed to handle the intent in a timely manner.
- [INListRideOptionsIntentResponseCode.success](./inlistrideoptionsintentresponsecode/success.md)
  You successfully handled the intent.
- [INListRideOptionsIntentResponseCode.failure](./inlistrideoptionsintentresponsecode/failure.md)
  You were unable to retrieve the list of ride options.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunch](./inlistrideoptionsintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to get information about the ride options.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchMustVerifyCredentials](./inlistrideoptionsintentresponsecode/failurerequiringapplaunchmustverifycredentials.md)
  The user must launch your app and verify their credentials to continue.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchNoServiceInArea](./inlistrideoptionsintentresponsecode/failurerequiringapplaunchnoserviceinarea.md)
  You do not provide service in the area requested by the user.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./inlistrideoptionsintentresponsecode/failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchPreviousRideNeedsCompletion](./inlistrideoptionsintentresponsecode/failurerequiringapplaunchpreviousrideneedscompletion.md)
  You can’t book a new ride because an existing ride is currently in progress.
- [INListRideOptionsIntentResponseCode.failurePreviousRideNeedsFeedback](./inlistrideoptionsintentresponsecode/failurepreviousrideneedsfeedback.md)
  You can’t book a new ride because an existing ride is currently in progress.
### Initializers
- [init?(rawValue: Int)](./inlistrideoptionsintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintentresponsecode)*