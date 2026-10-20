# MLWordTagger.Token

**Framework**: Create ML  
**Kind**: typealias  
**Role**: Type Alias

The token type of a word tagger, which is a string.

**Availability**:
- macOS 10.14+

## Declaration

```swift
typealias Token = String
```

## See Also

### Creating and training a word tagger
- [init(trainingData: [(tokens: [MLWordTagger.Token], labels: [String])], parameters: MLWordTagger.ModelParameters) throws](./init%28trainingdata,parameters%29.md)
  Creates a word tagger.
- [init(trainingData:tokenColumn:labelColumn:parameters:)](./init%28trainingdata,tokencolumn,labelcolumn,parameters%29.md)
  Creates a word tagger.
- [MLWordTagger.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLWordTagger.ModelParameters](./modelparameters-swift.property.md)
  The configuration parameters that the word tagger used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/token)*