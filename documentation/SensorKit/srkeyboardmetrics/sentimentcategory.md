# SRKeyboardMetrics.SentimentCategory

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

Moods that the framework determines by analyzing the user’s input.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum SentimentCategory
```

```c
enum SRKeyboardMetricsSentimentCategory : NSInteger;
```

#### Overview

This class describes possible values for [`wordCount(for:)`](./wordcount%28for%29.md) and [`emojiCount(for:)`](./emojicount%28for%29.md) properties of a keyboard report.

## Topics

### Sentiments
- [SRKeyboardMetrics.SentimentCategory.absolutist](./sentimentcategory/absolutist.md)
  A mood that embodies absolutism.
- [SRKeyboardMetrics.SentimentCategory.anger](./sentimentcategory/anger.md)
  A mood that embodies anger.
- [SRKeyboardMetrics.SentimentCategory.anxiety](./sentimentcategory/anxiety.md)
  A mood that embodies worrying.
- [SRKeyboardMetrics.SentimentCategory.confused](./sentimentcategory/confused.md)
  A mood that embodies confusion.
- [SRKeyboardMetrics.SentimentCategory.death](./sentimentcategory/death.md)
  A mood that expresses death.
- [SRKeyboardMetrics.SentimentCategory.down](./sentimentcategory/down.md)
  A mood that embodies depression.
- [SRKeyboardMetrics.SentimentCategory.health](./sentimentcategory/health.md)
  A general concern for health.
- [SRKeyboardMetrics.SentimentCategory.lowEnergy](./sentimentcategory/lowenergy.md)
  A mood that indicates low energy.
- [SRKeyboardMetrics.SentimentCategory.positive](./sentimentcategory/positive.md)
  A mood that embodies positivity.
- [SRKeyboardMetrics.SentimentCategory.sad](./sentimentcategory/sad.md)
  A mood that embodies sadness.
### Initializers
- [init?(rawValue: Int)](./sentimentcategory/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inferring Sentiment
- [func wordCount(for: SRKeyboardMetrics.SentimentCategory) -> Int](./wordcount%28for%29.md)
  Provides the number of typed words for the specified sentiment in the report.
- [func emojiCount(for: SRKeyboardMetrics.SentimentCategory) -> Int](./emojicount%28for%29.md)
  Provides the number of typed emojis for the specified sentiment in the report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/sentimentcategory)*