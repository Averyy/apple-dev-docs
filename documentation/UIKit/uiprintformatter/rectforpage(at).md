# rectForPage(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the area that encloses a specified page of content.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func rectForPage(at pageIndex: Int) -> CGRect
```

```objc
- (CGRect) rectForPageAtIndex:(NSInteger) pageIndex;
```

## Return Value

A rectangle enclosing the content area for page `pageIndex`.

## Discussion

Returns [`CGRectZero`](../../CoreGraphics/cgrectzero.md) if the print formatter draws no content on the specified page.

## Parameters

- `pageIndex`: The index number of a page.

## See Also

### Drawing the content
- [func draw(in: CGRect, forPageAt: Int)](./draw%28in,forpageat%29.md)
  Draws the portion of a print formatter’s content for the specified area of the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/rectforpage(at:))*