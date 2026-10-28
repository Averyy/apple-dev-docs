# size()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (CGSize) size;
```

## Return Value

The minimum size required to draw the entire contents of the string.

## Discussion

You can use this method prior to drawing to compute how much space is required to draw the string.

This method may return fractional sizes. When setting the size of your view, use the [`ceil`](../../kernel/api-1557272-ceil.md) function to round fractional values up to the nearest whole number.

## See Also

### Related Documentation
- [func draw(at: CGPoint)](./draw%28at%29.md)
  Draws the attributed string starting at the specified point in the current graphics context.
- [func draw(in: CGRect)](./draw%28in%29.md)
  Draws the attributed string inside the specified bounding rectangle in the current graphics context.
### Getting metrics for the string
- [func boundingRect(with: CGSize, options: NSStringDrawingOptions, context: NSStringDrawingContext?) -> CGRect](./boundingrect%28with,options,context%29.md)
  Returns the bounding rectangle necessary to draw the string.
- [func containsAttachments(in: NSRange) -> Bool](./containsattachments%28in%29.md)
  Returns a Boolean value that indicates if the attributed string contains an attachment in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/size())*