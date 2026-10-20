# init(_:rank:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Initializes a tensor data with an MPS matrix enforcing rank of the result.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(_ matrix: MPSMatrix, rank: Int)
```

#### Return Value

A valid MPSGraphTensorData of given rank, or nil if allocation failure.

#### Discussion

The device of the MPSMatrix will be used to get the MPSDevice for this MPSGraphTensorData.

## Parameters

- `matrix`: MPSMatrix to be used within the MPSGraphTensorData
- `rank`: The rank of the resulting TensorData tensor. NOTE: must be within { 1, … ,16 }.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensordata/init(_:rank:)-1lnxg)*