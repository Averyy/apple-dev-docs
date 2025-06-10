# rectForPage(at:)

**Framework**: UIKit  
**Kind**: method

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

#### Return Value

A rectangle enclosing the content area for page `pageIndex`.

#### Discussion

Returns [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero) if the print formatter draws no content on the specified page.

## Parameters

- `pageIndex`: The index number of a page.

## See Also

- [func draw(in: CGRect, forPageAt: Int)](uiprintformatter/draw(in:forpageat:).md)
  Draws the portion of a print formatter’s content for the specified area of the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/rectforpage(at:))*