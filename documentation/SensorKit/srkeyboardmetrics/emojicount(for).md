# emojiCount(for:)

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Provides the number of typed emojis for the specified sentiment in the report.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func emojiCount(for category: SRKeyboardMetrics.SentimentCategory) -> Int
```

```objc
- (NSInteger) emojiCountForSentimentCategory:(SRKeyboardMetricsSentimentCategory) category;
```

## Return Value

The total number of typed emojis for a sentiment.

## Parameters

- `category`: An estimation of the user’s demeanor.

## See Also

### Inferring Sentiment
- [func wordCount(for: SRKeyboardMetrics.SentimentCategory) -> Int](./wordcount%28for%29.md)
  Provides the number of typed words for the specified sentiment in the report.
- [SRKeyboardMetrics.SentimentCategory](./sentimentcategory.md)
  Moods that the framework determines by analyzing the user’s input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/emojicount(for:))*