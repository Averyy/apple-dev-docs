# ARImageAnchor

**Framework**: ARKit  
**Kind**: class

An anchor for a known image that ARKit detects in the physical environment.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARImageAnchor
```

#### Overview

When you run a world-tracking AR session and specify [`ARReferenceImage`](arreferenceimage.md) objects for the session configuration’s [`detectionImages`](arworldtrackingconfiguration/detectionimages.md) property, ARKit searches for those images in the real-world environment. When the session recognizes an image, it automatically adds an [`ARImageAnchor`](arimageanchor.md) for each detected image to its list of anchors.

To find the extent of a recognized image in the scene, use the inherited [`transform`](aranchor/transform.md) property together with the [`physicalSize`](arreferenceimage/physicalsize.md) of the anchor’s [`referenceImage`](arimageanchor/referenceimage.md).

## Topics

### Identifying Detected Images
- [var referenceImage: ARReferenceImage](arimageanchor/referenceimage.md)
  The detected image referenced by the image anchor.
### Estimating Scale
- [var estimatedScaleFactor: CGFloat](arimageanchor/estimatedscalefactor.md)
  A factor between the initial size and the estimated physical size.

## Relationships

### Inherits From
- [ARAnchor](aranchor.md)
### Conforms To
- [ARAnchorCopying](aranchorcopying.md)
- [ARTrackable](artrackable.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Tracking and altering images](tracking-and-altering-images.md)
  Create images from rectangular shapes found in the user’s environment, and augment their appearance.
- [Detecting Images in an AR Experience](detecting-images-in-an-ar-experience.md)
  React to known 2D images in the user’s environment, and use their positions to place AR content.
- [class ARReferenceImage](arreferenceimage.md)
  A 2D image that you want ARKit to detect in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arimageanchor)*