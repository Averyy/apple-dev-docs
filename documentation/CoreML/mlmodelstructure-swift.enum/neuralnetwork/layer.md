# MLModelStructure.NeuralNetwork.Layer

**Framework**: Core ML  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
struct Layer
```

## Topics

### Accessing layer properties
- [let inputNames: [String]](./layer/inputnames.md)
  The input names.
- [let name: String](./layer/name.md)
  The layer name.
- [let outputNames: [String]](./layer/outputnames.md)
  The output names.
- [let type: String](./layer/type.md)
  The type of the layer, e,g, “elementwise”, “pooling”, etc.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing the layers
- [let layers: [MLModelStructure.NeuralNetwork.Layer]](./layers.md)
  The topologically sorted layers in the NeuralNetwork.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum/neuralnetwork/layer)*