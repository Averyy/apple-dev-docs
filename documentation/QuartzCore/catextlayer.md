# CATextLayer

**Framework**: Core Animation  
**Kind**: class

A layer that provides simple text layout and rendering of plain or attributed strings.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CATextLayer
```

#### Overview

The first line is aligned to the top of the layer.

> **Note**:  `CATextLayer` disables sub-pixel antialiasing when rendering text. Text can only be drawn using sub-pixel antialiasing when it is composited into an existing opaque background at the same time that it’s rasterized. There is no way to draw text with sub-pixel antialiasing by itself, whether into an image or a layer, in advance of having the background pixels to weave the text pixels into. Setting the `opacity` property of the layer to [`true`](https://developer.apple.com/documentation/Swift/true) does not change the rendering mode.

> **Note**:  In macOS, when a `CATextLayer` instance is positioned using the [`CAConstraintLayoutManager`](caconstraintlayoutmanager.md) class the bounds of the layer is resized to fit the text content.

## Topics

### Getting and Setting the Text
- [var string: Any?](catextlayer/string.md)
  The text to be rendered by the receiver.
### Text Visual Properties
- [var font: CFTypeRef?](catextlayer/font.md)
  The font used to render the receiver’s text.
- [var fontSize: CGFloat](catextlayer/fontsize.md)
  The font size used to render the receiver’s text. Animatable.
- [var foregroundColor: CGColor?](catextlayer/foregroundcolor.md)
  The color used to render the receiver’s text. Animatable.
- [var allowsFontSubpixelQuantization: Bool](catextlayer/allowsfontsubpixelquantization.md)
  Determines whether to allow subpixel quantization for the graphics context used for text rendering.
### Text Alignment and Truncation
- [var isWrapped: Bool](catextlayer/iswrapped.md)
  Determines whether the text is wrapped to fit within the receiver’s bounds.
- [var alignmentMode: CATextLayerAlignmentMode](catextlayer/alignmentmode.md)
  Determines how individual lines of text are horizontally aligned within the receiver’s bounds.
- [var truncationMode: CATextLayerTruncationMode](catextlayer/truncationmode.md)
  Determines how the text is truncated to fit within the receiver’s bounds.
### Constants
- [Truncation modes](truncation-modes.md)
  These constants are used by the [`truncationMode`](catextlayer/truncationmode.md) property.
- [Horizontal alignment modes](horizontal-alignment-modes.md)
  These constants are used by the [`alignmentMode`](catextlayer/alignmentmode.md) property.

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

- [class CAShapeLayer](cashapelayer.md)
  A layer that draws a cubic Bezier spline in its coordinate space.
- [class CAGradientLayer](cagradientlayer.md)
  A layer that draws a color gradient over its background color, filling the shape of the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catextlayer)*