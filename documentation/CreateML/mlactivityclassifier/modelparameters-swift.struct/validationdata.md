# validationData

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The activity classifier’s validation dataset.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

> **Deprecated**: Use validationDataSource

## Declaration

```swift
var validationData: MLDataTable?
```

#### Discussion

If you don’t specify validation data, the training process automatically sets aside a random subset of the training data as the validation data.

## See Also

### Accessing the training parameters
- [var batchSize: Int?](./batchsize.md)
  The number of sequence chunks the training session uses per iteration.
- [var maximumIterations: Int?](./maximumiterations.md)
  The maximum number of iterations over the training data the training session uses.
- [var predictionWindowSize: Int?](./predictionwindowsize.md)
  The number of samples for each labeled activity.
- [var validation: MLActivityClassifier.ModelParameters.Validation](./validation-swift.property.md)
  The validation data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.struct/validationdata)*