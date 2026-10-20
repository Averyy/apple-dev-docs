# negativeEdgeInset

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The distance from each negative edge (-X, -Y, -Z) of the clip bounds over which opacity fades to 0, expressed in local coordinate space units.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var negativeEdgeInset: SIMD3<Float>
```

#### Discussion

Values range from `0.0` to the half-extent of the bounding box on each axis. For example:

- `0.0` means no feathering on that edge.
- An inset distance  value of `2.0` on X axis  creates a 2-unit feather zone inward from the -X edge.

## See Also

### Configuring edge insets
- [var positiveEdgeInset: SIMD3<Float>](./positiveedgeinset.md)
  The distance from each positive edge (+X, +Y, +Z) of the clip bounds over which opacity fades to 0, expressed in local coordinate space units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingcomponent/featherededge-swift.struct/negativeedgeinset)*