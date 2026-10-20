# init(validationData:batchSize:maximumIterations:predictionWindowSize:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a set of activity classifier parameters that includes a validation dataset in a data source.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(validationData: MLActivityClassifier.DataSource, batchSize: Int? = 32, maximumIterations: Int? = 10, predictionWindowSize: Int? = 100)
```

**Other overloads**:

```swift
init(validationData: MLDataTable?, batchSize: Int? = 32, maximumIterations: Int? = 10, predictionWindowSize: Int? = 100)
```

## Parameters

- `validationData`: An [`MLActivityClassifier.DataSource`](../datasource.md) instance that contains a validation dataset.
- `batchSize`: The number of activity entries the training session uses for each of its training iterations.
- `maximumIterations`: The largest number of training iterations the training session can use.
- `predictionWindowSize`: The number of time increments the training session uses to train an activity classifier.

## See Also

### Creating parameters
- [init(validation: MLActivityClassifier.ModelParameters.Validation, batchSize: Int?, maximumIterations: Int?, predictionWindowSize: Int?)](./init%28validation,batchsize,maximumiterations,predictionwindowsize%29.md)
  Creates a set of activity classifier parameters that includes a validation dataset in a data source.
- [MLActivityClassifier.ModelParameters.Validation](./validation-swift.enum.md)
  The source of a validation dataset for an activity classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.struct/init(validationdata:batchsize:maximumiterations:predictionwindowsize:))*