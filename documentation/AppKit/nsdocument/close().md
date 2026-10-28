# close()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Closes all of the document’s windows and removes the document from its document controller.

**Availability**:
- macOS

## Declaration

```swift
func close()
```

```objc
- (void) close;
```

## Discussion

This method closes the document immediately, without asking users if they want to save the document. This method may not always be called.

## See Also

### Related Documentation
- [func shouldCloseWindowController(NSWindowController, delegate: Any?, shouldClose: Selector?, contextInfo: UnsafeMutableRawPointer?)](./shouldclosewindowcontroller%28_,delegate,shouldclose,contextinfo%29.md)
  Determines whether the system should close the document and its associated window.
### Closing the Document
- [func canClose(withDelegate: Any, shouldClose: Selector?, contextInfo: UnsafeMutableRawPointer?)](./canclose%28withdelegate,shouldclose,contextinfo%29.md)
  Determines whether to close the document, prompting the user as needed to choose a course of action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/close())*