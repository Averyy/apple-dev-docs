# MLObjectDetector.ModelParameters

**Framework**: Create ML  
**Kind**: struct

Parameters that affect the process of training an object detection model.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct ModelParameters
```

#### Overview

Customize the training process of an object detector by creating an [`MLObjectDetector.ModelParameters`](mlobjectdetector/modelparameters-swift.struct.md) instance and passing it to an object detector’s initializer. You can explicitly set values for [`maxIterations`](mlobjectdetector/modelparameters-swift.struct/maxiterations.md) and [`batchSize`](mlobjectdetector/modelparameters-swift.struct/batchsize.md). You can also explicitly define the validation dataset to override the default behavior, which uses a random selection of your training dataset for validation.

## Topics

### Creating object detector parameters
- [init(validation: MLObjectDetector.ModelParameters.ValidationData, batchSize: Int?, maxIterations: Int?)](mlobjectdetector/modelparameters-swift.struct/init(validation:batchsize:maxiterations:).md)
  Creates a model parameters instance for an object-detector training session set to use the full network algorithm.
- [init(validation: MLObjectDetector.ModelParameters.ValidationData, batchSize: Int?, maxIterations: Int?, gridSize: CGSize, algorithm: MLObjectDetector.ModelParameters.ModelAlgorithmType)](mlobjectdetector/modelparameters-swift.struct/init(validation:batchsize:maxiterations:gridsize:algorithm:).md)
  Creates a model parameters instance for an object-detector training session.
- [init(validationData: MLObjectDetector.DataSource, batchSize: Int?, maxIterations: Int?) throws](mlobjectdetector/modelparameters-swift.struct/init(validationdata:batchsize:maxiterations:).md)
  Creates a model parameters instance for an object-detector training session set to use the full network algorithm.
### Accessing the training parameters
- [var validation: MLObjectDetector.ModelParameters.ValidationData](mlobjectdetector/modelparameters-swift.struct/validation.md)
  The object detector’s validation dataset for the training session.
- [var batchSize: Int?](mlobjectdetector/modelparameters-swift.struct/batchsize.md)
  The number of images the training session can use in a training iteration.
- [var maxIterations: Int?](mlobjectdetector/modelparameters-swift.struct/maxiterations.md)
  The maximum number of iterations the training session can use.
- [var algorithm: MLObjectDetector.ModelParameters.ModelAlgorithmType](mlobjectdetector/modelparameters-swift.struct/algorithm.md)
  The algorithm the training session uses to train the object detector.
- [var gridSize: CGSize](mlobjectdetector/modelparameters-swift.struct/gridsize.md)
  The number of rectangles, vertically and horizontally, the training algorithm uses to analyze each input image.
### Describing the model parameters
- [var description: String](mlobjectdetector/modelparameters-swift.struct/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](mlobjectdetector/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlobjectdetector/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters within a playground.
### Supporting types
- [MLObjectDetector.ModelParameters.ValidationData](mlobjectdetector/modelparameters-swift.struct/validationdata.md)
  A validation dataset for an object detector.
- [MLObjectDetector.ModelParameters.ModelAlgorithmType](mlobjectdetector/modelparameters-swift.struct/modelalgorithmtype.md)
  An object-detector training algorithm.
### Enumerations
- [MLObjectDetector.ModelParameters.FeatureExtractorType](mlobjectdetector/modelparameters-swift.struct/featureextractortype.md)
  The underlying base model that extracts image features for an object-detector training session.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlobjectdetector/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlobjectdetector/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlobjectdetector/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [MLObjectDetector.DataSource](mlobjectdetector/datasource.md)
  A data source for an object detector.
- [MLObjectDetector.AnnotationType](mlobjectdetector/annotationtype.md)
  The available types of image annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct)*