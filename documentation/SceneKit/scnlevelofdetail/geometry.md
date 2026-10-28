# geometry

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The geometry associated with this level of detail.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var geometry: SCNGeometry? { get }
```

```objc
@property (readonly, nullable) SCNGeometry * geometry;
```

## Discussion

SceneKit renders this geometry instead of the original geometry when the level of detail is appropriate. Generally, levels of detail with larger [`worldSpaceDistance`](./worldspacedistance.md) values or smaller [`screenSpaceRadius`](./screenspaceradius.md) values should contain less complex geometries.

If the value of this property is `nil`, SceneKit renders no geometry at this level of detail.

## See Also

### Inspecting a Level of Detail
- [var screenSpaceRadius: CGFloat](./screenspaceradius.md)
  The maximum radius (in pixels) of the geometry’s bounding sphere for this level of detail to appear.
- [var worldSpaceDistance: CGFloat](./worldspacedistance.md)
  The minimum distance from the current point of view for this level of detail to appear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/geometry)*