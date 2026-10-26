# INSetCarLockStatusIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code indicating that your app has attempted to lock or unlock the car, but does not yet have the results.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case inProgress
```

```c
INSetCarLockStatusIntentResponseCodeInProgress
```

#### Discussion

When handling the intent, return this code if the action may take longer than a few seconds to complete.

## See Also

### Constants
- [INSetCarLockStatusIntentResponseCode.failure](./failure.md)
  An error code indicating that you were unable to lock or unlock the car.
- [INSetCarLockStatusIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to lock or unlock the car.
- [INSetCarLockStatusIntentResponseCode.ready](./ready.md)
  A response code indicating that you are ready to handle the intent.
- [INSetCarLockStatusIntentResponseCode.success](./success.md)
  A response code indicating that you have successfully handled the intent.
- [INSetCarLockStatusIntentResponseCode.unspecified](./unspecified.md)
  A response code indicating that the status was not specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetcarlockstatusintentresponsecode/inprogress)*