# screenSpaceRadius

**Framework**: SceneKit  
**Kind**: property

The maximum radius (in pixels) of the geometry’s bounding sphere for this level of detail to appear.

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
var screenSpaceRadius: CGFloat { get }
```

#### Discussion

When rendering a geometry with associated levels of detail, SceneKit calculates the radius in pixels of the circle covered by a geometry’s bounding sphere, then renders the geometry for the [`SCNLevelOfDetail`](scnlevelofdetail.md) object with the smallest `radius` parameter larger than that circle.

## See Also

- [var geometry: SCNGeometry?](scnlevelofdetail/geometry.md)
  The geometry associated with this level of detail.
- [var worldSpaceDistance: CGFloat](scnlevelofdetail/worldspacedistance.md)
  The minimum distance from the current point of view for this level of detail to appear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/screenspaceradius)*