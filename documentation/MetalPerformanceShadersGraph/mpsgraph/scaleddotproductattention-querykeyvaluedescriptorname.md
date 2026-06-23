# scaledDotProductAttention(query:key:value:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a scaled dot product attention (SDPA) operation using a descriptor and returns the result tensor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func scaledDotProductAttention(query queryTensor: MPSGraphTensor, key keyTensor: MPSGraphTensor, value valueTensor: MPSGraphTensor, descriptor: MPSGraphSDPADescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

The descriptor allows configuring an optional attention mask, causal masking, and attention sinks without requiring a separate API method for each combination of features.

## Parameters

- `queryTensor`: A tensor that represents the query projection.
- `keyTensor`: A tensor that represents the key projection.
- `valueTensor`: A tensor that represents the value projection.
- `descriptor`: A descriptor specifying scale and optional features (mask, isCausal, sinks).
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/scaleddotproductattention(query:key:value:descriptor:name:))*