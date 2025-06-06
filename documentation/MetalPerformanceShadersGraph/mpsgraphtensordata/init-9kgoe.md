# init(_:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Initializes a tensor data with an MPS vector.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(_ vector: MPSVector)
```

#### Return Value

A valid MPSGraphTensorData, or nil if allocation failure.

#### Discussion

The device of the MPSVector will be used to get the MPSDevice for this MPSGraphTensorData.

## Parameters

- `vector`: MPSVector to be used within the MPSGraphTensorData


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensordata/init(_:)-9kgoe)*