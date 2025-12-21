# MLCustomLayer

**Framework**: Core ML  
**Kind**: protocol

An interface that defines the behavior of a custom layer in your neural network model.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- macOS 10.13.2+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 4.2+

## Declaration

```swift
protocol MLCustomLayer
```

## Mentions

- [Creating and Integrating a Model with Custom Layers](creating-and-integrating-a-model-with-custom-layers.md)

#### Overview

You use the [`MLCustomLayer`](mlcustomlayer.md) protocol to define the behavior of your own neural network layers in Core ML models. You can deploy novel or proprietary models on your own release schedule. Custom layers also provide a mechanism for pre- or post-processing during model evaluation.

## Topics

### Creating a layer
- [init(parameters: [String : Any]) throws](mlcustomlayer/init(parameters:).md)
  Initializes the custom layer implementation.
### Integrating a layer
- [func setWeightData([Data]) throws](mlcustomlayer/setweightdata(_:).md)
  Assigns the weights for the connections within the layer.
- [func outputShapes(forInputShapes: [[NSNumber]]) throws -> [[NSNumber]]](mlcustomlayer/outputshapes(forinputshapes:).md)
  Calculates the shapes of the output of this layer for the given input shapes.
### Evaluating a layer
- [func evaluate(inputs: [MLMultiArray], outputs: [MLMultiArray]) throws](mlcustomlayer/evaluate(inputs:outputs:).md)
  Evaluates the custom layer with the given inputs.
- [func encode(commandBuffer: any MTLCommandBuffer, inputs: [any MTLTexture], outputs: [any MTLTexture]) throws](mlcustomlayer/encode(commandbuffer:inputs:outputs:).md)
  Encodes GPU commands to evaluate the custom layer.

## See Also

- [Creating and Integrating a Model with Custom Layers](creating-and-integrating-a-model-with-custom-layers.md)
  Add models with custom neural-network layers to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcustomlayer)*