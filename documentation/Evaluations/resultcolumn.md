# ResultColumn

**Framework**: Evaluations  
**Kind**: struct

A typed descriptor for a column in an evaluation result DataFrame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ResultColumn<Value>
```

#### Overview

```swift
let column = ResultColumn<ModelSample<String>>(name: "Input")
```

## Topics

### Instance Properties
- [let name: String](resultcolumn/name.md)
  The column name in the DataFrame.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct EvaluationResult](evaluationresult.md)
  The results of running a model evaluation.
- [var inputColumn: ResultColumn<Self.Sample>](evaluation/inputcolumn.md)
  A typed column descriptor for the input samples in the detailed DataFrame.
- [var responseColumn: ResultColumn<Self.Subject>](evaluation/responsecolumn.md)
  A typed column descriptor for the model responses in the detailed DataFrame.
- [var expectedColumn: ResultColumn<Self.Sample.ExpectedValue>](evaluation/expectedcolumn.md)
  A typed column descriptor for the expected values in the detailed DataFrame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/resultcolumn)*