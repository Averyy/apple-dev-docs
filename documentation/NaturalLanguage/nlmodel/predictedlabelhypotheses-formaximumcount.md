# predictedLabelHypotheses(for:maximumCount:)

**Framework**: Natural Language  
**Kind**: method

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

```swift
@nonobjc
func predictedLabelHypotheses(for string: String, maximumCount maxCount: Int) -> [String : Double]
```

#### Return Value

A dictionary of label hypotheses. Each dictionary entry is a predicted label with its associated probability score. These labels are the top candidates proposed as possible labels for the input string. The dictionary contains up to `maxCount` entries.

## Parameters

- `string`: The input string for the model to analyze.
- `maxCount`: The maximum number of label predictions to return.

## See Also

- [func predictedLabel(for: String) -> String?](nlmodel/predictedlabel(for:).md)
  Predicts a label for the given input string.
- [func predictedLabels(forTokens: [String]) -> [String]](nlmodel/predictedlabels(fortokens:).md)
  Predicts a label for each string in the given array.
- [func predictedLabelHypotheses(forTokens: [String], maximumCount: Int) -> [[String : Double]]](nlmodel/predictedlabelhypotheses(fortokens:maximumcount:).md)
  Predicts multiple possible labels for each string in the given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodel/predictedlabelhypotheses(for:maximumcount:))*