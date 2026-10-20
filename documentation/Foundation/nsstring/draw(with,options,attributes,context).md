# draw(with:options:attributes:context:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Draws the attributed string in the specified bounding rectangle using the provided options.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
func draw(with rect: CGRect, options: NSStringDrawingOptions = [], attributes: [NSAttributedString.Key : Any]? = nil, context: NSStringDrawingContext?)
```

*macOS*

```swift
func draw(with rect: CGRect, options: NSString.DrawingOptions = [], attributes: [NSAttributedString.Key : Any]? = nil, context: NSStringDrawingContext?)
```

```objc
- (void) drawWithRect:(CGRect) rect options:(NSStringDrawingOptions) options attributes:(NSDictionary<NSString *,id> *) attributes context:(NSStringDrawingContext *) context;
```

#### Discussion

This method draws as much of the string as it can inside the specified rectangle, wrapping the string text as needed to make it fit. If the string is too big to fit completely inside the rectangle, the method scales the font or adjusts the letter spacing to make the string fit within the given bounds.

If newline characters are present in the string, those characters are honored and cause subsequent text to be placed on the next line underneath the starting point. To correctly draw and size multi-line text, pass [`usesLineFragmentOrigin`](../../UIKit/nsstringdrawingoptions/useslinefragmentorigin.md) in the options parameter.

##### Special Considerations

This method uses the baseline origin by default.

If [`usesLineFragmentOrigin`](../../UIKit/nsstringdrawingoptions/useslinefragmentorigin.md) is not specified, the rectangle’s height will be ignored and the operation considered to be single-line rendering.

## Parameters

- `rect`: The bounding rectangle in which to draw the string.
- `options`: Additional drawing options to apply to the string during rendering. For a list of possible values, see [`NSStringDrawingOptions`](../../UIKit/nsstringdrawingoptions.md).
- `attributes`: The text attributes with which to draw the string. These are the same attributes that can be applied to an `NSAttributedString` object, but in the case of `NSString` objects, the attributes apply to the entire string, rather than ranges within the string.
- `context`: A context object with information about how to adjust the font tracking and scaling information. On return, the specified object contains information about the actual values used to render the string. This parameter may be `nil`.

## See Also

### Sizing and Drawing Strings
- [func draw(at: CGPoint, withAttributes: [NSAttributedString.Key : Any]?)](./draw%28at,withattributes%29.md)
  Draws the receiver with the font and other display characteristics of the given attributes, at the specified point in the current graphics context.
- [func draw(in: CGRect, withAttributes: [NSAttributedString.Key : Any]?)](./draw%28in,withattributes%29.md)
  Draws the attributed string inside the specified bounding rectangle.
- [func boundingRect(with: CGSize, options: NSStringDrawingOptions, attributes: [NSAttributedString.Key : Any]?, context: NSStringDrawingContext?) -> CGRect](./boundingrect%28with,options,attributes,context%29.md)
  Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.
- [func size(withAttributes: [NSAttributedString.Key : Any]?) -> CGSize](./size%28withattributes%29.md)
  Returns the bounding box size the receiver occupies when drawn with the given attributes.
- [func variantFittingPresentationWidth(Int) -> String](./variantfittingpresentationwidth%28_%29.md)
  Returns a string variation suitable for the specified presentation width.
- [struct NSStringDrawingOptions](../../UIKit/nsstringdrawingoptions.md)
  Constants that specify the rendering options for drawing a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/draw(with:options:attributes:context:))*