# blendFactor

**Framework**: RealityKit  
**Kind**: property

The degree at which the entity rotates toward the camera.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var blendFactor: Float
```

#### Discussion

The `blendFactor` property is a floating-point number in the range `[0.0, 1.0]`.

- When `blendFactor` is `1.0`, the entity fully faces the camera. This is the default behavior.
- When `blendFactor` is `0.0`, the entity doesn’t rotate at all.
- When `blendFactor` is between `0.0` and `1.0`, the entity partially rotates toward the camera.

The following example configures the entity to rotate by half the angle it needs to directly face the camera by setting the `blendFactor` to `0.5`:

```swift
var billboard = BillboardComponent()
billboard.blendFactor = 0.5
entity.components.set(billboard)
```

For example, here’s how a few different `blendFactor` values affect the orientation:

| 0 | 0.25 | 0.5 | 1 |
| --- | --- | --- | --- |
| ![An image of a vintage-style toy robot in a living room scene. The robot is facing about 45 degrees to the left and down from the viewer’s perspective.](https://docs-assets.developer.apple.com/published/eeff1917f6f47d0a52a049afc17fc1b4/billboardcomponent-robot-side-above-without.jpg) | ![An image of a vintage-style toy robot in a living room scene. The robot is facing about 35 degrees to the left and down from the viewer’s perspective.](https://docs-assets.developer.apple.com/published/8dc18cf95752364b607352f4a8cabc84/billboardcomponent-robot-side-above-blend-25.jpg) | ![An image of a vintage-style toy robot in a living room scene. The robot is facing about 22 degrees to the left and down from the viewer’s perspective.](https://docs-assets.developer.apple.com/published/b15157f8a313099b033a3cc60988252d/billboardcomponent-robot-side-above-blend-50.jpg) | ![An image of a vintage-style toy robot in a living room scene. The robot is facing directly towards the viewer.](https://docs-assets.developer.apple.com/published/83e2c31b61c7e99ba2df03efd08d302b/billboardcomponent-robot-side-above-with.jpg) |

For an example of how to animate `blendFactor`, see [`BillboardAction`](billboardaction.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/billboardcomponent/blendfactor)*