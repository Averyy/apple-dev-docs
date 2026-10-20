# endPage()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the end of a conforming page.

**Availability**:
- macOS

## Declaration

```swift
func endPage()
```

```objc
- (void) endPage;
```

#### Discussion

This method is invoked after each page is printed. It invokes [`unlockFocus()`](./unlockfocus%28%29.md). This method also generates comments for the bounding box and page fonts, if they were specified as being at the end of the page.

## See Also

### Writing Conforming Rendering Instructions
- [func beginDocument()](./begindocument%28%29.md)
  Invoked at the beginning of the printing session, this method sets up the current graphics context.
- [func endDocument()](./enddocument%28%29.md)
  This method is invoked at the end of the printing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/endpage())*