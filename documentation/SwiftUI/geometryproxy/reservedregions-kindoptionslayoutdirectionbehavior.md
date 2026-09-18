# reservedRegions(kind:options:layoutDirectionBehavior:)

**Framework**: SwiftUI  
**Kind**: method

Returns an array of reserved regions that match the selection options you specify.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
func reservedRegions(kind: ReservedRegion.Kind, options: ReservedRegion.QueryOptions = [], layoutDirectionBehavior: LayoutDirectionBehavior = .mirrors) -> [ReservedRegion]
```

#### Discussion

A reserved region indicates an area within a view’s coordinate space that an entity, such as the device hardware, reserves. Arrange the view’s content to account for this region. Each region describes a frame, margins, active state, and an identifier.

There are two categories of reserved regions:

- **[`occlusion`](reservedregion/kind-swift.struct/occlusion.md)**: An area where an element, such as the Dynamic Island, a camera, or window controls, occludes content.
- **[`division`](reservedregion/kind-swift.struct/division.md)**: An area where content splits into separate regions, such as at the fold of a hinge.

Read reserved regions using the [`reservedRegions(kind:options:layoutDirectionBehavior:)`](geometryproxy/reservedregions(kind:options:layoutdirectionbehavior:).md) method, which returns all of the reserved regions that currently intersect your view regardless of whether they are currently active.

In the example below, a custom [`Layout`](layout.md) uses the reserved regions from a [`GeometryProxy`](geometryproxy.md) instance to handle positioning its subviews away from any regions that intersect it.

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

When you manually position your content to incorporate reserved regions, take care to consider right-to-left layout directions. Reserved regions are typically in a fixed coordinate space; the absolute location of the camera of a device doesn’t flip depending on a person’s preferred language. By default, the system mirrors the geometry of these regions automatically before it provides them to SwiftUI APIs.

For example, a [`Layout`](layout.md) automatically flips the geometry of the subviews you place. By mirroring the geometry of the reserved regions, your layout doesn’t need to account for the layout direction when determining whether a subview intersects the region.

There may be cases when you need to make more manual adjustments for the frames of reserved regions for right-to-left layout directions. In these cases, you can provide the [`LayoutDirectionBehavior.fixed`](layoutdirectionbehavior/fixed.md) value to the method and the system doesn’t mirror the frames of the regions.

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