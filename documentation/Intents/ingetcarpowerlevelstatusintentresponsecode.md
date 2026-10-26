# INGetCarPowerLevelStatusIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the status of the response.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INGetCarPowerLevelStatusIntentResponseCode
```

```c
enum INGetCarPowerLevelStatusIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INGetCarPowerLevelStatusIntentResponseCode.failure](./ingetcarpowerlevelstatusintentresponsecode/failure.md)
  An error code indicating that you were unable to get the car’s power level.
- [INGetCarPowerLevelStatusIntentResponseCode.failureRequiringAppLaunch](./ingetcarpowerlevelstatusintentresponsecode/failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to get the car’s current power level.
- [INGetCarPowerLevelStatusIntentResponseCode.inProgress](./ingetcarpowerlevelstatusintentresponsecode/inprogress.md)
  A response code indicating that your app has requested the power level data, but has not yet received the results.
- [INGetCarPowerLevelStatusIntentResponseCode.ready](./ingetcarpowerlevelstatusintentresponsecode/ready.md)
  A response code indicating that you are ready to handle the intent.
- [INGetCarPowerLevelStatusIntentResponseCode.success](./ingetcarpowerlevelstatusintentresponsecode/success.md)
  A response code indicating that you successfully handled the intent.
- [INGetCarPowerLevelStatusIntentResponseCode.unspecified](./ingetcarpowerlevelstatusintentresponsecode/unspecified.md)
  A response code indicating that the status was not specified.
### Initializers
- [init?(rawValue: Int)](./ingetcarpowerlevelstatusintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INGetCarPowerLevelStatusIntentResponseCode](./ingetcarpowerlevelstatusintentresponse/code.md)
  The code that indicates success or failure when confirming or handling an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponsecode)*