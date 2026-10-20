# size(withAttributes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the bounding box size the receiver occupies when drawn with the given attributes.

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
func size(withAttributes attrs: [NSAttributedString.Key : Any]? = nil) -> CGSize
```

```objc
- (CGSize) sizeWithAttributes:(NSDictionary<NSString *,id> *) attrs;
```

#### Return Value

The bounding box size the receiver occupies when drawn with the specified attributes.

#### Discussion

This method returns fractional sizes; to use a returned size to size views, you must raise its value to the nearest higher integer using the [`ceil`](../../kernel/api-1557272-ceil.md) function.

## Parameters

- `attrs`: A dictionary of text attributes to be applied to the string. These are the same attributes that can be applied to an `NSAttributedString` object, but in the case of `NSString` objects, the attributes apply to the entire string, rather than ranges within the string.

## See Also

### Sizing and Drawing Strings
- [func draw(at: CGPoint, withAttributes: [NSAttributedString.Key : Any]?)](./draw%28at,withattributes%29.md)
  Draws the receiver with the font and other display characteristics of the given attributes, at the specified point in the current graphics context.
- [func draw(in: CGRect, withAttributes: [NSAttributedString.Key : Any]?)](./draw%28in,withattributes%29.md)
  Draws the attributed string inside the specified bounding rectangle.
- [func draw(with: CGRect, options: NSStringDrawingOptions, attributes: [NSAttributedString.Key : Any]?, context: NSStringDrawingContext?)](./draw%28with,options,attributes,context%29.md)
  Draws the attributed string in the specified bounding rectangle using the provided options.
- [func boundingRect(with: CGSize, options: NSStringDrawingOptions, attributes: [NSAttributedString.Key : Any]?, context: NSStringDrawingContext?) -> CGRect](./boundingrect%28with,options,attributes,context%29.md)
  Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.
- [func variantFittingPresentationWidth(Int) -> String](./variantfittingpresentationwidth%28_%29.md)
  Returns a string variation suitable for the specified presentation width.
- [struct NSStringDrawingOptions](../../UIKit/nsstringdrawingoptions.md)
  Constants that specify the rendering options for drawing a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/size(withattributes:))*