# INGetCarPowerLevelStatusIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

An error code indicating that you were unable to get the car’s power level.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failure
```

```c
INGetCarPowerLevelStatusIntentResponseCodeFailure
```

## Discussion

Use this code for both transient and unrecoverable errors that would prevent your app from getting the car’s power levels.

## See Also

### Constants
- [INGetCarPowerLevelStatusIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to get the car’s current power level.
- [INGetCarPowerLevelStatusIntentResponseCode.inProgress](./inprogress.md)
  A response code indicating that your app has requested the power level data, but has not yet received the results.
- [INGetCarPowerLevelStatusIntentResponseCode.ready](./ready.md)
  A response code indicating that you are ready to handle the intent.
- [INGetCarPowerLevelStatusIntentResponseCode.success](./success.md)
  A response code indicating that you successfully handled the intent.
- [INGetCarPowerLevelStatusIntentResponseCode.unspecified](./unspecified.md)
  A response code indicating that the status was not specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponsecode/failure)*