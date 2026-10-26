# INActivateCarSignalIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

An error code indicating that the user must launch your app to activate the car’s signals.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INActivateCarSignalIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this response code when you cannot handle the request through Siri for a reason not covered by any other response code. For example, you might use this code if the user has not set up the car in your app. Do not use it for general errors or to force the user to launch your app.

## See Also

### Constants
- [INActivateCarSignalIntentResponseCode.failure](./failure.md)
  An error code indicating that you were unable to activate the car’s signals.
- [INActivateCarSignalIntentResponseCode.inProgress](./inprogress.md)
  A response code indicating that you are activating the signals but do not yet have the results.
- [INActivateCarSignalIntentResponseCode.ready](./ready.md)
  A response code indicating that you are ready to handle the intent.
- [INActivateCarSignalIntentResponseCode.success](./success.md)
  A response code indicating that you have successfully handled the intent.
- [INActivateCarSignalIntentResponseCode.unspecified](./unspecified.md)
  A response code indicating that the status was not specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintentresponsecode/failurerequiringapplaunch)*