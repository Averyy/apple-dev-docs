# INListRideOptionsIntentResponseCode.failureRequiringAppLaunchNoServiceInArea

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You do not provide service in the area requested by the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureRequiringAppLaunchNoServiceInArea
```

```c
INListRideOptionsIntentResponseCodeFailureRequiringAppLaunchNoServiceInArea
```

#### Discussion

Use this code when you definitively do not provide service in the requested area. Specify this code to redirect the user to your app. For temporary service disruptions, use the [`INListRideOptionsIntentResponseCode.failureRequiringAppLaunchServiceTemporarilyUnavailable`](./failurerequiringapplaunchservicetemporarilyunavailable.md) code instead. Don’t use this response code for general errors or to force the user to launch your app.

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
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchPreviousRideNeedsCompletion](./failurerequiringapplaunchpreviousrideneedscompletion.md)
  You can’t book a new ride because an existing ride is currently in progress.
- [INListRideOptionsIntentResponseCode.failurePreviousRideNeedsFeedback](./failurepreviousrideneedsfeedback.md)
  You can’t book a new ride because an existing ride is currently in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintentresponsecode/failurerequiringapplaunchnoserviceinarea)*