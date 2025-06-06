# init(validationData:batchSize:maximumIterations:predictionWindowSize:)

**Framework**: Create ML  
**Kind**: init

Creates a set of activity classifier parameters that includes a validation dataset in a data table.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(validationData: MLDataTable?, batchSize: Int? = 32, maximumIterations: Int? = 10, predictionWindowSize: Int? = 100)
```

## Parameters

- `validationData`: An   instance that contains a validation dataset.
- `batchSize`: The number of activity entries the training session uses for each of its training iterations.
- `maximumIterations`: The largest number of training iterations the training session can use.
- `predictionWindowSize`: The number of time increments the training session uses to train an activity   classifier.

## See Also

- [init(validation: MLActivityClassifier.ModelParameters.Validation, batchSize: Int?, maximumIterations: Int?, predictionWindowSize: Int?)](mlactivityclassifier/modelparameters-swift.struct/init(validation:batchsize:maximumiterations:predictionwindowsize:).md)
  Creates a set of activity classifier parameters that includes a validation dataset in a data source.
- [init(validationData: MLActivityClassifier.DataSource, batchSize: Int?, maximumIterations: Int?, predictionWindowSize: Int?)](mlactivityclassifier/modelparameters-swift.struct/init(validationdata:batchsize:maximumiterations:predictionwindowsize:)-66z1y.md)
  Creates a set of activity classifier parameters that includes a validation dataset in a data source.
- [MLActivityClassifier.ModelParameters.Validation](mlactivityclassifier/modelparameters-swift.struct/validation-swift.enum.md)
  The source of a validation dataset for an activity classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.struct/init(validationdata:batchsize:maximumiterations:predictionwindowsize:)-6lc3g)*