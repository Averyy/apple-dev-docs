# init(_:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Initializes an MPSGraphTensorData with an MTLTensor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(_ tensor: any MTLTensor)
```

#### Return Value

A valid MPSGraphTensorData, or nil if allocation failure.

#### Discussion

The internal storage of the MTLTensor will be aliased. Requires tensor to support MTLTensorUsageMachineLearning.

## Parameters

- `tensor`: MTLTensor to be used within the MPSGraphTensorData


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensordata/init(_:)-60j6x)*