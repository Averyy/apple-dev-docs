# MLWordTagger.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The algorithm type.

**Availability**:
- macOS 10.14+

## Declaration

```swift
enum ModelAlgorithmType
```

## Topics

### Selecting an algorithm type
- [MLWordTagger.ModelAlgorithmType.crf(revision:)](./modelalgorithmtype/crf%28revision%29.md)
  A conditional random field algorithm.
- [case transferLearning(MLWordTagger.FeatureExtractorType, revision: Int)](./modelalgorithmtype/transferlearning%28_,revision%29.md)
  A transfer-learning algorithm.
- [MLWordTagger.FeatureExtractorType](./featureextractortype.md)
  The feature extractors that are available to train a word tagger using with the transfer-learning algorithm option.
### Describing an algorithm type
- [var description: String](./modelalgorithmtype/description.md)
  A text representation of the model algorithm type.
- [var debugDescription: String](./modelalgorithmtype/debugdescription.md)
  A text representation of the algorithm type that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelalgorithmtype/playgrounddescription.md)
  A description of the algorithm type in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./modelalgorithmtype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./modelalgorithmtype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./modelalgorithmtype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLWordTagger.FeatureExtractorType](./featureextractortype.md)
  The feature extractors that are available to train a word tagger using with the transfer-learning algorithm option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelalgorithmtype)*