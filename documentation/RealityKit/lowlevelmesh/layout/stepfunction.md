# stepFunction

**Framework**: RealityKit  
**Kind**: property

Determines how the vertex shader steps through the data in this layout.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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