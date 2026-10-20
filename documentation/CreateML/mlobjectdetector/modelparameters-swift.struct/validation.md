# validation

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The object detector’s validation dataset for the training session.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var validation: MLObjectDetector.ModelParameters.ValidationData
```

## See Also

### Accessing the training parameters
- [var batchSize: Int?](./batchsize.md)
  The number of images the training session can use in a training iteration.
- [var maxIterations: Int?](./maxiterations.md)
  The maximum number of iterations the training session can use.
- [var algorithm: MLObjectDetector.ModelParameters.ModelAlgorithmType](./algorithm.md)
  The algorithm the training session uses to train the object detector.
- [var gridSize: CGSize](./gridsize.md)
  The number of rectangles, vertically and horizontally, the training algorithm uses to analyze each input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/validation)*