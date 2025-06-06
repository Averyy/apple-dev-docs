# geometry

**Framework**: SceneKit  
**Kind**: property

The geometry associated with this level of detail.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var geometry: SCNGeometry? { get }
```

#### Discussion

SceneKit renders this geometry instead of the original geometry when the level of detail is appropriate. Generally, levels of detail with larger [`worldSpaceDistance`](scnlevelofdetail/worldspacedistance.md) values or smaller [`screenSpaceRadius`](scnlevelofdetail/screenspaceradius.md) values should contain less complex geometries.

If the value of this property is `nil`, SceneKit renders no geometry at this level of detail.

## See Also

- [var screenSpaceRadius: CGFloat](scnlevelofdetail/screenspaceradius.md)
  The maximum radius (in pixels) of the geometry’s bounding sphere for this level of detail to appear.
- [var worldSpaceDistance: CGFloat](scnlevelofdetail/worldspacedistance.md)
  The minimum distance from the current point of view for this level of detail to appear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/geometry)*