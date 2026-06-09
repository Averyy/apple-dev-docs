# negativeEdgeInset

**Framework**: RealityKit  
**Kind**: property

The distance from each negative edge (-X, -Y, -Z) of the clip bounds over which opacity fades to 0, expressed in local coordinate space units.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var negativeEdgeInset: SIMD3<Float>
```

#### Discussion

Values range from `0.0` to the half-extent of the bounding box on each axis. For example:

- `0.0` means no feathering on that edge.
- An inset distance  value of `2.0` on X axis  creates a 2-unit feather zone inward from the -X edge.

## See Also

- [var positiveEdgeInset: SIMD3<Float>](clippingcomponent/featherededge-swift.struct/positiveedgeinset.md)
  The distance from each positive edge (+X, +Y, +Z) of the clip bounds over which opacity fades to 0, expressed in local coordinate space units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingcomponent/featherededge-swift.struct/negativeedgeinset)*