# MLTextClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

Parameters that specify model training parameters and validation data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(validation: MLTextClassifier.ModelParameters.ValidationData, algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?)](./modelparameters-swift.struct/init%28validation,algorithm,language%29.md)
  Creates model parameters for a text classifier with the specified validation data, algorithm, and language.
- [struct NLLanguage](../../NaturalLanguage/nllanguage.md)
  The languages that the Natural Language framework supports.
- [MLTextClassifier.ModelAlgorithmType](./modelalgorithmtype.md)
  The type of algorithm that a text classifier uses.
- [MLTextClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validationdata-swift.enum.md)
  The validation data that a text classifier uses.
### Accessing parameters
- [var algorithm: MLTextClassifier.ModelAlgorithmType](./modelparameters-swift.struct/algorithm.md)
  The parameter’s algorithm setting.
- [var language: NLLanguage?](./modelparameters-swift.struct/language.md)
  The parameter’s language setting.
- [var validation: MLTextClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validation.md)
  The validation dataset.
- [var maxIterations: Int?](./modelparameters-swift.struct/maxiterations.md)
  The maximum number of training iterations.
### Describing parameters
- [var description: String](./modelparameters-swift.struct/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](./modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters in a playground.
### Deprecated
- [init(validationData:algorithm:language:)](./modelparameters-swift.struct/init%28validationdata,algorithm,language%29.md)
  Creates parameters for a text classifier with validation data in a set of labeled directories.
- [init(validationData: MLDataTable?, algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?, textColumnValidationData: String?, labelColumnValidationData: String?)](./modelparameters-swift.struct/init%28validationdata,algorithm,language,textcolumnvalidationdata,labelcolumnvalidationdata%29.md)
  Creates parameters for a text classifier with validation data in a data table.
- [var validationData: MLDataTable?](./modelparameters-swift.struct/validationdata-swift.property.md)
  The validation data.
- [var textColumnValidationData: String?](./modelparameters-swift.struct/textcolumnvalidationdata.md)
  The name of the text column in the validation data table.
- [var labelColumnValidationData: String?](./modelparameters-swift.struct/labelcolumnvalidationdata.md)
  The name of the label column in the validation data table.
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

### Creating and training a text classifier
- [init(trainingData:parameters:)](./init%28trainingdata,parameters%29.md)
  Creates a text classifier.
- [init(trainingData:textColumn:labelColumn:parameters:)](./init%28trainingdata,textcolumn,labelcolumn,parameters%29.md)
  Creates a text classifier.
- [MLTextClassifier.DataSource](./datasource.md)
  A data source for a text classifier.
- [let modelParameters: MLTextClassifier.ModelParameters](./modelparameters-swift.property.md)
  The configuration parameters that the text classifier used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct)*