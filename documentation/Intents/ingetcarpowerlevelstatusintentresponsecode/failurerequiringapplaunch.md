# INGetCarPowerLevelStatusIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

An error code indicating that the user must launch your app to get the car’s current power level.

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
INGetCarPowerLevelStatusIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this response code when you cannot handle the request through Siri for a reason not covered by any other response code. For example, you might use this code if the user has not set up the car in your app. Do not use it for general errors or to force the user to launch your app.

## See Also

### Constants
- [INGetCarPowerLevelStatusIntentResponseCode.failure](./failure.md)
  An error code indicating that you were unable to get the car’s power level.
- [INGetCarPowerLevelStatusIntentResponseCode.inProgress](./inprogress.md)
  A response code indicating that your app has requested the power level data, but has not yet received the results.
- [INGetCarPowerLevelStatusIntentResponseCode.ready](./ready.md)
  A response code indicating that you are ready to handle the intent.
- [INGetCarPowerLevelStatusIntentResponseCode.success](./success.md)
  A response code indicating that you successfully handled the intent.
- [INGetCarPowerLevelStatusIntentResponseCode.unspecified](./unspecified.md)
  A response code indicating that the status was not specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponsecode/failurerequiringapplaunch)*