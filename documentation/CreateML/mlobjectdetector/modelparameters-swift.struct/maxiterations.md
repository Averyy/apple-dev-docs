# maxIterations

**Framework**: Create ML  
**Kind**: property

The maximum number of iterations the training session can use.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var maxIterations: Int?
```

#### Discussion

If you don’t have a preference, set this property to `nil` to tell Create ML to use an appropriate value when it trains the model.

## See Also

- [var validation: MLObjectDetector.ModelParameters.ValidationData](mlobjectdetector/modelparameters-swift.struct/validation.md)
  The object detector’s validation dataset for the training session.
- [var batchSize: Int?](mlobjectdetector/modelparameters-swift.struct/batchsize.md)
  The number of images the training session can use in a training iteration.
- [var algorithm: MLObjectDetector.ModelParameters.ModelAlgorithmType](mlobjectdetector/modelparameters-swift.struct/algorithm.md)
  The algorithm the training session uses to train the object detector.
- [var gridSize: CGSize](mlobjectdetector/modelparameters-swift.struct/gridsize.md)
  The number of rectangles, vertically and horizontally, the training algorithm uses to analyze each input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/maxiterations)*