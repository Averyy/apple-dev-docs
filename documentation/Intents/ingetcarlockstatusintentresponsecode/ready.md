# INGetCarLockStatusIntentResponseCode.ready

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
INGetCarLockStatusIntentResponseCodeReady
```

#### Discussion

During the confirmation phase of an intent, use this code to signal that your app is ready and able to act on the intent.

## See Also

### Constants
- [INGetCarLockStatusIntentResponseCode.failure](./failure.md)
  An error code indicating that you were unable to get the car’s lock status.
- [INGetCarLockStatusIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to get the car’s lock status.
- [INGetCarLockStatusIntentResponseCode.inProgress](./inprogress.md)
  A response code indicating that you are getting the car’s lock status but do not yet have the results.
- [INGetCarLockStatusIntentResponseCode.success](./success.md)
  A response code indicating that you have successfully handled the intent.
- [INGetCarLockStatusIntentResponseCode.unspecified](./unspecified.md)
  A response code indicating that the status was not specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarlockstatusintentresponsecode/ready)*