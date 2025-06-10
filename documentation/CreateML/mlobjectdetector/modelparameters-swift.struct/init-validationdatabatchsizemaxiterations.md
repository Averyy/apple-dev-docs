# init(validationData:batchSize:maxIterations:)

**Framework**: Create ML  
**Kind**: init

Creates a model parameters instance for an object-detector training session set to use the full network algorithm.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(validationData: MLObjectDetector.DataSource, batchSize: Int? = nil, maxIterations: Int? = nil) throws
```

## Parameters

- `validationData`: An   instance that   contains your validation dataset.
- `batchSize`: The number of images the object detector uses for each training iteration. If you don’t have   a preference, set this parameter to   to tell Create ML to use an appropriate value when it trains   the model.
- `maxIterations`: The largest number of training iterations the object detector can use. If you don’t have   a preference, set this parameter to   to tell Create ML to use an appropriate value when it trains   the model.

## See Also

- [init(validation: MLObjectDetector.ModelParameters.ValidationData, batchSize: Int?, maxIterations: Int?)](mlobjectdetector/modelparameters-swift.struct/init(validation:batchsize:maxiterations:).md)
  Creates a model parameters instance for an object-detector training session set to use the full network algorithm.
- [init(validation: MLObjectDetector.ModelParameters.ValidationData, batchSize: Int?, maxIterations: Int?, gridSize: CGSize, algorithm: MLObjectDetector.ModelParameters.ModelAlgorithmType)](mlobjectdetector/modelparameters-swift.struct/init(validation:batchsize:maxiterations:gridsize:algorithm:).md)
  Creates a model parameters instance for an object-detector training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/init(validationdata:batchsize:maxiterations:))*