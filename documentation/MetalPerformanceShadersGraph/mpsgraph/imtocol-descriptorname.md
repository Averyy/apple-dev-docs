# imToCol(_:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates an imToCol operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func imToCol(_ source: MPSGraphTensor, descriptor: MPSGraphImToColOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `source`: The tensor containing the source data. Must be of rank 4. The layout is defined by  .
- `descriptor`: The descriptor object that specifies the parameters of the operation.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/imtocol(_:descriptor:name:))*