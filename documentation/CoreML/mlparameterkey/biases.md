# biases

**Framework**: Core ML  
**Kind**: property

The key you use to access the biases of a layer in a neural network model.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class var biases: MLParameterKey { get }
```

#### Discussion

The value type for the [`biases`](mlparameterkey/biases.md) key is an [`MLMultiArray`](mlmultiarray.md). You must scope this key with the name of the specific neural network layer whose biases you’d like to access. See [`scoped(to:)`](mlparameterkey/scoped(to:).md).

> **Note**:  You can only override the biases of a model’s  layers. Model developers mark these layers as updatable with the [`Core ML Tools`](https://developer.apple.comhttps://coremltools.readme.io/).

## See Also

- [class var weights: MLParameterKey](mlparameterkey/weights.md)
  The key you use to access the weights of a layer in a neural network model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlparameterkey/biases)*