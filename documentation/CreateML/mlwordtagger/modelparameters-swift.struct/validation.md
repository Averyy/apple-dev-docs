# validation

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The validation dataset.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var validation: MLWordTagger.ModelParameters.ValidationData { get set }
```

#### Discussion

The default value is an [`MLWordTagger.ModelParameters.ValidationData.split(strategy:)`](./validationdata-swift.enum/split%28strategy%29.md) instance with the [`MLSplitStrategy.automatic`](../../mlsplitstrategy/automatic.md) split strategy``, which automatically generates the validation dataset by partitioning up to 10% of the training dataset.

## See Also

### Accessing parameters
- [var algorithm: MLWordTagger.ModelAlgorithmType](./algorithm.md)
  The algorithm type.
- [var language: NLLanguage?](./language.md)
  The language setting.
- [var maxIterations: Int?](./maxiterations.md)
  The maximum training iterations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/validation)*