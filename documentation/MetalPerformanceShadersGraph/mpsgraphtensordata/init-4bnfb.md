# init(_:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Initializes an MPSGraphTensorData with an MPS ndarray.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(_ ndarray: MPSNDArray)
```

#### Return Value

A valid MPSGraphTensorData, or nil if allocation failure.

#### Discussion

The device of the MPSNDArray will be used to get the MPSDevice for this MPSGraphTensorData.

## Parameters

- `ndarray`: MPSNDArray to be used within the MPSGraphTensorData.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensordata/init(_:)-4bnfb)*