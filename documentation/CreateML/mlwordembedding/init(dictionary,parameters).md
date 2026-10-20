# init(dictionary:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a word embedding.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(dictionary: [String : [Double]], parameters: MLWordEmbedding.ModelParameters = ModelParameters()) throws
```

## Parameters

- `dictionary`: A dictionary of strings and their embeddings.
- `parameters`: The model parameters.

## See Also

### Creating a word embedding
- [MLWordEmbedding.ModelParameters](./modelparameters-swift.struct.md)
  The model configuration parameters.
- [let modelParameters: MLWordEmbedding.ModelParameters](./modelparameters-swift.property.md)
  The model configuration parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordembedding/init(dictionary:parameters:))*