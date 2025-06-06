# beginPage(mediaBox:)

**Framework**: Core Graphics  
**Kind**: method

Starts a new page in a page-based graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func beginPage(mediaBox: UnsafePointer<CGRect>?)
```

#### Discussion

When using a graphics context that supports multiple pages, you should call this function together with [`endPage()`](cgcontext/endpage().md) to delineate the page boundaries in the output. In other words, each page should be bracketed by calls to `CGContextBeginPage` and `CGContextEndPage`. Core Graphics ignores all drawing operations performed outside a page boundary in a page-based context.

## Parameters

- `mediaBox`: A rectangle defining the bounds of the new page, expressed in units of the default user space, or  . These bounds supersede any supplied for the media box when you created the context. If you pass  , Core Graphics uses the rectangle you supplied for the media box when the graphics context was created.

## See Also

- [func endPage()](cgcontext/endpage.md)
  Ends the current page in a page-based graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/beginpage(mediabox:))*