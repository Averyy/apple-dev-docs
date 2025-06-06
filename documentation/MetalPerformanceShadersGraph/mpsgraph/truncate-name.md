# truncate(_:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Applies the truncate operation to the input tensor elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func truncate(_ tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

#### Discussion

This operation applies the floor operation to positive inputs and ceiling operation to negative inputs.

## Parameters

- `tensor`: The input tensor.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/truncate(_:name:))*