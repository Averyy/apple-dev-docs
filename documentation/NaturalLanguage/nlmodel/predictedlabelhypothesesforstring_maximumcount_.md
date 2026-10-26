# predictedLabelHypothesesForString:maximumCount:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Predicts multiple possible labels for the given input string.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```objc
- (NSDictionary<NSString *,NSNumber *> *) predictedLabelHypothesesForString:(NSString *) string maximumCount:(NSUInteger) maximumCount;
```

#### Return Value

A dictionary of label hypotheses. Each dictionary entry is a predicted label with its associated probability score. These labels are the top candidates proposed as possible labels for the input string. The dictionary contains up to `maximumCount` entries.

## Parameters

- `string`: The input string for the model to analyze.
- `maximumCount`: The maximum number of label predictions to return for each input string.

## See Also

### Making predictions
- [func predictedLabel(for: String) -> String?](./predictedlabel%28for%29.md)
  Predicts a label for the given input string.
- [func predictedLabels(forTokens: [String]) -> [String]](./predictedlabels%28fortokens%29.md)
  Predicts a label for each string in the given array.
- [- predictedLabelHypothesesForTokens:maximumCount:](./predictedlabelhypothesesfortokens_maximumcount_.md)
  Predicts multiple possible labels for each string in the given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodel/predictedlabelhypothesesforstring:maximumcount:)*