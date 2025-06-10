# Alignment3D

**Framework**: SwiftUI  
**Kind**: struct

An alignment in all three axes.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
@frozen
struct Alignment3D
```

## Topics

### Initializers
- [init(horizontal: HorizontalAlignment, vertical: VerticalAlignment, depth: DepthAlignment)](alignment3d/init(horizontal:vertical:depth:).md)
  Creates a custom alignment value with the specified horizontal, vertical and depth alignment guides.
### Instance Properties
- [var depth: DepthAlignment](alignment3d/depth.md)
  The alignment on the depth axis.
- [var horizontal: HorizontalAlignment](alignment3d/horizontal.md)
  The alignment on the horizontal axis.
- [var vertical: VerticalAlignment](alignment3d/vertical.md)
  The alignment on the vertical axis.
### Type Properties
- [static let back: Alignment3D](alignment3d/back.md)
  A guide representing a point at the center of the horizontal axis, center of the vertical axis, and back of the depth axis.
- [static let bottom: Alignment3D](alignment3d/bottom.md)
  A guide representing a point at the center of the horizontal axis, bottom of the vertical axis, and center of the depth axis.
- [static let bottomBack: Alignment3D](alignment3d/bottomback.md)
  A guide representing a point at the center of the horizontal axis, bottom of the vertical axis, and back of the depth axis.
- [static let bottomFront: Alignment3D](alignment3d/bottomfront.md)
  A guide representing a point at the center of the horizontal axis, bottom of the vertical axis, and front of the depth axis.
- [static let bottomLeading: Alignment3D](alignment3d/bottomleading.md)
  A guide representing a point at the leading edge of the horizontal axis, bottom of the vertical axis, and center of the depth axis.
- [static let bottomLeadingBack: Alignment3D](alignment3d/bottomleadingback.md)
  A guide representing a point at the leading edge of the horizontal axis, bottom of the vertical axis, and back of the depth axis.
- [static let bottomLeadingFront: Alignment3D](alignment3d/bottomleadingfront.md)
  A guide representing a point at the leading edge of the horizontal axis, bottom of the vertical axis, and front of the depth axis.
- [static let bottomTrailing: Alignment3D](alignment3d/bottomtrailing.md)
  A guide representing a point at the trailing edge of the horizontal axis, bottom of the vertical axis, and center of the depth axis.
- [static let bottomTrailingBack: Alignment3D](alignment3d/bottomtrailingback.md)
  A guide representing a point at the trailing edge of the horizontal axis, bottom of the vertical axis, and back of the depth axis.
- [static let bottomTrailingFront: Alignment3D](alignment3d/bottomtrailingfront.md)
  A guide representing a point at the trailing edge of the horizontal axis, bottom of the vertical axis, and front of the depth axis.
- [static let center: Alignment3D](alignment3d/center.md)
  A guide representing a point at the center of the horizontal axis, center of the vertical axis, and center of the depth axis.
- [static let front: Alignment3D](alignment3d/front.md)
  A guide representing a point at the center of the horizontal axis, center of the vertical axis, and front of the depth axis.
- [static let leading: Alignment3D](alignment3d/leading.md)
  A guide representing a point at the leading edge of the horizontal axis, center of the vertical axis, and center of the depth axis.
- [static let leadingBack: Alignment3D](alignment3d/leadingback.md)
  A guide representing a point at the leading edge of the horizontal axis, center of the vertical axis, and back of the depth axis.
- [static let leadingFront: Alignment3D](alignment3d/leadingfront.md)
  A guide representing a point at the leading edge of the horizontal axis, center of the vertical axis, and front of the depth axis.
- [static let top: Alignment3D](alignment3d/top.md)
  A guide representing a point at the center of the horizontal axis, top of the vertical axis, and center of the depth axis.
- [static let topBack: Alignment3D](alignment3d/topback.md)
  A guide representing a point at the center of the horizontal axis, top of the vertical axis, and back of the depth axis.
- [static let topFront: Alignment3D](alignment3d/topfront.md)
  A guide representing a point at the center of the horizontal axis, top of the vertical axis, and front of the depth axis.
- [static let topLeading: Alignment3D](alignment3d/topleading.md)
  A guide representing a point at the center of the horizontal axis, top of the vertical axis, and center of the depth axis.
- [static let topLeadingBack: Alignment3D](alignment3d/topleadingback.md)
  A guide representing a point at the leading edge of the horizontal axis, top of the vertical axis, and back of the depth axis.
- [static let topLeadingFront: Alignment3D](alignment3d/topleadingfront.md)
  A guide representing a point at the leading edge of the horizontal axis, top of the vertical axis, and front of the depth axis.
- [static let topTrailing: Alignment3D](alignment3d/toptrailing.md)
  A guide representing a point at the trailing edge of the horizontal axis, top of the vertical axis, and center of the depth axis.
- [static let topTrailingBack: Alignment3D](alignment3d/toptrailingback.md)
  A guide representing a point at the trailing edge of the horizontal axis, top of the vertical axis, and back of the depth axis.
- [static let topTrailingFront: Alignment3D](alignment3d/toptrailingfront.md)
  A guide representing a point at the trailing edge of the horizontal axis, top of the vertical axis, and front of the depth axis.
- [static let trailing: Alignment3D](alignment3d/trailing.md)
  A guide representing a point at the trailing edge of the horizontal axis, center of the vertical axis, and center of the depth axis.
- [static let trailingBack: Alignment3D](alignment3d/trailingback.md)
  A guide representing a point at the trailing edge of the horizontal axis, center of the vertical axis, and back of the depth axis.
- [static let trailingFront: Alignment3D](alignment3d/trailingfront.md)
  A guide representing a point at the trailing edge of the horizontal axis, center of the vertical axis, and front of the depth axis.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [enum Axis](axis.md)
  The horizontal or vertical dimension in a 2D coordinate system.
- [struct Angle](angle.md)
  A geometric angle whose value you access in either radians or degrees.
- [struct UnitPoint](unitpoint.md)
  A normalized 2D point in a view’s coordinate space.
- [struct UnitPoint3D](unitpoint3d.md)
  A normalized 3D point in a view’s coordinate space.
- [struct Anchor](anchor.md)
  An opaque value derived from an anchor source and a particular view.
- [protocol DepthAlignmentID](depthalignmentid.md)
- [struct GeometryProxyCoordinateSpace3D](geometryproxycoordinatespace3d.md)
  A representation of a `GeometryProxy3D` which can be used for `CoordinateSpace3D` based conversions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alignment3d)*