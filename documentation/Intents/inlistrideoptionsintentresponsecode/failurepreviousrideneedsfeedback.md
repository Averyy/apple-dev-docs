# INListRideOptionsIntentResponseCode.failurePreviousRideNeedsFeedback

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You can’t book a new ride because an existing ride is currently in progress.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case failurePreviousRideNeedsFeedback
```

```c
INListRideOptionsIntentResponseCodeFailurePreviousRideNeedsFeedback
```

## Discussion

Use this code when the user must provide feedback for the previous ride before getting a new ride. Specifying this code causes SiriKit to send an [`INSendRideFeedbackIntent`](../insendridefeedbackintent.md) object to your Intents extension. If your Intents extension does not support that intent, SiriKit launches your app as if you had specified the [`INListRideOptionsIntentResponseCode.failureRequiringAppLaunchPreviousRideNeedsCompletion`](./failurerequiringapplaunchpreviousrideneedscompletion.md) response code.

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
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchPreviousRideNeedsCompletion](./failurerequiringapplaunchpreviousrideneedscompletion.md)
  You can’t book a new ride because an existing ride is currently in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintentresponsecode/failurepreviousrideneedsfeedback)*