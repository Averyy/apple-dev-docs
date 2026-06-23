# maskTensor

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

An optional additive mask tensor applied to the scaled QK^T scores before softmax. Must be broadcast-compatible with shape `[batch, heads, T_q, T_kv]`. Mutually exclusive with [`isCausal`](mpsgraphsdpadescriptor/iscausal.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var maskTensor: MPSGraphTensor? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor/masktensor)*