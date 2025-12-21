# MLActivityClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct

Model training parameters that direct the training process for an activity classifier model.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(validation: MLActivityClassifier.ModelParameters.Validation, batchSize: Int?, maximumIterations: Int?, predictionWindowSize: Int?)](mlactivityclassifier/modelparameters-swift.struct/init(validation:batchsize:maximumiterations:predictionwindowsize:).md)
  Creates a set of activity classifier parameters that includes a validation dataset in a data source.
- [init(validationData:batchSize:maximumIterations:predictionWindowSize:)](mlactivityclassifier/modelparameters-swift.struct/init(validationdata:batchsize:maximumiterations:predictionwindowsize:).md)
  Creates a set of activity classifier parameters that includes a validation dataset in a data source.
- [MLActivityClassifier.ModelParameters.Validation](mlactivityclassifier/modelparameters-swift.struct/validation-swift.enum.md)
  The source of a validation dataset for an activity classifier.
### Accessing the training parameters
- [var validationData: MLDataTable?](mlactivityclassifier/modelparameters-swift.struct/validationdata.md)
  The activity classifier’s validation dataset.
- [var batchSize: Int?](mlactivityclassifier/modelparameters-swift.struct/batchsize.md)
  The number of sequence chunks the training session uses per iteration.
- [var maximumIterations: Int?](mlactivityclassifier/modelparameters-swift.struct/maximumiterations.md)
  The maximum number of iterations over the training data the training session uses.
- [var predictionWindowSize: Int?](mlactivityclassifier/modelparameters-swift.struct/predictionwindowsize.md)
  The number of samples for each labeled activity.
- [var validation: MLActivityClassifier.ModelParameters.Validation](mlactivityclassifier/modelparameters-swift.struct/validation-swift.property.md)
  The validation data source.
### Describing parameters
- [var description: String](mlactivityclassifier/modelparameters-swift.struct/description.md)
  A text representation of the activity-model parameters.
- [var debugDescription: String](mlactivityclassifier/modelparameters-swift.struct/debugdescription.md)
  A text representation of the activity-model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlactivityclassifier/modelparameters-swift.struct/playgrounddescription.md)
  A description of the activity-model parameters shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlactivityclassifier/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlactivityclassifier/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlactivityclassifier/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [MLActivityClassifier.DataSource](mlactivityclassifier/datasource.md)
  A data source for an activity classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.struct)*