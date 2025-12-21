# animationOverrideWeight

**Framework**: RealityKit  
**Kind**: property

The blending weights between the FK demand and the your target per demand type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var animationOverrideWeight: (position: Float, rotation: Float) { get set }
```

#### Discussion

Each demand uses either the value you set using [`target`](ikcomponent/constraint/target.md) and [`lookAtTargetPosition`](ikcomponent/constraint/lookattargetposition.md), or computes one from the FK demand pose. These weights control the blending between the two.

The values are in the closed range `[0, 1]`, where a weight value of `0` means the constraint demands are computed from the FK demand, and a weight value of `1` means that [`target`](ikcomponent/constraint/target.md) is used. All values in-between represent linear blend of the two. Default values are 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/constraint/animationoverrideweight)*