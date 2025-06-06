# projectionEffect(_:)

**Framework**: RealityKit  
**Kind**: method

Applies a projection transformation to this view’s rendered output.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func projectionEffect(_ transform: ProjectionTransform) -> some View
```

#### Discussion

Use `projectionEffect(_:)` to apply a 3D transformation to the view.

The example below rotates the text 30˚ around the `z` axis, which is the axis pointing out of the screen:

```None
// This transform represents a 30˚ rotation around the z axis.
let transform = CATransform3DMakeRotation(
    -30 * (.pi / 180), 0.0, 0.0, 1.0)

Text("Projection effects using transforms")
    .projectionEffect(.init(transform))
    .border(Color.gray)
```

## Parameters

- `transform`: A   to apply to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/projectioneffect(_:))*