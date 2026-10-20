# init(validationData:batchSize:maxIterations:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a model parameters instance for an object-detector training session set to use the full network algorithm.

**Availability**:
- macOS 10.15+ - Deprecated in 11.0

## Declaration

```swift
init(validationData: MLObjectDetector.DataSource, batchSize: Int? = nil, maxIterations: Int? = nil) throws
```

## Parameters

- `validationData`: An [`MLObjectDetector.ModelParameters.ValidationData`](./validationdata.md) instance that contains your validation dataset.
- `batchSize`: The number of images the object detector uses for each training iteration. If you don’t have a preference, set this parameter to `nil` to tell Create ML to use an appropriate value when it trains the model.
- `maxIterations`: The largest number of training iterations the object detector can use. If you don’t have a preference, set this parameter to `nil` to tell Create ML to use an appropriate value when it trains the model.

## See Also

### Creating object detector parameters
- [init(validation: MLObjectDetector.ModelParameters.ValidationData, batchSize: Int?, maxIterations: Int?)](./init%28validation,batchsize,maxiterations%29.md)
  Creates a model parameters instance for an object-detector training session set to use the full network algorithm.
- [init(validation: MLObjectDetector.ModelParameters.ValidationData, batchSize: Int?, maxIterations: Int?, gridSize: CGSize, algorithm: MLObjectDetector.ModelParameters.ModelAlgorithmType)](./init%28validation,batchsize,maxiterations,gridsize,algorithm%29.md)
  Creates a model parameters instance for an object-detector training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/init(validationdata:batchsize:maxiterations:))*