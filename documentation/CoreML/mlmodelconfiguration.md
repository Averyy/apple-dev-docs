# MLModelConfiguration

**Framework**: Core ML  
**Kind**: class

The settings for creating or updating a machine learning model.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class MLModelConfiguration
```

#### Overview

Use a model configuration to:

- Set or override model parameters.
- Designate which device the model uses to make predictions, such as a GPU.
- Restrict the model to use a specific computational device category, such as a CPU.

You typically use a model configuration instance to configure an [`MLModel`](mlmodel.md) instance as you create it with [`init(contentsOf:configuration:)`](mlmodel/init(contentsof:configuration:).md) or create an [`MLUpdateTask`](mlupdatetask.md). See [`Personalizing a Model with On-Device Updates`](personalizing-a-model-with-on-device-updates.md).

Configure your model parameters by setting values for each relevant [`MLParameterKey`](mlparameterkey.md) in the [`parameters`](mlmodelconfiguration/parameters.md) property.

## Topics

### Configuring model parameters
- [var functionName: String?](mlmodelconfiguration/functionname.md)
  Function name that `MLModel` will use.
- [var modelDisplayName: String?](mlmodelconfiguration/modeldisplayname.md)
  A human readable name of a model for display purposes.
- [var parameters: [MLParameterKey : Any]?](mlmodelconfiguration/parameters.md)
  A dictionary of configuration settings your app can override when loading a model.
- [class MLParameterKey](mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.
### Configuring GPU usage
- [var preferredMetalDevice: (any MTLDevice)?](mlmodelconfiguration/preferredmetaldevice.md)
  The metal device you prefer this model use to make predictions (inference) and update the model.
- [var allowLowPrecisionAccumulationOnGPU: Bool](mlmodelconfiguration/allowlowprecisionaccumulationongpu.md)
  A Boolean value that determines whether to allow low-precision accumulation on a GPU.
### Allowing access to processing units
- [var computeUnits: MLComputeUnits](mlmodelconfiguration/computeunits.md)
  The processing unit or units the model uses to make predictions.
- [enum MLComputeUnits](mlcomputeunits.md)
  The set of processing-unit configurations the model can use to make predictions.
### Getting optimization hints
- [var optimizationHints: MLOptimizationHints](mlmodelconfiguration/optimizationhints-1oq0g.md)
  A group of hints for CoreML to optimize

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [struct MLOptimizationHints](mloptimizationhints-swift.struct.md)
- [class MLKey](mlkey.md)
  An abstract base class for machine learning key types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelconfiguration)*