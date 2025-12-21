# MLWordTagger.ModelParameters

**Framework**: Create ML  
**Kind**: struct

Parameters that specify model training parameters and validation data.

**Availability**:
- macOS 10.14+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(validation: MLWordTagger.ModelParameters.ValidationData, algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?)](mlwordtagger/modelparameters-swift.struct/init(validation:algorithm:language:).md)
  Creates model parameters.
- [MLWordTagger.ModelAlgorithmType](mlwordtagger/modelalgorithmtype.md)
  The algorithm type.
- [MLWordTagger.ModelParameters.ValidationData](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum.md)
  The validation data.
### Accessing parameters
- [var algorithm: MLWordTagger.ModelAlgorithmType](mlwordtagger/modelparameters-swift.struct/algorithm.md)
  The algorithm type.
- [var language: NLLanguage?](mlwordtagger/modelparameters-swift.struct/language.md)
  The language setting.
- [var validation: MLWordTagger.ModelParameters.ValidationData](mlwordtagger/modelparameters-swift.struct/validation.md)
  The validation dataset.
- [var maxIterations: Int?](mlwordtagger/modelparameters-swift.struct/maxiterations.md)
  The maximum training iterations.
### Describing parameters
- [var description: String](mlwordtagger/modelparameters-swift.struct/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](mlwordtagger/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlwordtagger/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters in a playground.
### Deprecated
- [init(validationData: MLDataTable?, algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?, tokenColumnValidationData: String?, labelColumnValidationData: String?)](mlwordtagger/modelparameters-swift.struct/init(validationdata:algorithm:language:tokencolumnvalidationdata:labelcolumnvalidationdata:).md)
  Creates model parameters.
- [init(validationData: [(tokens: [MLWordTagger.Token], labels: [String])], algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?)](mlwordtagger/modelparameters-swift.struct/init(validationdata:algorithm:language:).md)
  Creates model parameters.
- [var validationData: MLDataTable?](mlwordtagger/modelparameters-swift.struct/validationdata-swift.property.md)
  The word tagger’s validation dataset as a data table.
- [var tokenColumnValidationData: String?](mlwordtagger/modelparameters-swift.struct/tokencolumnvalidationdata.md)
  The name of the column containing the tokens in the validation data table.
- [var labelColumnValidationData: String?](mlwordtagger/modelparameters-swift.struct/labelcolumnvalidationdata.md)
  The name of the column containing the token labels in the validation data table.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlwordtagger/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlwordtagger/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlwordtagger/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [init(trainingData: [(tokens: [MLWordTagger.Token], labels: [String])], parameters: MLWordTagger.ModelParameters) throws](mlwordtagger/init(trainingdata:parameters:).md)
  Creates a word tagger.
- [init(trainingData:tokenColumn:labelColumn:parameters:)](mlwordtagger/init(trainingdata:tokencolumn:labelcolumn:parameters:).md)
  Creates a word tagger.
- [MLWordTagger.Token](mlwordtagger/token.md)
  The token type of a word tagger, which is a string.
- [let modelParameters: MLWordTagger.ModelParameters](mlwordtagger/modelparameters-swift.property.md)
  The configuration parameters that the word tagger used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct)*