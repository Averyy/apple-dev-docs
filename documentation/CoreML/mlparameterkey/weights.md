# weights

**Framework**: Core ML  
**Kind**: property  
**Role**: Type Property

The key you use to access the weights of a layer in a neural network model.

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
class var weights: MLParameterKey { get }
```

```objc
@property (class, nonatomic, readonly) MLParameterKey * weights;
```

## Discussion

The value type for the [`weights`](./weights.md) key is an [`MLMultiArray`](../mlmultiarray.md). You must scope this key with the name of the specific neural network layer whose weights you’d like to access. See [`scoped(to:)`](./scoped%28to%29.md).

> **Note**:  You can only override the weights of a model’s *updatable* layers. Model developers mark these layers as updatable with the [Core ML Tools](https://coremltools.readme.io/).

## See Also

### Accessing neural network layer parameters
- [class var biases: MLParameterKey](./biases.md)
  The key you use to access the biases of a layer in a neural network model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlparameterkey/weights)*