# INActivateCarSignalIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code indicating that you have successfully handled the intent.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case success
```

```c
INActivateCarSignalIntentResponseCodeSuccess
```

## Discussion

Use this code when your app has successfully activated the specified signals on the user’s car.

## See Also

### Constants
- [INActivateCarSignalIntentResponseCode.failure](./failure.md)
  An error code indicating that you were unable to activate the car’s signals.
- [INActivateCarSignalIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to activate the car’s signals.
- [INActivateCarSignalIntentResponseCode.inProgress](./inprogress.md)
  A response code indicating that you are activating the signals but do not yet have the results.
- [INActivateCarSignalIntentResponseCode.ready](./ready.md)
  A response code indicating that you are ready to handle the intent.
- [INActivateCarSignalIntentResponseCode.unspecified](./unspecified.md)
  A response code indicating that the status was not specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintentresponsecode/success)*