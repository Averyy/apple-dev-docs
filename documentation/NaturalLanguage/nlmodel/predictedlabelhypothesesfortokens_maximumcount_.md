# predictedLabelHypothesesForTokens:maximumCount:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Predicts multiple possible labels for each string in the given array.

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
- (NSArray<NSDictionary<NSString *,NSNumber *> *> *) predictedLabelHypothesesForTokens:(NSArray<NSString *> *) tokens maximumCount:(NSUInteger) maximumCount;
```

#### Return Value

An array of dictionaries. Each dictionary corresponds to the token at the same index in the input array `tokens`. Within each dictionary, each entry is a predicted label with its associated probability score. These labels are the top candidates proposed as possible labels for the token. Each dictionary contains up to `maximumCount` entries.

## Parameters

- `tokens`: An array of input tokens for the model to analyze.
- `maximumCount`: The maximum number of label predictions to return for each input string.

## See Also

### Making predictions
- [func predictedLabel(for: String) -> String?](./predictedlabel%28for%29.md)
  Predicts a label for the given input string.
- [func predictedLabels(forTokens: [String]) -> [String]](./predictedlabels%28fortokens%29.md)
  Predicts a label for each string in the given array.
- [- predictedLabelHypothesesForString:maximumCount:](./predictedlabelhypothesesforstring_maximumcount_.md)
  Predicts multiple possible labels for the given input string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodel/predictedlabelhypothesesfortokens:maximumcount:)*