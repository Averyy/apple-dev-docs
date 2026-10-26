# INListRideOptionsIntentResponseCode.ready

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
INListRideOptionsIntentResponseCodeReady
```

#### Discussion

During the confirmation phase of an intent, use this code to signal that your Intents extension is ready and able to act on the intent. Consider specifying this constant during handling of the intent a failure on your part and it results in an error.

## See Also

### Constants
- [INListRideOptionsIntentResponseCode.unspecified](./unspecified.md)
  No response didn’t specify a response code.
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
- [INListRideOptionsIntentResponseCode.failurePreviousRideNeedsFeedback](./failurepreviousrideneedsfeedback.md)
  You can’t book a new ride because an existing ride is currently in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintentresponsecode/ready)*