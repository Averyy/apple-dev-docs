# validation

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The validation data source.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var validation: MLActivityClassifier.ModelParameters.Validation { get set }
```

## Discussion

If you don’t specify validation data, the training process automatically sets aside a random subset of the training data as the validation data.

## See Also

### Accessing the training parameters
- [var validationData: MLDataTable?](./validationdata.md)
  The activity classifier’s validation dataset.
- [var batchSize: Int?](./batchsize.md)
  The number of sequence chunks the training session uses per iteration.
- [var maximumIterations: Int?](./maximumiterations.md)
  The maximum number of iterations over the training data the training session uses.
- [var predictionWindowSize: Int?](./predictionwindowsize.md)
  The number of samples for each labeled activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.struct/validation-swift.property)*