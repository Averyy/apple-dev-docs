# SCNChamferMode

**Framework**: SceneKit  
**Kind**: enum

Options for which edges of an extruded shape are chamfered, used by the [`chamferMode`](scnshape/chamfermode.md) property.

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
enum SCNChamferMode
```

#### Overview

![None](https://docs-assets.developer.apple.com/published/1bd46a3942a3db81cff2295284beab48/media-2929773%402x.png)

## Topics

### Constants
- [SCNChamferMode.both](scnchamfermode/both.md)
  Apply a chamfer to both front and back edges of the extruded shape.
- [SCNChamferMode.front](scnchamfermode/front.md)
  Apply a chamfer to only the front edge of the extruded shape.
- [SCNChamferMode.back](scnchamfermode/back.md)
  Apply a chamfer to only the back edge of the extruded shape.
### Initializers
- [init?(rawValue: Int)](scnchamfermode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var chamferMode: SCNChamferMode](scnshape/chamfermode.md)
  A constant specifying which ends of the extruded shape’s profile are chamfered.
- [var chamferProfile: UIBezierPath?](scnshape/chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.
- [var chamferRadius: CGFloat](scnshape/chamferradius.md)
  The width or depth of each chamfered edge. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnchamfermode)*