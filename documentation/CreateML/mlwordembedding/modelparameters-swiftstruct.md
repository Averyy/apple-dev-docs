# MLWordEmbedding.ModelParameters

**Framework**: Create ML  
**Kind**: struct

The model configuration parameters.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(language: NLLanguage?, revision: Int)](mlwordembedding/modelparameters-swift.struct/init(language:revision:).md)
  Creates model parameters.
### Accessing parameters
- [var revision: Int](mlwordembedding/modelparameters-swift.struct/revision.md)
  The revision of the word embedding.
- [var language: NLLanguage?](mlwordembedding/modelparameters-swift.struct/language.md)
  The language of the word embedding.
### Describing parameters
- [var description: String](mlwordembedding/modelparameters-swift.struct/description.md)
  A text representation of the word embedding parameters.
- [var debugDescription: String](mlwordembedding/modelparameters-swift.struct/debugdescription.md)
  A text representation of the word embedding parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlwordembedding/modelparameters-swift.struct/playgrounddescription.md)
  A description of the word embedding parameters shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlwordembedding/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlwordembedding/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlwordembedding/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(dictionary: [String : [Double]], parameters: MLWordEmbedding.ModelParameters) throws](mlwordembedding/init(dictionary:parameters:).md)
  Creates a word embedding.
- [let modelParameters: MLWordEmbedding.ModelParameters](mlwordembedding/modelparameters-swift.property.md)
  The model configuration parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct)*