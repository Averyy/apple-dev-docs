# gridSize

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The number of rectangles, vertically and horizontally, the training algorithm uses to analyze each input image.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var gridSize: CGSize { get set }
```

## See Also

### Accessing the training parameters
- [var validation: MLObjectDetector.ModelParameters.ValidationData](./validation.md)
  The object detector’s validation dataset for the training session.
- [var batchSize: Int?](./batchsize.md)
  The number of images the training session can use in a training iteration.
- [var maxIterations: Int?](./maxiterations.md)
  The maximum number of iterations the training session can use.
- [var algorithm: MLObjectDetector.ModelParameters.ModelAlgorithmType](./algorithm.md)
  The algorithm the training session uses to train the object detector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/gridsize)*