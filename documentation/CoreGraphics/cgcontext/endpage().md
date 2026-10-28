# endPage()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Ends the current page in a page-based graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func endPage()
```

```c
extern void CGContextEndPage(CGContextRef c);
```

## Discussion

When using a graphics context that supports multiple pages, you should call this function to terminate drawing in the current page.

## See Also

### Managing a Page-Based Graphics Context
- [func beginPage(mediaBox: UnsafePointer<CGRect>?)](./beginpage%28mediabox%29.md)
  Starts a new page in a page-based graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/endpage())*