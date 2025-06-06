# randomTensor(withShapeTensor:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a Random op of type matching distribution in descriptor and returns random values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func randomTensor(withShapeTensor shapeTensor: MPSGraphTensor, descriptor: MPSGraphRandomOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

An MPSGraphTensor of shape containing random values in the defined range.

#### Discussion

Returns a tensor of provided shape of random values in the distribution specified. Uses a random seed value to initalize state. No state is preserved, and subsequent calls are not guaranteed to result in a unique stream of random values.

## Parameters

- `shapeTensor`: 1D Int32 or Int64 tensor. The shape of the tensor generated
- `descriptor`: The descriptor of the distribution. See MPSGraphRandomOpDescriptor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/randomtensor(withshapetensor:descriptor:name:))*