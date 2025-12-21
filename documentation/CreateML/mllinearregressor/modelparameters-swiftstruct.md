# MLLinearRegressor.ModelParameters

**Framework**: Create ML  
**Kind**: struct

Parameters that affect the process of training a model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(validation: MLLinearRegressor.ModelParameters.ValidationData, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllinearregressor/modelparameters-swift.struct/init(validation:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
- [init(validationData: MLDataTable?, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllinearregressor/modelparameters-swift.struct/init(validationdata:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
  Creates a new set of parameters.
- [MLLinearRegressor.ModelParameters.ValidationData](mllinearregressor/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var validationData: MLDataTable?](mllinearregressor/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var maxIterations: Int](mllinearregressor/modelparameters-swift.struct/maxiterations.md)
- [var l1Penalty: Double](mllinearregressor/modelparameters-swift.struct/l1penalty.md)
- [var l2Penalty: Double](mllinearregressor/modelparameters-swift.struct/l2penalty.md)
- [var stepSize: Double](mllinearregressor/modelparameters-swift.struct/stepsize.md)
- [var convergenceThreshold: Double](mllinearregressor/modelparameters-swift.struct/convergencethreshold.md)
- [var featureRescaling: Bool](mllinearregressor/modelparameters-swift.struct/featurerescaling.md)
- [var validation: MLLinearRegressor.ModelParameters.ValidationData](mllinearregressor/modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](mllinearregressor/modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a linear regressor.
- [var debugDescription: String](mllinearregressor/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a linear regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mllinearregressor/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a linear regressor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mllinearregressor/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mllinearregressor/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mllinearregressor/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [var model: MLModel](mllinearregressor/model.md)
  The Core ML model.
- [let modelParameters: MLLinearRegressor.ModelParameters](mllinearregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllinearregressor/modelparameters-swift.struct)*