# init(geometry:worldSpaceDistance:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a level of detail with the specified geometry and threshold camera distance.

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
convenience init(geometry: SCNGeometry?, worldSpaceDistance distance: CGFloat)
```

```objc
+ (instancetype) levelOfDetailWithGeometry:(SCNGeometry *) geometry worldSpaceDistance:(CGFloat) distance;
```

#### Return Value

A level-of-detail object. You associate levels of detail with a [`SCNGeometry`](../scngeometry.md) object using its [`levelsOfDetail`](../scngeometry/levelsofdetail.md) property.

#### Discussion

When rendering a geometry with associated levels of detail, SceneKit calculates the distance from the current point of view to the geometry’s parent node, then renders the geometry for the [`SCNLevelOfDetail`](../scnlevelofdetail.md) object with the smallest `distance` parameter greater than that distance.

If you pass `nil` for the geometry parameter, SceneKit renders no geometry for the level of detail. Creating a level-of-detail object with no geometry allows you to skip rendering costs entirely for an object when it would appear very far away or very small.

## Parameters

- `geometry`: The geometry to render for this level of detail, or `nil` if SceneKit should render no geometry at this level of detail.
- `distance`: The minimum distance from the current point of view for this level of detail to appear.

## See Also

### Creating a Level of Detail
- [convenience init(geometry: SCNGeometry?, screenSpaceRadius: CGFloat)](./init%28geometry,screenspaceradius%29.md)
  Creates a level of detail with the specified geometry and threshold pixel radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/init(geometry:worldspacedistance:))*