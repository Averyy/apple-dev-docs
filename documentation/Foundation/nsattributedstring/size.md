# size()

**Framework**: Foundation  
**Kind**: method

Returns the size necessary to draw the string.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func size() -> CGSize
```

#### Return Value

The minimum size required to draw the entire contents of the string.

#### Discussion

You can use this method prior to drawing to compute how much space is required to draw the string.

This method may return fractional sizes. When setting the size of your view, use the [`ceil`](https://developer.apple.com/documentation/kernel/1557272-ceil) function to round fractional values up to the nearest whole number.

## See Also

- [func draw(at: CGPoint)](nsattributedstring/draw(at:).md)
  Draws the attributed string starting at the specified point in the current graphics context.
- [func draw(in: CGRect)](nsattributedstring/draw(in:).md)
  Draws the attributed string inside the specified bounding rectangle in the current graphics context.
- [func boundingRect(with: CGSize, options: NSStringDrawingOptions, context: NSStringDrawingContext?) -> CGRect](nsattributedstring/boundingrect(with:options:context:).md)
  Returns the bounding rectangle necessary to draw the string.
- [func containsAttachments(in: NSRange) -> Bool](nsattributedstring/containsattachments(in:).md)
  Returns a Boolean value that indicates if the attributed string contains an attachment in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/size())*