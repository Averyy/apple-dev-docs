# SCNChamferMode

**Framework**: SceneKit  
**Kind**: enum

Options for which edges of an extruded shape are chamfered, used by the [`chamferMode`](scnshape/chamfermode.md) property.

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
enum SCNChamferMode
```

#### Overview

![None](/images/com.apple.scenekit/media-2929773@2x.png)

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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var chamferMode: SCNChamferMode](scnshape/chamfermode.md)
  A constant specifying which ends of the extruded shape’s profile are chamfered.
- [var chamferProfile: UIBezierPath?](scnshape/chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.
- [var chamferRadius: CGFloat](scnshape/chamferradius.md)
  The width or depth of each chamfered edge. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnchamfermode)*