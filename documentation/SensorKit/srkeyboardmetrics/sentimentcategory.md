# SRKeyboardMetrics.SentimentCategory

**Framework**: SensorKit  
**Kind**: enum

Moods that the framework determines by analyzing the user’s input.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum SentimentCategory
```

#### Overview

This class describes possible values for [`wordCount(for:)`](srkeyboardmetrics/wordcount(for:).md) and [`emojiCount(for:)`](srkeyboardmetrics/emojicount(for:).md) properties of a keyboard report.

## Topics

### Sentiments
- [SRKeyboardMetrics.SentimentCategory.absolutist](srkeyboardmetrics/sentimentcategory/absolutist.md)
  A mood that embodies absolutism.
- [SRKeyboardMetrics.SentimentCategory.anger](srkeyboardmetrics/sentimentcategory/anger.md)
  A mood that embodies anger.
- [SRKeyboardMetrics.SentimentCategory.anxiety](srkeyboardmetrics/sentimentcategory/anxiety.md)
  A mood that embodies worrying.
- [SRKeyboardMetrics.SentimentCategory.confused](srkeyboardmetrics/sentimentcategory/confused.md)
  A mood that embodies confusion.
- [SRKeyboardMetrics.SentimentCategory.death](srkeyboardmetrics/sentimentcategory/death.md)
  A mood that expresses death.
- [SRKeyboardMetrics.SentimentCategory.down](srkeyboardmetrics/sentimentcategory/down.md)
  A mood that embodies depression.
- [SRKeyboardMetrics.SentimentCategory.health](srkeyboardmetrics/sentimentcategory/health.md)
  A general concern for health.
- [SRKeyboardMetrics.SentimentCategory.lowEnergy](srkeyboardmetrics/sentimentcategory/lowenergy.md)
  A mood that indicates low energy.
- [SRKeyboardMetrics.SentimentCategory.positive](srkeyboardmetrics/sentimentcategory/positive.md)
  A mood that embodies positivity.
- [SRKeyboardMetrics.SentimentCategory.sad](srkeyboardmetrics/sentimentcategory/sad.md)
  A mood that embodies sadness.
### Initializers
- [init?(rawValue: Int)](srkeyboardmetrics/sentimentcategory/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func wordCount(for: SRKeyboardMetrics.SentimentCategory) -> Int](srkeyboardmetrics/wordcount(for:).md)
  Provides the number of typed words for the specified sentiment in the report.
- [func emojiCount(for: SRKeyboardMetrics.SentimentCategory) -> Int](srkeyboardmetrics/emojicount(for:).md)
  Provides the number of typed emojis for the specified sentiment in the report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/sentimentcategory)*