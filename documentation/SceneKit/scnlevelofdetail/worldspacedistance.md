# worldSpaceDistance

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The minimum distance from the current point of view for this level of detail to appear.

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
var worldSpaceDistance: CGFloat { get }
```

```objc
@property (readonly) CGFloat worldSpaceDistance;
```

## Discussion

When rendering a geometry with associated levels of detail, SceneKit calculates the distance from the current point of view to the geometry’s parent node, then renders the geometry for the [`SCNLevelOfDetail`](../scnlevelofdetail.md) object with the largest `distance` parameter less than that distance.

## See Also

### Inspecting a Level of Detail
- [var geometry: SCNGeometry?](./geometry.md)
  The geometry associated with this level of detail.
- [var screenSpaceRadius: CGFloat](./screenspaceradius.md)
  The maximum radius (in pixels) of the geometry’s bounding sphere for this level of detail to appear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/worldspacedistance)*