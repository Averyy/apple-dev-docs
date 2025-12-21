# boundingRect(with:options:attributes:context:)

**Framework**: Foundation  
**Kind**: method

Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func boundingRect(with size: CGSize, options: NSString.DrawingOptions = [], attributes: [NSAttributedString.Key : Any]? = nil, context: NSStringDrawingContext?) -> CGRect
```

#### Return Value

The bounding rect for the receiver drawn using the given options and display characteristics. The rect origin returned from this method is the first glyph origin.

#### Discussion

To correctly draw and size multi-line text, pass [`usesLineFragmentOrigin`](https://developer.apple.com/documentation/UIKit/NSStringDrawingOptions/usesLineFragmentOrigin) in the options parameter.

This method returns fractional sizes (in the `size` component of the returned [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect)); to use a returned size to size views, you must raise its value to the nearest higher integer using the [`ceil`](https://developer.apple.com/documentation/kernel/1557272-ceil) function.

This method returns the actual bounds of the glyphs in the string. Some of the glyphs (spaces, for example) are allowed to overlap the layout constraints specified by the size passed in, so in some cases the width value of the size component of the returned [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) can exceed the width value of the `size` parameter.

## Parameters

- `size`: The size of the rectangle to draw in.
- `options`: String drawing options.
- `attributes`: A dictionary of text attributes to be applied to the string. These are the same attributes that can be applied to an   object, but in the case of   objects, the attributes apply to the entire string, rather than ranges within the string.
- `context`: The string drawing context to use for the receiver, specifying minimum scale factor and tracking adjustments.

## See Also

- [func draw(at: CGPoint, withAttributes: [NSAttributedString.Key : Any]?)](nsstring/draw(at:withattributes:).md)
  Draws the receiver with the font and other display characteristics of the given attributes, at the specified point in the current graphics context.
- [func draw(in: CGRect, withAttributes: [NSAttributedString.Key : Any]?)](nsstring/draw(in:withattributes:).md)
  Draws the attributed string inside the specified bounding rectangle.
- [func draw(with: CGRect, options: NSStringDrawingOptions, attributes: [NSAttributedString.Key : Any]?, context: NSStringDrawingContext?)](nsstring/draw(with:options:attributes:context:).md)
  Draws the attributed string in the specified bounding rectangle using the provided options.
- [func size(withAttributes: [NSAttributedString.Key : Any]?) -> CGSize](nsstring/size(withattributes:).md)
  Returns the bounding box size the receiver occupies when drawn with the given attributes.
- [func variantFittingPresentationWidth(Int) -> String](nsstring/variantfittingpresentationwidth(_:).md)
  Returns a string variation suitable for the specified presentation width.
- [struct NSStringDrawingOptions](../UIKit/NSStringDrawingOptions.md)
  Constants that specify the rendering options for drawing a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/boundingrect(with:options:attributes:context:))*