# validation

**Framework**: Create ML  
**Kind**: property

The validation data source.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var validation: MLActivityClassifier.ModelParameters.Validation { get set }
```

#### Discussion

If you don’t specify validation data, the training process automatically sets aside a random subset of the training data as the validation data.

## See Also

- [var validationData: MLDataTable?](mlactivityclassifier/modelparameters-swift.struct/validationdata.md)
  The activity classifier’s validation dataset.
- [var batchSize: Int?](mlactivityclassifier/modelparameters-swift.struct/batchsize.md)
  The number of sequence chunks the training session uses per iteration.
- [var maximumIterations: Int?](mlactivityclassifier/modelparameters-swift.struct/maximumiterations.md)
  The maximum number of iterations over the training data the training session uses.
- [var predictionWindowSize: Int?](mlactivityclassifier/modelparameters-swift.struct/predictionwindowsize.md)
  The number of samples for each labeled activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.struct/validation-swift.property)*