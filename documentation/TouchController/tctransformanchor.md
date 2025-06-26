# TCTransformAnchor

**Framework**: Touch Controller  
**Kind**: enum

Defines the anchor point for a transform.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum TCTransformAnchor
```

## Topics

### Getting the absolute anchor
- [TCTransformAnchor.absoluteBottomCenter](tctransformanchor/absolutebottomcenter.md)
  Anchors to the bottom-center, using absolute coordinates.
- [TCTransformAnchor.absoluteBottomLeft](tctransformanchor/absolutebottomleft.md)
  Anchors to the bottom-left corner, using absolute coordinates.
- [TCTransformAnchor.absoluteBottomRight](tctransformanchor/absolutebottomright.md)
  Anchors to the bottom-right corner, using absolute coordinates.
- [TCTransformAnchor.absoluteCenter](tctransformanchor/absolutecenter.md)
  Anchors to the center, using absolute coordinates.
- [TCTransformAnchor.absoluteCenterLeft](tctransformanchor/absolutecenterleft.md)
  Anchors to the center-left, using absolute coordinates.
- [TCTransformAnchor.absoluteCenterRight](tctransformanchor/absolutecenterright.md)
  Anchors to the center-right, using absolute coordinates.
- [TCTransformAnchor.absoluteTopCenter](tctransformanchor/absolutetopcenter.md)
  Anchors to the top-center, using absolute coordinates.
- [TCTransformAnchor.absoluteTopLeft](tctransformanchor/absolutetopleft.md)
  Anchors to the top-left corner, using absolute coordinates.
- [TCTransformAnchor.absoluteTopRight](tctransformanchor/absolutetopright.md)
  Anchors to the top-right corner, using absolute coordinates.
### Accessing the bottom anchor
- [TCTransformAnchor.bottomCenter](tctransformanchor/bottomcenter.md)
  Anchors to the bottom-center, relative to the screen size.
- [TCTransformAnchor.bottomLeft](tctransformanchor/bottomleft.md)
  Anchors to the bottom-left corner, relative to the screen size.
- [TCTransformAnchor.bottomRight](tctransformanchor/bottomright.md)
  Anchors to the bottom-right corner, relative to the screen size.
### Retrieving the center anchor
- [TCTransformAnchor.center](tctransformanchor/center.md)
  Anchors to the center, relative to the screen size.
- [TCTransformAnchor.centerLeft](tctransformanchor/centerleft.md)
  Anchors to the center-left, relative to the screen size.
- [TCTransformAnchor.centerRight](tctransformanchor/centerright.md)
  Anchors to the center-right, relative to the screen size.
### Getting the top anchor
- [TCTransformAnchor.topCenter](tctransformanchor/topcenter.md)
  Anchors to the top-center, relative to the screen size.
- [TCTransformAnchor.topLeft](tctransformanchor/topleft.md)
  Anchors to the top-left corner, relative to the screen size.
- [TCTransformAnchor.topRight](tctransformanchor/topright.md)
  Anchors to the top-right corner, relative to the screen size.
### Creating a transform anchor
- [init?(rawValue: Int)](tctransformanchor/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](tctransformanchor/equatable-implementations.md)
- [RawRepresentable Implementations](tctransformanchor/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var anchor: TCTransformAnchor](tcbutton/anchor.md)
  The anchor point that the control’s offset is relative to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctransformanchor)*