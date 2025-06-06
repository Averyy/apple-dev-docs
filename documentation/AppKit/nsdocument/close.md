# close()

**Framework**: AppKit  
**Kind**: method

Closes all of the document’s windows and removes the document from its document controller.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func close()
```

#### Discussion

This method closes the document immediately, without asking users if they want to save the document. This method may not always be called.

## See Also

- [func shouldCloseWindowController(NSWindowController, delegate: Any?, shouldClose: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/shouldclosewindowcontroller(_:delegate:shouldclose:contextinfo:).md)
  Determines whether the system should close the document and its associated window.
- [func canClose(withDelegate: Any, shouldClose: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/canclose(withdelegate:shouldclose:contextinfo:).md)
  Determines whether to close the document, prompting the user as needed to choose a course of action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/close())*