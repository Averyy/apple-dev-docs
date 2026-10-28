# INGetCarPowerLevelStatusIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code indicating that your app has requested the power level data, but has not yet received the results.

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
INGetCarPowerLevelStatusIntentResponseCodeInProgress
```

## Discussion

When handling the intent, return this code if your request may take longer than a few seconds to complete.

## See Also

### Constants
- [INGetCarPowerLevelStatusIntentResponseCode.failure](./failure.md)
  An error code indicating that you were unable to get the car’s power level.
- [INGetCarPowerLevelStatusIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to get the car’s current power level.
- [INGetCarPowerLevelStatusIntentResponseCode.ready](./ready.md)
  A response code indicating that you are ready to handle the intent.
- [INGetCarPowerLevelStatusIntentResponseCode.success](./success.md)
  A response code indicating that you successfully handled the intent.
- [INGetCarPowerLevelStatusIntentResponseCode.unspecified](./unspecified.md)
  A response code indicating that the status was not specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponsecode/inprogress)*