# MLWordEmbedding.ModelParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

The model configuration parameters.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(language: NLLanguage?, revision: Int)](./modelparameters-swift.struct/init%28language,revision%29.md)
  Creates model parameters.
### Accessing parameters
- [var revision: Int](./modelparameters-swift.struct/revision.md)
  The revision of the word embedding.
- [var language: NLLanguage?](./modelparameters-swift.struct/language.md)
  The language of the word embedding.
### Describing parameters
- [var description: String](./modelparameters-swift.struct/description.md)
  A text representation of the word embedding parameters.
- [var debugDescription: String](./modelparameters-swift.struct/debugdescription.md)
  A text representation of the word embedding parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelparameters-swift.struct/playgrounddescription.md)
  A description of the word embedding parameters shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./modelparameters-swift.struct/customstringconvertible-implementations.md)

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

### Creating a word embedding
- [init(dictionary: [String : [Double]], parameters: MLWordEmbedding.ModelParameters) throws](./init%28dictionary,parameters%29.md)
  Creates a word embedding.
- [let modelParameters: MLWordEmbedding.ModelParameters](./modelparameters-swift.property.md)
  The model configuration parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordembedding/modelparameters-swift.struct)*