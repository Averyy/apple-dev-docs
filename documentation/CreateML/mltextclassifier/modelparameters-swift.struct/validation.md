# validation

**Framework**: Create ML  
**Kind**: property

The validation dataset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var validation: MLTextClassifier.ModelParameters.ValidationData { get set }
```

#### Discussion

The default value is [`MLTextClassifier.ModelParameters.ValidationData.split(strategy:)`](mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md) with the [`MLSplitStrategy.automatic`](mlsplitstrategy/automatic.md) split strategy``, which automatically generates the validation dataset by partitioning up to 10% of the training dataset.

## See Also

- [var algorithm: MLTextClassifier.ModelAlgorithmType](mltextclassifier/modelparameters-swift.struct/algorithm.md)
  The parameter’s algorithm setting.
- [var language: NLLanguage?](mltextclassifier/modelparameters-swift.struct/language.md)
  The parameter’s language setting.
- [var maxIterations: Int?](mltextclassifier/modelparameters-swift.struct/maxiterations.md)
  The maximum number of training iterations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/validation)*