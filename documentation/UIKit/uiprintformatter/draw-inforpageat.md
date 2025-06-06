# draw(in:forPageAt:)

**Framework**: UIKit  
**Kind**: method

Draws the portion of a print formatter’s content for the specified area of the specified page.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func draw(in rect: CGRect, forPageAt pageIndex: Int)
```

#### Discussion

This method is called by the default implementation of `drawPrintFormatter:forPageAtIndex:` of the [`UIPrintPageRenderer`](uiprintpagerenderer.md) class for each print formatter associated with a page.

## Parameters

- `rect`: The area in which to draw the content.
- `pageIndex`: The number of the page of content to draw.

## See Also

- [func rectForPage(at: Int) -> CGRect](uiprintformatter/rectforpage(at:).md)
  Returns the area that encloses a specified page of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/draw(in:forpageat:))*