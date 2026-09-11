# stepRate

**Framework**: RealityKit  
**Kind**: property

The number of instances that share the same per-instance vertex data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var stepRate: Int
```

#### Discussion

Used together with `stepFunction`. When `stepFunction` is `.perInstance`, the vertex shader advances to the next entry in this layout once per `stepRate` instances. Defaults to `1`.

## See Also

- [var stepFunction: MTLVertexStepFunction](lowlevelmesh/layout/stepfunction.md)
  Determines how the vertex shader steps through the data in this layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/layout/steprate)*