# INListRideOptionsIntentResponseCode.failureRequiringAppLaunchPreviousRideNeedsCompletion

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You can’t book a new ride because an existing ride is currently in progress.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureRequiringAppLaunchPreviousRideNeedsCompletion
```

```c
INListRideOptionsIntentResponseCodeFailureRequiringAppLaunchPreviousRideNeedsCompletion
```

#### Discussion

Use this code when the user must provide feedback for the previous ride before getting a new ride. Specify this code to redirect the user to your app so that the user can complete or cancel the previous ride. For example, you might use this code if the user still needs to pay for the previous ride.

If there is a previous ride that is not yet complete, but you still want to allow the user to book another ride, return [`INListRideOptionsIntentResponseCode.success`](./success.md).

## See Also

### Constants
- [INListRideOptionsIntentResponseCode.unspecified](./unspecified.md)
  No response didn’t specify a response code.
- [INListRideOptionsIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INListRideOptionsIntentResponseCode.inProgress](./inprogress.md)
  You failed to handle the intent in a timely manner.
- [INListRideOptionsIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INListRideOptionsIntentResponseCode.failure](./failure.md)
  You were unable to retrieve the list of ride options.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to get information about the ride options.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchMustVerifyCredentials](./failurerequiringapplaunchmustverifycredentials.md)
  The user must launch your app and verify their credentials to continue.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchNoServiceInArea](./failurerequiringapplaunchnoserviceinarea.md)
  You do not provide service in the area requested by the user.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.
- [INListRideOptionsIntentResponseCode.failurePreviousRideNeedsFeedback](./failurepreviousrideneedsfeedback.md)
  You can’t book a new ride because an existing ride is currently in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintentresponsecode/failurerequiringapplaunchpreviousrideneedscompletion)*