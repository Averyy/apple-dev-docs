# beginDocument()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked at the beginning of the printing session, this method sets up the current graphics context.

**Availability**:
- macOS

## Declaration

```swift
func beginDocument()
```

```objc
- (void) beginDocument;
```

## Discussion

Note that this method may be invoked in a subthread.

Override it to configure printing related settings. You should store your settings in the object returned by `NSPrintInfo`’s [`shared`](../nsprintinfo/shared.md) class method, which is guaranteed to return an instance specific to the thread in which you invoke this method. If you override this method, call the superclass implementation.

## See Also

### Writing Conforming Rendering Instructions
- [func endDocument()](./enddocument%28%29.md)
  This method is invoked at the end of the printing session.
- [func endPage()](./endpage%28%29.md)
  Writes the end of a conforming page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/begindocument())*