# CAScrollLayer

**Framework**: Core Animation  
**Kind**: class

A layer that displays scrollable content larger than its own bounds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CAScrollLayer
```

#### Overview

The [`CAScrollLayer`](cascrolllayer.md) class is a subclass of [`CALayer`](calayer.md) that simplifies displaying a portion of a layer. The extent of the scrollable area of the [`CAScrollLayer`](cascrolllayer.md) is defined by the layout of its sublayers. The visible portion of the layer content is set by specifying the origin as a point or a rectangular area of the contents to be displayed. [`CAScrollLayer`](cascrolllayer.md) does not provide keyboard or mouse event-handling, nor does it provide visible scrollers.

## Topics

### Scrolling constraints
- [var scrollMode: CAScrollLayerScrollMode](cascrolllayer/scrollmode.md)
  Defines the axes in which the layer may be scrolled.
### Scrolling the layer
- [func scroll(to: CGPoint)](cascrolllayer/scroll(to:)-37q0p.md)
  Changes the origin of the receiver to the specified point.
- [func scroll(to: CGRect)](cascrolllayer/scroll(to:)-782vd.md)
  Scroll the contents of the receiver to ensure that the rectangle is visible.
### Constants
- [Scroll Modes](scroll-modes.md)
  These constants describe the supported scroll modes used by the [`scrollMode`](cascrolllayer/scrollmode.md) property.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CATiledLayer](catiledlayer.md)
  A layer that provides a way to asynchronously provide tiles of the layer’s content, potentially cached at multiple levels of detail.
- [class CATransformLayer](catransformlayer.md)
  Objects used to create true 3D layer hierarchies, rather than the flattened hierarchy rendering model used by other layer types.
- [class CAReplicatorLayer](careplicatorlayer.md)
  A layer that creates a specified number of sublayer copies with varying geometric, temporal, and color transformations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cascrolllayer)*