# endDocument()

**Framework**: AppKit  
**Kind**: method

This method is invoked at the end of the printing session.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func endDocument()
```

#### Discussion

If you override this method, call the superclass implementation.

## See Also

- [func beginDocument()](nsview/begindocument.md)
  Invoked at the beginning of the printing session, this method sets up the current graphics context.
- [func endPage()](nsview/endpage.md)
  Writes the end of a conforming page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/enddocument())*