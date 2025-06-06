# MLWordTagger.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum

The algorithm type.

**Availability**:
- macOS 10.14+

## Declaration

```swift
enum ModelAlgorithmType
```

## Topics

### Selecting an algorithm type
- [MLWordTagger.ModelAlgorithmType.crf(revision:)](mlwordtagger/modelalgorithmtype/crf(revision:).md)
  A conditional random field algorithm.
- [case transferLearning(MLWordTagger.FeatureExtractorType, revision: Int)](mlwordtagger/modelalgorithmtype/transferlearning(_:revision:).md)
  A transfer-learning algorithm.
- [MLWordTagger.FeatureExtractorType](mlwordtagger/featureextractortype.md)
  The feature extractors that are available to train a word tagger using with the transfer-learning algorithm option.
### Describing an algorithm type
- [var description: String](mlwordtagger/modelalgorithmtype/description.md)
  A text representation of the model algorithm type.
- [var debugDescription: String](mlwordtagger/modelalgorithmtype/debugdescription.md)
  A text representation of the algorithm type that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlwordtagger/modelalgorithmtype/playgrounddescription.md)
  A description of the algorithm type in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlwordtagger/modelalgorithmtype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlwordtagger/modelalgorithmtype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlwordtagger/modelalgorithmtype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(validation: MLWordTagger.ModelParameters.ValidationData, algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?)](mlwordtagger/modelparameters-swift.struct/init(validation:algorithm:language:).md)
  Creates model parameters.
- [MLWordTagger.ModelParameters.ValidationData](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum.md)
  The validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelalgorithmtype)*