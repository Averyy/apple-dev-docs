# MLTextClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct

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
- [init(validation: MLTextClassifier.ModelParameters.ValidationData, algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?)](mltextclassifier/modelparameters-swift.struct/init(validation:algorithm:language:).md)
  Creates model parameters for a text classifier with the specified validation data, algorithm, and language.
- [struct NLLanguage](../NaturalLanguage/NLLanguage.md)
  The languages that the Natural Language framework supports.
- [MLTextClassifier.ModelAlgorithmType](mltextclassifier/modelalgorithmtype.md)
  The type of algorithm that a text classifier uses.
- [MLTextClassifier.ModelParameters.ValidationData](mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  The validation data that a text classifier uses.
### Accessing parameters
- [var algorithm: MLTextClassifier.ModelAlgorithmType](mltextclassifier/modelparameters-swift.struct/algorithm.md)
  The parameter’s algorithm setting.
- [var language: NLLanguage?](mltextclassifier/modelparameters-swift.struct/language.md)
  The parameter’s language setting.
- [var validation: MLTextClassifier.ModelParameters.ValidationData](mltextclassifier/modelparameters-swift.struct/validation.md)
  The validation dataset.
- [var maxIterations: Int?](mltextclassifier/modelparameters-swift.struct/maxiterations.md)
  The maximum number of training iterations.
### Describing parameters
- [var description: String](mltextclassifier/modelparameters-swift.struct/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](mltextclassifier/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](mltextclassifier/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters in a playground.
### Deprecated
- [init(validationData: [String : [String]], algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?)](mltextclassifier/modelparameters-swift.struct/init(validationdata:algorithm:language:)-xplw.md)
  Creates parameters for a text classifier with validation data in a dictionary.
- [init(validationData: MLDataTable?, algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?, textColumnValidationData: String?, labelColumnValidationData: String?)](mltextclassifier/modelparameters-swift.struct/init(validationdata:algorithm:language:textcolumnvalidationdata:labelcolumnvalidationdata:).md)
  Creates parameters for a text classifier with validation data in a data table.
- [init(validationData: MLTextClassifier.DataSource, algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?)](mltextclassifier/modelparameters-swift.struct/init(validationdata:algorithm:language:)-95vq7.md)
  Creates parameters for a text classifier with validation data in a set of labeled directories.
- [var validationData: MLDataTable?](mltextclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  The validation data.
- [var textColumnValidationData: String?](mltextclassifier/modelparameters-swift.struct/textcolumnvalidationdata.md)
  The name of the text column in the validation data table.
- [var labelColumnValidationData: String?](mltextclassifier/modelparameters-swift.struct/labelcolumnvalidationdata.md)
  The name of the label column in the validation data table.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mltextclassifier/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mltextclassifier/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mltextclassifier/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [init(trainingData: [String : [String]], parameters: MLTextClassifier.ModelParameters) throws](mltextclassifier/init(trainingdata:parameters:)-9uj3q.md)
  Creates a text classifier.
- [init(trainingData: DataFrame, textColumn: String, labelColumn: String, parameters: MLTextClassifier.ModelParameters) throws](mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:)-6keqn.md)
  Creates a text classifier.
- [init(trainingData: MLTextClassifier.DataSource, parameters: MLTextClassifier.ModelParameters) throws](mltextclassifier/init(trainingdata:parameters:)-8n8vs.md)
  Creates a text classifier.
- [MLTextClassifier.DataSource](mltextclassifier/datasource.md)
  A data source for a text classifier.
- [let modelParameters: MLTextClassifier.ModelParameters](mltextclassifier/modelparameters-swift.property.md)
  The configuration parameters that the text classifier used for training during initialization.
- [init(trainingData: MLDataTable, textColumn: String, labelColumn: String, parameters: MLTextClassifier.ModelParameters) throws](mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:)-7lp6w.md)
  Creates a text classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct)*