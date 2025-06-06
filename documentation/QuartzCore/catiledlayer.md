# CATiledLayer

**Framework**: Core Animation  
**Kind**: class

A layer that provides a way to asynchronously provide tiles of the layer’s content, potentially cached at multiple levels of detail.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CATiledLayer
```

#### Overview

As more data is required by the renderer, the layer’s [`draw(in:)`](calayer/draw(in:).md) method is called on one or more background threads to supply the drawing operations to fill in one tile of data. The clip bounds and current transformation matrix (CTM) of the drawing context can be used to determine the bounds and resolution of the tile being requested.

Regions of the layer may be invalidated using the [`setNeedsDisplay(_:)`](calayer/setneedsdisplay(_:).md) method however the update will be asynchronous. While the next display update will most likely not contain the updated content, a future update will.

> ❗ **Important**:  Do not attempt to directly modify the [`contents`](calayer/contents.md) property of a [`CATiledLayer`](catiledlayer.md) object. Doing so disables the ability of a tiled layer to asynchronously provide tiled content, effectively turning the layer into a regular [`CALayer`](calayer.md) object.

 Do not attempt to directly modify the [`contents`](calayer/contents.md) property of a [`CATiledLayer`](catiledlayer.md) object. Doing so disables the ability of a tiled layer to asynchronously provide tiled content, effectively turning the layer into a regular [`CALayer`](calayer.md) object.

## Topics

### Visual Fade
- [class func fadeDuration() -> CFTimeInterval](catiledlayer/fadeduration.md)
  The time, in seconds, that newly added images take to “fade-in” to the rendered representation of the tiled layer.
### Levels of detail
- [var levelsOfDetail: Int](catiledlayer/levelsofdetail.md)
  The number of levels of detail maintained by this layer.
- [var levelsOfDetailBias: Int](catiledlayer/levelsofdetailbias.md)
  The number of magnified levels of detail for this layer.
### Layer tile size
- [var tileSize: CGSize](catiledlayer/tilesize.md)
  The maximum size of each tile used to create the layer’s content.

## Relationships

### Inherits From
- [CALayer](calayer.md)
### Conforms To
- [CAMediaTiming](camediatiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CAScrollLayer](cascrolllayer.md)
  A layer that displays scrollable content larger than its own bounds.
- [class CATransformLayer](catransformlayer.md)
  Objects used to create true 3D layer hierarchies, rather than the flattened hierarchy rendering model used by other layer types.
- [class CAReplicatorLayer](careplicatorlayer.md)
  A layer that creates a specified number of sublayer copies with varying geometric, temporal, and color transformations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catiledlayer)*