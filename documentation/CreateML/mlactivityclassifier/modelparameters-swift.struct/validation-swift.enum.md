# MLActivityClassifier.ModelParameters.Validation

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The source of a validation dataset for an activity classifier.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum Validation
```

## Topics

### Specifying validation data
- [MLActivityClassifier.ModelParameters.Validation.split(strategy:)](./validation-swift.enum/split%28strategy%29.md)
  A validation dataset derived by randomly selecting a portion of the training data.
- [MLActivityClassifier.ModelParameters.Validation.dataSource(_:)](./validation-swift.enum/datasource%28_%29.md)
  A validation dataset represented by a data source.
- [MLActivityClassifier.ModelParameters.Validation.none](./validation-swift.enum/none.md)
  An empty validation dataset that skips the model validation phase after training.

## See Also

### Creating parameters
- [init(validation: MLActivityClassifier.ModelParameters.Validation, batchSize: Int?, maximumIterations: Int?, predictionWindowSize: Int?)](./init%28validation,batchsize,maximumiterations,predictionwindowsize%29.md)
  Creates a set of activity classifier parameters that includes a validation dataset in a data source.
- [init(validationData:batchSize:maximumIterations:predictionWindowSize:)](./init%28validationdata,batchsize,maximumiterations,predictionwindowsize%29.md)
  Creates a set of activity classifier parameters that includes a validation dataset in a data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.struct/validation-swift.enum)*