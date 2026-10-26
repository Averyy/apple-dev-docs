# INUpcomingMediaPredictionMode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Prediction modes for upcoming media intent shortcuts.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum INUpcomingMediaPredictionMode
```

```c
enum INUpcomingMediaPredictionMode : NSInteger;
```

## Topics

### Prediction Modes
- [INUpcomingMediaPredictionMode.default](./inupcomingmediapredictionmode/default.md)
  The mode that predicts donated and suggested media intent shortcuts associated with your app.
- [INUpcomingMediaPredictionMode.onlyPredictSuggestedIntents](./inupcomingmediapredictionmode/onlypredictsuggestedintents.md)
  The mode that predicts suggested media intent shortcuts associated with your app.
### Initializers
- [init?(rawValue: Int)](./inupcomingmediapredictionmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Setting Prediction Modes
- [func setPredictionMode(INUpcomingMediaPredictionMode, for: INMediaItemType)](./inupcomingmediamanager/setpredictionmode%28_,for%29.md)
  Suggests how Siri should predict media intent shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupcomingmediapredictionmode)*