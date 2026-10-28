# endDocument()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This method is invoked at the end of the printing session.

**Availability**:
- macOS

## Declaration

```swift
func endDocument()
```

```objc
- (void) endDocument;
```

## Discussion

If you override this method, call the superclass implementation.

## See Also

### Writing Conforming Rendering Instructions
- [func beginDocument()](./begindocument%28%29.md)
  Invoked at the beginning of the printing session, this method sets up the current graphics context.
- [func endPage()](./endpage%28%29.md)
  Writes the end of a conforming page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/enddocument())*