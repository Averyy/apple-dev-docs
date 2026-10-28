# SCNLevelOfDetail

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

An alternate resolution for a geometry that SceneKit automatically substitutes to improve rendering performance.

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
class SCNLevelOfDetail
```

```objc
@interface SCNLevelOfDetail : NSObject
```

## Overview

You use level-of-detail objects when you have a detailed geometry that appears at several apparent sizes in a scene. For example, the teapot model on the the left in the figure below has 256 polygons, the model at center has 1024 polygons, and the model on the right has 14,400 polygons. If all three models appear close to the camera, filling most of the rendered view, the difference in detail between them is clearly visible—but if they appear far away, taking up a small area of the view, the difference is much less obvious. Rendering higher-resolution geometries incurs a higher performance cost.

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2929784@2x.png)

When you associate one or more level-of-detail objects with a [`SCNGeometry`](./scngeometry.md) object using its [`levelsOfDetail`](./scngeometry/levelsofdetail.md) property, SceneKit automatically substitutes alternate geometries when appropriate. For example, the two lower-resolution teapot models seen above can be added as levels of detail for the high-resolution model.

For each level of detail, you specify either a world-space distance or a screen-space radius. The measure you specify determines the threshold where SceneKit automatically renders that level of detail’s alternate geometry instead of the original geometry. If you specify a distance, the alternate geometry appears when the node containing the geometry is moved that distance away from the camera. If you specify a radius, the alternate geometry appears when the pixel area covered by the rendered geometry is smaller than a circle of that radius.

The geometries associated with lower levels of detail need not share all attributes of the original geometry. For example, you can use different materials for levels of detail that only appear when far away from the camera, disabling expensive features such as per-pixel lighting, reflection mapping, or custom shader programs.

## Topics

### Creating a Level of Detail
- [convenience init(geometry: SCNGeometry?, screenSpaceRadius: CGFloat)](./scnlevelofdetail/init%28geometry,screenspaceradius%29.md)
  Creates a level of detail with the specified geometry and threshold pixel radius.
- [convenience init(geometry: SCNGeometry?, worldSpaceDistance: CGFloat)](./scnlevelofdetail/init%28geometry,worldspacedistance%29.md)
  Creates a level of detail with the specified geometry and threshold camera distance.
### Inspecting a Level of Detail
- [var geometry: SCNGeometry?](./scnlevelofdetail/geometry.md)
  The geometry associated with this level of detail.
- [var screenSpaceRadius: CGFloat](./scnlevelofdetail/screenspaceradius.md)
  The maximum radius (in pixels) of the geometry’s bounding sphere for this level of detail to appear.
- [var worldSpaceDistance: CGFloat](./scnlevelofdetail/worldspacedistance.md)
  The minimum distance from the current point of view for this level of detail to appear.
### Initializers
- [init?(coder: NSCoder)](./scnlevelofdetail/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Optimizing Level of Detail
- [var levelsOfDetail: [SCNLevelOfDetail]?](./scngeometry/levelsofdetail.md)
  An array of [`SCNLevelOfDetail`](./scnlevelofdetail.md) objects for managing the geometry’s appearance when viewed from far away.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlevelofdetail)*