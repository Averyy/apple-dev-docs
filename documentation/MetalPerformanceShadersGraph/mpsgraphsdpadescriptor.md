# MPSGraphSDPADescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

A descriptor that configures a scaled dot product attention (SDPA) operation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class MPSGraphSDPADescriptor
```

#### Overview

Use this descriptor with [`scaledDotProductAttention(query:key:value:descriptor:name:)`](mpsgraph/scaleddotproductattention(query:key:value:descriptor:name:).md) to specify optional features such as an attention mask, causal masking, and attention sinks.

## Topics

### Initializers
- [convenience init(scale: Float)](mpsgraphsdpadescriptor/init(scale:).md)
  Creates a descriptor with the given scale and all other properties set to their defaults (no mask, isCausal = NO, no sinks).
### Instance Properties
- [var isCausal: Bool](mpsgraphsdpadescriptor/iscausal.md)
  When YES, a causal (lower-triangular) mask is applied so that each query position attends only to key positions at or before it. Mutually exclusive with [`maskTensor`](mpsgraphsdpadescriptor/masktensor.md).
- [var maskTensor: MPSGraphTensor?](mpsgraphsdpadescriptor/masktensor.md)
  An optional additive mask tensor applied to the scaled QK^T scores before softmax. Must be broadcast-compatible with shape `[batch, heads, T_q, T_kv]`. Mutually exclusive with [`isCausal`](mpsgraphsdpadescriptor/iscausal.md).
- [var scale: Float](mpsgraphsdpadescriptor/scale.md)
  The scale applied to the result of the query–key matrix multiply before softmax. Typically set to `1/sqrt(headDimension)`.
- [var sinksTensor: MPSGraphTensor?](mpsgraphsdpadescriptor/sinkstensor.md)
  An optional attention-sinks tensor of shape `[nHeads]`. Each element seeds the online-softmax accumulator for the corresponding query head with a virtual token logit, causing real-token attention weights to sum to less than one.

## Relationships

### Inherits From
- [MPSGraphObject](mpsgraphobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor)*