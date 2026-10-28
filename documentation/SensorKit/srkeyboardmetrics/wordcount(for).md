# wordCount(for:)

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Provides the number of typed words for the specified sentiment in the report.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func wordCount(for category: SRKeyboardMetrics.SentimentCategory) -> Int
```

```objc
- (NSInteger) wordCountForSentimentCategory:(SRKeyboardMetricsSentimentCategory) category;
```

## Return Value

The total number of typed words for a sentiment.

## Parameters

- `category`: An estimation of the user’s demeanor.

## See Also

### Inferring Sentiment
- [func emojiCount(for: SRKeyboardMetrics.SentimentCategory) -> Int](./emojicount%28for%29.md)
  Provides the number of typed emojis for the specified sentiment in the report.
- [SRKeyboardMetrics.SentimentCategory](./sentimentcategory.md)
  Moods that the framework determines by analyzing the user’s input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics/wordcount(for:))*