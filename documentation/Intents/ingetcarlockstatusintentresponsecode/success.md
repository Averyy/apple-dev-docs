# INGetCarLockStatusIntentResponseCode.success

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
INGetCarLockStatusIntentResponseCodeSuccess
```

## Discussion

Use this code when your app has successfully received the car’s current lock status.

## See Also

### Constants
- [INGetCarLockStatusIntentResponseCode.failure](./failure.md)
  An error code indicating that you were unable to get the car’s lock status.
- [INGetCarLockStatusIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to get the car’s lock status.
- [INGetCarLockStatusIntentResponseCode.inProgress](./inprogress.md)
  A response code indicating that you are getting the car’s lock status but do not yet have the results.
- [INGetCarLockStatusIntentResponseCode.ready](./ready.md)
  A response code indicating that you are ready to handle the intent.
- [INGetCarLockStatusIntentResponseCode.unspecified](./unspecified.md)
  A response code indicating that the status was not specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarlockstatusintentresponsecode/success)*