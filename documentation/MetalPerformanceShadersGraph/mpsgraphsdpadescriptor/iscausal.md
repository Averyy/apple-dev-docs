# isCausal

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

When YES, a causal (lower-triangular) mask is applied so that each query position attends only to key positions at or before it. Mutually exclusive with [`maskTensor`](mpsgraphsdpadescriptor/masktensor.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var isCausal: Bool { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor/iscausal)*