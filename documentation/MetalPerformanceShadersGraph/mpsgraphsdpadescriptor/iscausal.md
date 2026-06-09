# isCausal

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

When YES, a causal (lower-triangular) mask is applied so that each query position attends only to key positions at or before it. Mutually exclusive with [`maskTensor`](mpsgraphsdpadescriptor/masktensor.md).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var isCausal: Bool { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor/iscausal)*