# endPage()

**Framework**: AppKit  
**Kind**: method

Writes the end of a conforming page.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func endPage()
```

#### Discussion

This method is invoked after each page is printed. It invokes [`unlockFocus()`](nsview/unlockfocus().md). This method also generates comments for the bounding box and page fonts, if they were specified as being at the end of the page.

## See Also

- [func beginDocument()](nsview/begindocument.md)
  Invoked at the beginning of the printing session, this method sets up the current graphics context.
- [func endDocument()](nsview/enddocument.md)
  This method is invoked at the end of the printing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/endpage())*