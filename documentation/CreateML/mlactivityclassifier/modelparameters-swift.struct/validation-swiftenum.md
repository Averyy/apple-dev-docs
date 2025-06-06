# MLActivityClassifier.ModelParameters.Validation

**Framework**: Create ML  
**Kind**: enum

The source of a validation dataset for an activity classifier.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum Validation
```

## Topics

### Specifying validation data
- [MLActivityClassifier.ModelParameters.Validation.split(strategy:)](mlactivityclassifier/modelparameters-swift.struct/validation-swift.enum/split(strategy:).md)
  A validation dataset derived by randomly selecting a portion of the training data.
- [MLActivityClassifier.ModelParameters.Validation.dataSource(_:)](mlactivityclassifier/modelparameters-swift.struct/validation-swift.enum/datasource(_:).md)
  A validation dataset represented by a data source.
- [MLActivityClassifier.ModelParameters.Validation.none](mlactivityclassifier/modelparameters-swift.struct/validation-swift.enum/none.md)
  An empty validation dataset that skips the model validation phase after training.

## See Also

- [init(validation: MLActivityClassifier.ModelParameters.Validation, batchSize: Int?, maximumIterations: Int?, predictionWindowSize: Int?)](mlactivityclassifier/modelparameters-swift.struct/init(validation:batchsize:maximumiterations:predictionwindowsize:).md)
  Creates a set of activity classifier parameters that includes a validation dataset in a data source.
- [init(validationData: MLActivityClassifier.DataSource, batchSize: Int?, maximumIterations: Int?, predictionWindowSize: Int?)](mlactivityclassifier/modelparameters-swift.struct/init(validationdata:batchsize:maximumiterations:predictionwindowsize:)-66z1y.md)
  Creates a set of activity classifier parameters that includes a validation dataset in a data source.
- [init(validationData: MLDataTable?, batchSize: Int?, maximumIterations: Int?, predictionWindowSize: Int?)](mlactivityclassifier/modelparameters-swift.struct/init(validationdata:batchsize:maximumiterations:predictionwindowsize:)-6lc3g.md)
  Creates a set of activity classifier parameters that includes a validation dataset in a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.struct/validation-swift.enum)*