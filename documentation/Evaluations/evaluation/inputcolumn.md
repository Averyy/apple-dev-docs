# inputColumn

**Framework**: Evaluations  
**Kind**: property  
**Role**: Instance Property

A typed column descriptor for the input samples in the detailed DataFrame.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
var inputColumn: ResultColumn<Self.Sample> { get }
```

## Mentions

- [Evaluating language model responses](../evaluating-language-model-responses.md)

## See Also

### Results
- [struct EvaluationResult](../evaluationresult.md)
  The results of running a model evaluation.
- [struct ResultColumn](../resultcolumn.md)
  A typed descriptor for a column in an evaluation result DataFrame.
- [var responseColumn: ResultColumn<Self.Subject>](./responsecolumn.md)
  A typed column descriptor for the model responses in the detailed DataFrame.
- [var expectedColumn: ResultColumn<Self.Sample.ExpectedValue>](./expectedcolumn.md)
  A typed column descriptor for the expected values in the detailed DataFrame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/inputcolumn)*