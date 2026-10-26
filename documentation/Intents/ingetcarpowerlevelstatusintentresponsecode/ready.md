# INGetCarPowerLevelStatusIntentResponseCode.ready

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
INGetCarPowerLevelStatusIntentResponseCodeReady
```

#### Discussion

During the confirmation phase of an intent, use this code to signal that your app is ready and able to act on the intent.

## See Also

### Constants
- [INGetCarPowerLevelStatusIntentResponseCode.failure](./failure.md)
  An error code indicating that you were unable to get the car’s power level.
- [INGetCarPowerLevelStatusIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to get the car’s current power level.
- [INGetCarPowerLevelStatusIntentResponseCode.inProgress](./inprogress.md)
  A response code indicating that your app has requested the power level data, but has not yet received the results.
- [INGetCarPowerLevelStatusIntentResponseCode.success](./success.md)
  A response code indicating that you successfully handled the intent.
- [INGetCarPowerLevelStatusIntentResponseCode.unspecified](./unspecified.md)
  A response code indicating that the status was not specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponsecode/ready)*