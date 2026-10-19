# reservedRegions(kind:options:layoutDirectionBehavior:)

**Framework**: SwiftUI  
**Kind**: method

Returns an array of reserved regions that match the selection options you specify.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
func reservedRegions(kind: ReservedRegion.Kind, options: ReservedRegion.QueryOptions = [], layoutDirectionBehavior: LayoutDirectionBehavior = .mirrors) -> [ReservedRegion]
```

#### Return Value

The reserved regions that overlap the view, with frames in the view’s coordinate space.

#### Discussion

A reserved region is an area of your view that an entity reserves, such as the device hardware. Arrange your view’s content around it. Each region describes a frame, margins, active state, and an identifier.

There are two categories of reserved regions:

- **[`occlusion`](reservedregion/kind-swift.struct/occlusion.md)**: An area where an element, such as the Dynamic Island, a camera, or window controls, cover your content. Place content outside this area.
- **[`division`](reservedregion/kind-swift.struct/division.md)**: An area where content splits into separate regions, such as at the fold of a hinge. Arrange your content on both sides of this area.

Call this method on the proxy of a [`GeometryReader`](geometryreader.md) to get the reserved regions that overlap your view. By default, the method returns only the active regions. To also get the inactive regions, pass [`includeInactive`](reservedregion/queryoptions/includeinactive.md) for the `options` parameter.

In the following example, `RegionAvoidingLayout` is a layout that you write yourself. It takes the reserved regions from the geometry proxy, and places each view it contains in a spot that doesn’t overlap a region:

```swift
GeometryReader { proxy in
    RegionAvoidingLayout(
        regions: proxy.reservedRegions(kind: .occlusion)
    ) {
        ForEach(items) { item in
            ItemView(item)
        }
    }
}
```

Make sure a region’s frame and your layout’s positions use the same coordinates. The frame is measured from the top-leading corner of the view you read it from, but the `bounds` that a layout receives in [`placeSubviews(in:proposal:subviews:cache:)`](layout/placesubviews(in:proposal:subviews:cache:).md) don’t always start at `(0, 0)`. Do your calculations from `(0, 0)`, and add `bounds.origin` only when you place each view.

With some right-to-left languages, SwiftUI flips the left and right sides of a layout. To keep reserved regions consistent with the flipped layout, the system mirrors the frames of reserved regions by default before it gives them to you. A layout that flips automatically, such as a custom [`Layout`](layout.md), lines up with the mirrored frames without extra work.

If you position content in a way that doesn’t flip with the layout direction, pass [`LayoutDirectionBehavior.fixed`](layoutdirectionbehavior/fixed.md) for the `layoutDirectionBehavior` parameter to get the unmirrored frames.

For more information, see [`ReservedRegion`](reservedregion.md).

## Parameters

- `kind`: The kind of reserved region to return, such as [`occlusion`](reservedregion/kind-swift.struct/occlusion.md) or [`division`](reservedregion/kind-swift.struct/division.md).
- `options`: Options that change which regions the method returns. By default, the method returns only active regions. Pass [`includeInactive`](reservedregion/queryoptions/includeinactive.md) to also return regions that aren’t currently active.
- `layoutDirectionBehavior`: A value that determines how the method handles right-to-left layout directions. By default, the system mirrors the frames of the regions. Pass [`LayoutDirectionBehavior.fixed`](layoutdirectionbehavior/fixed.md) to get unmirrored frames.

## See Also

- [struct GeometryReader](geometryreader.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryReader3D](geometryreader3d.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryProxy](geometryproxy.md)
  A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [struct ReservedRegion](reservedregion.md)
  A region within a view’s coordinate space that another entity reserves.
- [struct GeometryProxy3D](geometryproxy3d.md)
  A proxy for access to the size and coordinate space of the container view.
- [func coordinateSpace(NamedCoordinateSpace) -> some View](view/coordinatespace(_:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [enum CoordinateSpace](coordinatespace.md)
  A resolved coordinate space created by the coordinate space protocol.
- [protocol CoordinateSpaceProtocol](coordinatespaceprotocol.md)
  A frame of reference within the layout system.
- [struct PhysicalMetric](physicalmetric.md)
  Provides access to a value in points that corresponds to the specified physical measurement.
- [struct PhysicalMetricsConverter](physicalmetricsconverter.md)
  A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy/reservedregions(kind:options:layoutdirectionbehavior:))*