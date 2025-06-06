# setWeightData(_:)

**Framework**: Core ML  
**Kind**: method  
**Required**: Yes

Assigns the weights for the connections within the layer.

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
func setWeightData(_ weights: [Data]) throws
```

## Mentions

- [Creating and Integrating a Model with Custom Layers](creating-and-integrating-a-model-with-custom-layers.md)

#### Discussion

Implement this method to assign the weights for all the connections between nodes in your layer. This method is called once after the initialization call. Your implementation should validate the weights and throw an error if the weights do not have the expected shape or values.

The data encoded in the `weights` field of the `.mlmodel` file is loaded and passed into this method. If there are repeated weights in the `.mlmodel` file, they will be listed explicitly in the `weights` array. The weight values are provided in the order that they were defined during the custom layer conversion process. Keep a reference to the `weights` passed in because copying the `weights` array can significantly increase an app’s memory. Avoid modifying values of the weights.

## Parameters

- `weights`: The data encoded in the   field of the model specification.

## See Also

- [func outputShapes(forInputShapes: [[NSNumber]]) throws -> [[NSNumber]]](mlcustomlayer/outputshapes(forinputshapes:).md)
  Calculates the shapes of the output of this layer for the given input shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcustomlayer/setweightdata(_:))*