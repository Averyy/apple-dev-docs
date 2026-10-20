# randomUniformTensor(withShapeTensor:seed:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a RandomUniform operation and returns random uniform values

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func randomUniformTensor(withShapeTensor shapeTensor: MPSGraphTensor, seed: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

An MPSGraphTensor of shape containing random values in the defined range.

#### Discussion

Returns a tensor of provided shape of random uniform values in the range [0.0, 1.0). Uses the provided seed value to initalize state. No state is preserved, and all calls with equal seed yield an identical stream of random values.

## Parameters

- `shapeTensor`: 1D Int32 or Int64 tensor. The shape of the tensor generated
- `seed`: The seed to use to initialize state. All calls with equal seed yield an identical stream of random values.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/randomuniformtensor(withshapetensor:seed:name:))*