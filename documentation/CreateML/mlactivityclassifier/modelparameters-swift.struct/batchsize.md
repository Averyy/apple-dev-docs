# batchSize

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The number of sequence chunks the training session uses per iteration.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var batchSize: Int?
```

## See Also

### Accessing the training parameters
- [var validationData: MLDataTable?](./validationdata.md)
  The activity classifier’s validation dataset.
- [var maximumIterations: Int?](./maximumiterations.md)
  The maximum number of iterations over the training data the training session uses.
- [var predictionWindowSize: Int?](./predictionwindowsize.md)
  The number of samples for each labeled activity.
- [var validation: MLActivityClassifier.ModelParameters.Validation](./validation-swift.property.md)
  The validation data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.struct/batchsize)*