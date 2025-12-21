# segmentCount

**Framework**: SceneKit  
**Kind**: property

A number determining the detail of the polygon mesh SceneKit uses to render the sphere. Animatable.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var segmentCount: Int { get set }
```

#### Discussion

If the sphere’s [`isGeodesic`](scnsphere/isgeodesic.md) property is [`false`](https://developer.apple.com/documentation/Swift/false), its segment count determines the number of subdivisions along its polar and azimuth angles, similar to the latitude and longitude system on a globe of the Earth. For example, if the segment count is `24`, the circular horizontal cross section through the center of the sphere has 24 segments around its circumference, and a semicircle reaching from one pole to another through a vertical cross section also has 24 segments.

If the sphere’s [`isGeodesic`](scnsphere/isgeodesic.md) property is [`true`](https://developer.apple.com/documentation/Swift/true), SceneKit creates the sphere’s surface by successively subdividing the faces of an icosahedron (or twenty-sided polyhedron). Each subdivision quadruples the number of polygons in the surface. The number of subdivisions increases logarithmically with the segment count, so that the total number of polygons or vertices for a geodesic sphere is similar to that for a non-geodesic sphere of the same segment count.

The default segment count is `48`. Setting this property’s value to a number less than `3` results in undefined behavior.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var isGeodesic: Bool](scnsphere/isgeodesic.md)
  A Boolean value specifying whether SceneKit uses a geodesic polygon mesh to render the sphere.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnsphere/segmentcount)*