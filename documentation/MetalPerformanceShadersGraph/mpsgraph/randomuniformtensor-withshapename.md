# randomUniformTensor(withShape:name:)

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
func randomUniformTensor(withShape shape: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

An MPSGraphTensor of shape containing random values in the defined range.

#### Discussion

Returns a tensor of provided shape of random uniform values in the range [0.0, 1.0). Uses a random seed value to initalize state. No state is preserved, and subsequent calls are not guaranteed to result in a unique stream of random values.

## Parameters

- `shape`: The shape of the tensor generated
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/randomuniformtensor(withshape:name:))*