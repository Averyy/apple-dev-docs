# isCausal

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

When YES, a causal (lower-triangular) mask is applied so that each query position attends only to key positions at or before it. Mutually exclusive with [`maskTensor`](mpsgraphsdpadescriptor/masktensor.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var isCausal: Bool { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor/iscausal)*