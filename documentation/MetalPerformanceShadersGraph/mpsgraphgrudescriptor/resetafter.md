# resetAfter

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

A parameter that chooses between two variants for the reset gate computation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var resetAfter: Bool { get set }
```

#### Discussion

If set to `YES` then the layer will compute the intermediate value as `c[t] = ( b + (h[t-1] m ) R^T) r[t]`. Otherwise it’s computed as `c[t] = (h[t-1] r[t] m) R^T`. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphgrudescriptor/resetafter)*