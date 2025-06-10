# draw(at:withAttributes:)

**Framework**: Foundation  
**Kind**: method

Draws the receiver with the font and other display characteristics of the given attributes, at the specified point in the current graphics context.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func draw(at point: CGPoint, withAttributes attrs: [NSAttributedString.Key : Any]? = nil)
```

#### Discussion

The width (height for vertical layout) of the rendering area is unlimited, unlike [`draw(in:withAttributes:)`](nsstring/draw(in:withattributes:).md), which uses a bounding rectangle. As a result, this method renders the text in a single line. However, if newline characters are present in the string, those characters are honored and cause subsequent text to be placed on the next line underneath the starting point.

There must be either a focused view or an active graphics context when you call this method.

## Parameters

- `point`: The point in the current graphics context where you want to start drawing the string. The coordinate system of the graphics context is usually defined by the view in which you are drawing. In AppKit, the origin is normally in the lower-left corner of the drawing area, but the origin is in the upper-left corner if the focused view is flipped.
- `attrs`: A dictionary of text attributes to be applied to the string. These are the same attributes that can be applied to an   object, but in the case of   objects, the attributes apply to the entire string, rather than ranges within the string.

## See Also

- [func draw(in: CGRect, withAttributes: [NSAttributedString.Key : Any]?)](nsstring/draw(in:withattributes:).md)
  Draws the attributed string inside the specified bounding rectangle.
- [func draw(with: CGRect, options: NSStringDrawingOptions, attributes: [NSAttributedString.Key : Any]?, context: NSStringDrawingContext?)](nsstring/draw(with:options:attributes:context:).md)
  Draws the attributed string in the specified bounding rectangle using the provided options.
- [func boundingRect(with: CGSize, options: NSStringDrawingOptions, attributes: [NSAttributedString.Key : Any]?, context: NSStringDrawingContext?) -> CGRect](nsstring/boundingrect(with:options:attributes:context:).md)
  Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.
- [func size(withAttributes: [NSAttributedString.Key : Any]?) -> CGSize](nsstring/size(withattributes:).md)
  Returns the bounding box size the receiver occupies when drawn with the given attributes.
- [func variantFittingPresentationWidth(Int) -> String](nsstring/variantfittingpresentationwidth(_:).md)
  Returns a string variation suitable for the specified presentation width.
- [struct NSStringDrawingOptions](../UIKit/NSStringDrawingOptions.md)
  Constants that specify the rendering options for drawing a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/draw(at:withattributes:))*