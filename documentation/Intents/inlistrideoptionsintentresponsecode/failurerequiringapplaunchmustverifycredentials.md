# INListRideOptionsIntentResponseCode.failureRequiringAppLaunchMustVerifyCredentials

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app and verify their credentials to continue.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureRequiringAppLaunchMustVerifyCredentials
```

```c
INListRideOptionsIntentResponseCodeFailureRequiringAppLaunchMustVerifyCredentials
```

#### Discussion

Use this code when you require the user to login or sign up for your service and the user is currently not logged in or signed up. Specify this code to redirect the user to your app to provide the appropriate credentials. Don’t use this response code for general errors or to force the user to launch your app.

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
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchNoServiceInArea](./failurerequiringapplaunchnoserviceinarea.md)
  You do not provide service in the area requested by the user.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.
- [INListRideOptionsIntentResponseCode.failureRequiringAppLaunchPreviousRideNeedsCompletion](./failurerequiringapplaunchpreviousrideneedscompletion.md)
  You can’t book a new ride because an existing ride is currently in progress.
- [INListRideOptionsIntentResponseCode.failurePreviousRideNeedsFeedback](./failurepreviousrideneedsfeedback.md)
  You can’t book a new ride because an existing ride is currently in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintentresponsecode/failurerequiringapplaunchmustverifycredentials)*