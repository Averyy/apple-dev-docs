# reverse(_:axesTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Creates a reverse operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func reverse(_ tensor: MPSGraphTensor, axesTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) reverseTensor:(MPSGraphTensor *) tensor axesTensor:(MPSGraphTensor *) axesTensor name:(NSString *) name;
```

## Return Value

A valid MPSGraphTensor object.

## Discussion

Reverses a tensor on given axes. Semantics based on [TensorFlow reverse op](https://www.tensorflow.org/api_docs/python/tf/reverse).

## Parameters

- `tensor`: The tensor to be reversed.
- `axesTensor`: A tensor that specifies axes to be reversed (Axes must be unique and within normal axis range).
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/reverse(_:axestensor:name:))*