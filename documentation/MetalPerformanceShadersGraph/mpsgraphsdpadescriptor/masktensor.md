# maskTensor

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

An optional additive mask tensor applied to the scaled QK^T scores before softmax. Must be broadcast-compatible with shape `[batch, heads, T_q, T_kv]`. Mutually exclusive with [`isCausal`](mpsgraphsdpadescriptor/iscausal.md).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var maskTensor: MPSGraphTensor? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor/masktensor)*