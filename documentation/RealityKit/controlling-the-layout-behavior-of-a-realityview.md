# Controlling the layout behavior of a reality view

**Framework**: RealityKit

Choose a strategy for sizing frames and centering 3D content.

#### Overview

When you use [`Model3D`](model3d.md) to display a 3D model, the view automatically sizes its frame to fit the visible content, and centers that content within the frame. When your project outgrows [`Model3D`](model3d.md) and you switch to [`RealityView`](realityview.md) for more control over your entities, you lose that automatic sizing and centering behavior. By default, a [`RealityView`](realityview.md) takes up as much space as SwiftUI offers, and doesn’t adjust the position of its content.

The [`realityViewLayoutBehavior(_:)`](https://developer.apple.com/documentation/SwiftUI/View/realityViewLayoutBehavior(_:)) modifier gives you control over how a [`RealityView`](realityview.md) sizes its frame and positions its content. You apply the modifier to your [`RealityView`](realityview.md) and pass in a [`RealityViewLayoutOption`](realityviewlayoutoption.md) value that specifies the behavior you want. Choose from three options: [`fixedSize`](realityviewlayoutoption/fixedsize.md) to match the behavior of [`Model3D`](model3d.md), [`centered`](realityviewlayoutoption/centered.md) to center content within a flexible frame, or [`flexible`](realityviewlayoutoption/flexible.md) to keep the default behavior.

#### Size the Frame to Fit the Content

The most common use of [`realityViewLayoutBehavior(_:)`](https://developer.apple.com/documentation/SwiftUI/View/realityViewLayoutBehavior(_:)) is to make a [`RealityView`](realityview.md) behave like [`Model3D`](model3d.md). Apply the modifier with [`fixedSize`](realityviewlayoutoption/fixedsize.md) to set the frame of the [`RealityView`](realityview.md) equal to the visual bounds of its entity content and center that content within the frame.

```swift
RealityView { content in
    if let model = try? await Entity(named: modelName) {
        content.add(model)
    }
}
.realityViewLayoutBehavior(.fixedSize)
```

With [`fixedSize`](realityviewlayoutoption/fixedsize.md), the [`RealityView`](realityview.md) calculates the visual bounds of all the entities you add in the `make` closure, and creates a frame that tightly wraps that content. This is especially useful when you display a [`RealityView`](realityview.md) alongside other SwiftUI views because the frame accurately represents the size of the 3D content.

#### Center Content Within a Flexible Frame

When you display multiple [`RealityView`](realityview.md) instances side by side, each containing a different model, [`fixedSize`](realityviewlayoutoption/fixedsize.md) produces frames of different sizes. If you want consistent frame sizes across your views while still centering the content, use [`centered`](realityviewlayoutoption/centered.md) instead:

```swift
HStack {
    RealityView { content in
        if let model = try? await Entity(named: "SmallRobot") {
            content.add(model)
        }
    }
    .realityViewLayoutBehavior(.centered)

    RealityView { content in
        if let model = try? await Entity(named: "LargeRobot") {
            content.add(model)
        }
    }
    .realityViewLayoutBehavior(.centered)
}
```

With [`centered`](realityviewlayoutoption/centered.md), each [`RealityView`](realityview.md) keeps its default flexible frame that takes up as much space as SwiftUI provides, but shifts the visual content to the center of that frame. This gives you uniform frame sizes with centered content, regardless of each model’s dimensions.

#### Understand the Performance Tradeoff

The [`realityViewLayoutBehavior(_:)`](https://developer.apple.com/documentation/SwiftUI/View/realityViewLayoutBehavior(_:)) modifier calls [`visualBounds(recursive:relativeTo:excludeInactive:)`](hastransform/visualbounds(recursive:relativeto:excludeinactive:).md) to measure the content after the `make` closure runs. This call has a performance cost, so the modifier computes the layout only once — after `make` completes. It doesn’t recompute the layout when the `update` closure runs. The layout also doesn’t account for any entities you add to the [`RealityView`](realityview.md) during an `update` call.

If you need the layout to account for all of your content, add your entities in the `make` closure rather than deferring them to `update`.

## See Also

- [struct RealityView](realityview.md)
  A view that contains RealityKit content.
- [struct RealityViewContent](realityviewcontent.md)
  The content of a visionOS reality view.
- [struct RealityViewCameraContent](realityviewcameracontent.md)
  The content of a reality view that is displayed through a camera.
- [protocol RealityViewContentProtocol](realityviewcontentprotocol.md)
  A protocol representing the content of a reality view.
- [struct RealityViewDefaultPlaceholder](realityviewdefaultplaceholder.md)
  A view that represents the default placeholder for a RealityView.
- [struct RealityViewEntityCollection](realityviewentitycollection.md)
  A collection of entities in a RealityView.
- [struct RealityViewLayoutOption](realityviewlayoutoption.md)
  Options that specify the frame sizing and content alignment option for `RealityView`.
- [protocol EntityCollection](entitycollection.md)
  An ordered, mutable collection of entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/controlling-the-layout-behavior-of-a-realityview)*