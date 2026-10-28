# INSetCarLockStatusIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code indicating that you are ready to handle the intent.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case ready
```

```c
INSetCarLockStatusIntentResponseCodeReady
```

## Discussion

During the confirmation phase of an intent, use this code to signal that your app is ready and able to act on the intent.

## See Also

### Constants
- [INSetCarLockStatusIntentResponseCode.failure](./failure.md)
  An error code indicating that you were unable to lock or unlock the car.
- [INSetCarLockStatusIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to lock or unlock the car.
- [INSetCarLockStatusIntentResponseCode.inProgress](./inprogress.md)
  A response code indicating that your app has attempted to lock or unlock the car, but does not yet have the results.
- [INSetCarLockStatusIntentResponseCode.success](./success.md)
  A response code indicating that you have successfully handled the intent.
- [INSetCarLockStatusIntentResponseCode.unspecified](./unspecified.md)
  A response code indicating that the status was not specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetcarlockstatusintentresponsecode/ready)*