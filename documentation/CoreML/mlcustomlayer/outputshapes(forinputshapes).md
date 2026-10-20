# outputShapes(forInputShapes:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Calculates the shapes of the output of this layer for the given input shapes.

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
func outputShapes(forInputShapes inputShapes: [[NSNumber]]) throws -> [[NSNumber]]
```

```objc
- (NSArray<NSArray<NSNumber *> *> *) outputShapesForInputShapes:(NSArray<NSArray<NSNumber *> *> *) inputShapes error:(NSError **) error;
```

## Mentions

- [Creating and Integrating a Model with Custom Layers](../creating-and-integrating-a-model-with-custom-layers.md)

#### Return Value

The shapes of the output for the given input shapes.

#### Discussion

Implement this method to define the layer’s interface with the rest of the network. It will be called at least once at load time and any time the size of the inputs changes in a call to [`prediction(from:)`](../mlmodel/prediction%28from%29-9y2aa.md).

This method consumes and returns arrays of shapes, for inputs and outputs of the custom layer, respectively. See the [Core ML Neural Network specification](https://mlmodel.readme.io/reference/neuralnetwork) for more details about shapes and how layers use them.

## Parameters

- `inputShapes`: The shapes of the input for this layer.

## See Also

### Integrating a layer
- [func setWeightData([Data]) throws](./setweightdata%28_%29.md)
  Assigns the weights for the connections within the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcustomlayer/outputshapes(forinputshapes:))*