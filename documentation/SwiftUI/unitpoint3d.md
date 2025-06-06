# UnitPoint3D

**Framework**: SwiftUI  
**Kind**: struct

A normalized 3D point in a view’s coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@frozen
struct UnitPoint3D
```

#### Overview

Use a 3D unit point to represent a three-dimensional location in a view without having to know the view’s rendered size. The point stores a value in each dimension that indicates the fraction of the view’s size in that dimension — measured from the view’s origin — where the point appears. For example, you can create a unit point that represents the center of any view by using the value `0.5` for each dimension:

```swift
let unitPoint = UnitPoint3D(x: 0.5, y: 0.5, z: 0.5)
```

> **Note**: If you need a two-dimensional unit point, use [`UnitPoint`](unitpoint.md) instead.

If you need a two-dimensional unit point, use [`UnitPoint`](unitpoint.md) instead.

To project the unit point into the rendered view’s coordinate space, multiply each component of the unit point with the corresponding component of the view’s size:

```swift
let projectedPoint = Point3D(
    x: unitPoint.x * size.width,
    y: unitPoint.y * size.height,
    z: unitPoint.z * size.depth
)
```

You can perform this calculation yourself if you happen to know a view’s size, or if you want to use a unit point for some custom purpose, but SwiftUI typically does this for you to carry out operations that you request, like when you rotate a view with the [`rotation3DEffect(_:anchor:)`](view/rotation3deffect(_:anchor:).md) modifier and indicate the anchor point that you want to rotate the view around.

You can create custom unit points with explicit values, like the example above, or you can use one of the built-in unit points that SwiftUI provides, like [`zero`](unitpoint3d/zero.md), [`center`](unitpoint3d/center.md), or [`topTrailing`](unitpoint3d/toptrailing.md). The built-in values correspond to common anchor points that you might want to refer to, like the center of one of a view’s edges.

> **Note**: A unit point with one or more components outside the range `[0, 1]` projects to a point outside of the view.

A unit point with one or more components outside the range `[0, 1]` projects to a point outside of the view.

##### Layout Direction

When a person configures their device to use a left-to-right language like English, the system places the view’s origin in its top-left-back corner, with positive x toward the right, positive y toward the bottom of the view, and positive z toward the front. In a right-to-left environment, the origin moves to the upper-right-back corner, and the positive x direction changes to be toward the left. You don’t typically need to do anything to handle this change, because SwiftUI applies the change to all aspects of the system. For example, see the discussion about layout direction in [`HorizontalAlignment`](horizontalalignment.md).

It’s important to test your app for the different locales that you distribute your app in. For more information about the localization process, see [`Localization`](https://developer.apple.com/documentation/Xcode/localization).

## Topics

### Getting the origin
- [static let origin: UnitPoint3D](unitpoint3d/origin.md)
  The origin of a view.
- [static let zero: UnitPoint3D](unitpoint3d/zero.md)
  A 3D unit point with all components equal to zero.
### Getting top points
- [static let topLeadingBack: UnitPoint3D](unitpoint3d/topleadingback.md)
  A point that’s in the top-leading-back corner of a view.
- [static let topLeading: UnitPoint3D](unitpoint3d/topleading.md)
  A point that’s centered in the depth dimension on the top-leading edge of a view.
- [static let topLeadingFront: UnitPoint3D](unitpoint3d/topleadingfront.md)
  A point that’s in the top-leading-front corner of a view.
- [static let topBack: UnitPoint3D](unitpoint3d/topback.md)
  A point that’s centered horizontally on the top-back edge of a view.
- [static let top: UnitPoint3D](unitpoint3d/top.md)
  A point that’s centered horizontally and in the depth dimension on the top face of a view.
- [static let topFront: UnitPoint3D](unitpoint3d/topfront.md)
  A point that’s centered horizontally on the top-front edge of a view.
- [static let topTrailingBack: UnitPoint3D](unitpoint3d/toptrailingback.md)
  A point that’s in the top-trailing-back corner of a view.
- [static let topTrailing: UnitPoint3D](unitpoint3d/toptrailing.md)
  A point that’s centered in the depth dimension on the top-trailing edge of a view.
- [static let topTrailingFront: UnitPoint3D](unitpoint3d/toptrailingfront.md)
  A point that’s in the top-trailing-front corner of a view.
### Getting middle points
- [static let leadingBack: UnitPoint3D](unitpoint3d/leadingback.md)
  A point that’s centered vertically on the leading-back edge of a view.
- [static let leading: UnitPoint3D](unitpoint3d/leading.md)
  A point that’s centered vertically and in the depth dimension on the leading face of a view.
- [static let leadingFront: UnitPoint3D](unitpoint3d/leadingfront.md)
  A point that’s centered vertically on the leading-front edge of a view.
- [static let back: UnitPoint3D](unitpoint3d/back.md)
  A point that’s centered horizontally and vertically on the back face of a view.
- [static let center: UnitPoint3D](unitpoint3d/center.md)
  A point that’s centered in a view.
- [static let front: UnitPoint3D](unitpoint3d/front.md)
  A point that’s centered horizontally and vertically on the front face of a view.
- [static let trailingBack: UnitPoint3D](unitpoint3d/trailingback.md)
  A point that’s centered vertically on the trailing-back edge of a view.
- [static let trailing: UnitPoint3D](unitpoint3d/trailing.md)
  A point that’s centered vertically and in the depth dimension on the trailing face of a view.
- [static let trailingFront: UnitPoint3D](unitpoint3d/trailingfront.md)
  A point that’s centered vertically on the trailing-front edge of a view.
### Getting bottom points
- [static let bottomLeadingBack: UnitPoint3D](unitpoint3d/bottomleadingback.md)
  A point that’s in the bottom-leading-back corner of a view.
- [static let bottomLeading: UnitPoint3D](unitpoint3d/bottomleading.md)
  A point that’s centered in the depth dimension on the bottom-leading edge of a view.
- [static let bottomLeadingFront: UnitPoint3D](unitpoint3d/bottomleadingfront.md)
  A point that’s in the bottom-leading-front corner of a view.
- [static let bottomBack: UnitPoint3D](unitpoint3d/bottomback.md)
  A point that’s centered horizontally on the bottom-back edge of a view.
- [static let bottom: UnitPoint3D](unitpoint3d/bottom.md)
  A point that’s centered horizontally and in the depth dimension on the bottom face of a view.
- [static let bottomFront: UnitPoint3D](unitpoint3d/bottomfront.md)
  A point that’s centered horizontally on the bottom-front edge of a view.
- [static let bottomTrailingBack: UnitPoint3D](unitpoint3d/bottomtrailingback.md)
  A point that’s in the bottom-trailing-back corner of a view.
- [static let bottomTrailing: UnitPoint3D](unitpoint3d/bottomtrailing.md)
  A point that’s centered in the depth dimension on the bottom-trailing edge of a view.
- [static let bottomTrailingFront: UnitPoint3D](unitpoint3d/bottomtrailingfront.md)
  A point that’s in the bottom-trailing-front corner of a view.
### Creating a point
- [init()](unitpoint3d/init.md)
  Creates a 3D unit point at the origin.
- [init(x: CGFloat, y: CGFloat, z: CGFloat)](unitpoint3d/init(x:y:z:).md)
  Creates a 3D unit point with the specified offsets.
### Getting the point’s coordinates
- [var x: CGFloat](unitpoint3d/x.md)
  The normalized distance from the origin to the point in the horizontal direction.
- [var y: CGFloat](unitpoint3d/y.md)
  The normalized distance from the origin to the point in the vertical dimension.
- [var z: CGFloat](unitpoint3d/z.md)
  The normalized distance from the origin to the point in the depth dimension.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum Axis](axis.md)
  The horizontal or vertical dimension in a 2D coordinate system.
- [struct Angle](angle.md)
  A geometric angle whose value you access in either radians or degrees.
- [struct UnitPoint](unitpoint.md)
  A normalized 2D point in a view’s coordinate space.
- [struct Anchor](anchor.md)
  An opaque value derived from an anchor source and a particular view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/unitpoint3d)*