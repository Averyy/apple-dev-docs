# init(geometry:screenSpaceRadius:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a level of detail with the specified geometry and threshold pixel radius.

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
convenience init(geometry: SCNGeometry?, screenSpaceRadius radius: CGFloat)
```

```objc
+ (instancetype) levelOfDetailWithGeometry:(SCNGeometry *) geometry screenSpaceRadius:(CGFloat) radius;
```

## Return Value

A level-of-detail object. You associate levels of detail with a [`SCNGeometry`](../scngeometry.md) object using its [`levelsOfDetail`](../scngeometry/levelsofdetail.md) property.

## Discussion

When rendering a geometry with associated levels of detail, SceneKit calculates the radius in pixels of the circle covered by a geometry’s bounding sphere, then renders the geometry for the [`SCNLevelOfDetail`](../scnlevelofdetail.md) object with the largest `radius` parameter smaller than that circle.

If you pass `nil` for the geometry parameter, SceneKit renders no geometry for the level of detail. Creating a level-of-detail object with no geometry allows you to skip rendering costs entirely for an object when it would appear very far away or very small.

## Parameters

- `geometry`: The geometry to render for this level of detail.
- `radius`: The maximum radius (in pixels) of the geometry’s bounding sphere for this level of detail to appear.

## See Also

### Creating a Level of Detail
- [convenience init(geometry: SCNGeometry?, worldSpaceDistance: CGFloat)](./init%28geometry,worldspacedistance%29.md)
  Creates a level of detail with the specified geometry and threshold camera distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/init(geometry:screenspaceradius:))*