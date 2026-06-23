# responseColumn

**Framework**: Evaluations  
**Kind**: property

A typed column descriptor for the model responses in the detailed DataFrame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var responseColumn: ResultColumn<Self.Subject> { get }
```

## See Also

- [struct EvaluationResult](evaluationresult.md)
  The results of running a model evaluation.
- [struct ResultColumn](resultcolumn.md)
  A typed descriptor for a column in an evaluation result DataFrame.
- [var inputColumn: ResultColumn<Self.Sample>](evaluation/inputcolumn.md)
  A typed column descriptor for the input samples in the detailed DataFrame.
- [var expectedColumn: ResultColumn<Self.Sample.ExpectedValue>](evaluation/expectedcolumn.md)
  A typed column descriptor for the expected values in the detailed DataFrame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/responsecolumn)*