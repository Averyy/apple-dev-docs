# MLWordTagger.ModelParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

Parameters that specify model training parameters and validation data.

**Availability**:
- macOS 10.14+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(validation: MLWordTagger.ModelParameters.ValidationData, algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?)](./modelparameters-swift.struct/init%28validation,algorithm,language%29.md)
  Creates model parameters.
- [MLWordTagger.ModelAlgorithmType](./modelalgorithmtype.md)
  The algorithm type.
- [MLWordTagger.ModelParameters.ValidationData](./modelparameters-swift.struct/validationdata-swift.enum.md)
  The validation data.
### Accessing parameters
- [var algorithm: MLWordTagger.ModelAlgorithmType](./modelparameters-swift.struct/algorithm.md)
  The algorithm type.
- [var language: NLLanguage?](./modelparameters-swift.struct/language.md)
  The language setting.
- [var validation: MLWordTagger.ModelParameters.ValidationData](./modelparameters-swift.struct/validation.md)
  The validation dataset.
- [var maxIterations: Int?](./modelparameters-swift.struct/maxiterations.md)
  The maximum training iterations.
### Describing parameters
- [var description: String](./modelparameters-swift.struct/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](./modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters in a playground.
### Deprecated
- [init(validationData: MLDataTable?, algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?, tokenColumnValidationData: String?, labelColumnValidationData: String?)](./modelparameters-swift.struct/init%28validationdata,algorithm,language,tokencolumnvalidationdata,labelcolumnvalidationdata%29.md)
  Creates model parameters.
- [init(validationData: [(tokens: [MLWordTagger.Token], labels: [String])], algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?)](./modelparameters-swift.struct/init%28validationdata,algorithm,language%29.md)
  Creates model parameters.
- [var validationData: MLDataTable?](./modelparameters-swift.struct/validationdata-swift.property.md)
  The word tagger’s validation dataset as a data table.
- [var tokenColumnValidationData: String?](./modelparameters-swift.struct/tokencolumnvalidationdata.md)
  The name of the column containing the tokens in the validation data table.
- [var labelColumnValidationData: String?](./modelparameters-swift.struct/labelcolumnvalidationdata.md)
  The name of the column containing the token labels in the validation data table.
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

## See Also

### Creating and training a word tagger
- [init(trainingData: [(tokens: [MLWordTagger.Token], labels: [String])], parameters: MLWordTagger.ModelParameters) throws](./init%28trainingdata,parameters%29.md)
  Creates a word tagger.
- [init(trainingData:tokenColumn:labelColumn:parameters:)](./init%28trainingdata,tokencolumn,labelcolumn,parameters%29.md)
  Creates a word tagger.
- [MLWordTagger.Token](./token.md)
  The token type of a word tagger, which is a string.
- [let modelParameters: MLWordTagger.ModelParameters](./modelparameters-swift.property.md)
  The configuration parameters that the word tagger used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct)*