# predictedLabel(for:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Predicts a label for the given input string.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func predictedLabel(for string: String) -> String?
```

```objc
- (NSString *) predictedLabelForString:(NSString *) string;
```

## Return Value

The model’s predicted label for the input string.

## Parameters

- `string`: The input text for the model to analyze.

## See Also

### Making predictions
- [func predictedLabels(forTokens: [String]) -> [String]](./predictedlabels%28fortokens%29.md)
  Predicts a label for each string in the given array.
- [func predictedLabelHypotheses(for: String, maximumCount: Int) -> [String : Double]](./predictedlabelhypotheses%28for,maximumcount%29.md)
  Predicts multiple possible labels for the given input string.
- [func predictedLabelHypotheses(forTokens: [String], maximumCount: Int) -> [[String : Double]]](./predictedlabelhypotheses%28fortokens,maximumcount%29.md)
  Predicts multiple possible labels for each string in the given array.
- [- predictedLabelHypothesesForString:maximumCount:](./predictedlabelhypothesesforstring_maximumcount_.md)
  Predicts multiple possible labels for the given input string.
- [- predictedLabelHypothesesForTokens:maximumCount:](./predictedlabelhypothesesfortokens_maximumcount_.md)
  Predicts multiple possible labels for each string in the given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodel/predictedlabel(for:))*