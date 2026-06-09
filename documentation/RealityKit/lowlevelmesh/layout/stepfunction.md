# stepFunction

**Framework**: RealityKit  
**Kind**: property

Determines how the vertex shader steps through the data in this layout.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var stepFunction: MTLVertexStepFunction
```

#### Discussion

Set to `.perInstance` to supply per-instance data (for example, per-instance color) from a vertex buffer. Defaults to `.perVertex`.

## See Also

- [var stepRate: Int](lowlevelmesh/layout/steprate.md)
  The number of instances that share the same per-instance vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/layout/stepfunction)*