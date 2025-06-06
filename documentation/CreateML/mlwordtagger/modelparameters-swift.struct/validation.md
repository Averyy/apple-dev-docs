# validation

**Framework**: Create ML  
**Kind**: property

The validation dataset.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var validation: MLWordTagger.ModelParameters.ValidationData { get set }
```

#### Discussion

The default value is an [`MLWordTagger.ModelParameters.ValidationData.split(strategy:)`](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md) instance with the [`MLSplitStrategy.automatic`](mlsplitstrategy/automatic.md) split strategy``, which automatically generates the validation dataset by partitioning up to 10% of the training dataset.

## See Also

- [var algorithm: MLWordTagger.ModelAlgorithmType](mlwordtagger/modelparameters-swift.struct/algorithm.md)
  The algorithm type.
- [var language: NLLanguage?](mlwordtagger/modelparameters-swift.struct/language.md)
  The language setting.
- [var maxIterations: Int?](mlwordtagger/modelparameters-swift.struct/maxiterations.md)
  The maximum training iterations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/validation)*