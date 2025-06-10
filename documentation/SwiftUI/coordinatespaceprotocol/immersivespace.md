# immersiveSpace

**Framework**: SwiftUI  
**Kind**: property

The named coordinate space that represents the currently opened [`ImmersiveSpace`](immersivespace.md) scene. If no immersive space is currently opened, this CoordinateSpace provides the same behavior as the `.global` coordinate space.

**Availability**:
- visionOS 1.1+

## Declaration

```swift
static var immersiveSpace: NamedCoordinateSpace { get }
```

#### Discussion

Use this to convert transforms from a window to an immersive space. The following sample converts the top-leading-back origin of a Model3D view to coordinates in the immersive space.

```swift
Model3D(url: URL(string: "https://example.com/robot.usdz")!)
    .onGeometryChange3D(for: AffineTransform3D.self) { proxy in
        // Convert the view's transform to the immersive space
        return proxy.transform(in: .immersiveSpace) ?? .identity
    } action: { transform in
        appModel.immersiveSpaceFromCuboid = transform
    }
}
```

Then, apply it to a corresponding Model3D in the immersive space.

```swift
if let transform = appModel.immersiveSpaceFromRobot {
    Model3D(url: URL(string: "https://example.com/robot.usdz")!)
        // Align the origin of this Model3D to its top-leading-back
        .visualEffect3D({ effect, proxy in
            effect
                .offset(x: proxy.size.width/2, y: proxy.size.height/2)
                .offset(z: proxy.size.depth/2)
        })
        // Apply the transform in SRT order
       .scaleEffect(transform.scale)
       .rotation3DEffect(transform.rotation ?? .identity)
       .transform3DEffect(AffineTransform3D(
           translation: transform.translation))
}
```

To apply scale and rotation relative to a view’s origin, don’t set them at the same time using [`transform3DEffect(_:)`](view/transform3deffect(_:).md). Instead, set them separately using [`scaleEffect(_:anchor:)`](view/scaleeffect(_:anchor:).md) together with [`rotation3DEffect(_:anchor:)`](view/rotation3deffect(_:anchor:).md).

> **Note**: See WWDC24 session [`10153: Dive deep into volumes and immersive spaces`](https://developer.apple.comhttps://developer.apple.com/wwdc24/10153/) for details on how to convert between coordinate spaces with SwiftUI and RealityKit.

## See Also

- [static var global: GlobalCoordinateSpace](coordinatespaceprotocol/global.md)
  The global coordinate space at the root of the view hierarchy.
- [static var local: LocalCoordinateSpace](coordinatespaceprotocol/local.md)
  The local coordinate space of the current view.
- [static func named(some Hashable) -> NamedCoordinateSpace](coordinatespaceprotocol/named(_:).md)
  Creates a named coordinate space using the given value.
- [static var scrollView: NamedCoordinateSpace](coordinatespaceprotocol/scrollview.md)
  The named coordinate space that is added by the system for the innermost containing scroll view.
- [static func scrollView(axis: Axis) -> Self](coordinatespaceprotocol/scrollview(axis:).md)
  The named coordinate space that is added by the system for the innermost containing scroll view that allows scrolling along the provided axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/coordinatespaceprotocol/immersivespace)*