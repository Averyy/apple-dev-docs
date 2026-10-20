# predictedLabelHypotheses(forTokens:maximumCount:)

**Framework**: Natural Language  
**Kind**: method

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

```swift
@nonobjc
func predictedLabelHypotheses(forTokens tokens: [String], maximumCount maxCount: Int) -> [[String : Double]]
```

#### Return Value

An array of dictionaries. Each dictionary corresponds to the token at the same index in the input array `tokens`. Within each dictionary, each entry is a predicted label with its associated probability score. These labels are the top candidates proposed as possible labels for the token. Each dictionary contains up to `maxCount` entries.

## Parameters

- `tokens`: An array of input tokens for the model to analyze.
- `maxCount`: The maximum number of label predictions to return for each input string.

## See Also

- [func predictedLabel(for: String) -> String?](nlmodel/predictedlabel(for:).md)
  Predicts a label for the given input string.
- [func predictedLabels(forTokens: [String]) -> [String]](nlmodel/predictedlabels(fortokens:).md)
  Predicts a label for each string in the given array.
- [func predictedLabelHypotheses(for: String, maximumCount: Int) -> [String : Double]](nlmodel/predictedlabelhypotheses(for:maximumcount:).md)
  Predicts multiple possible labels for the given input string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodel/predictedlabelhypotheses(fortokens:maximumcount:))*