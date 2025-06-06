# handleSave(_:)

**Framework**: AppKit  
**Kind**: method

Handles the AppleScript command to save the window (and its associated document, if any).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func handleSave(_ command: NSScriptCommand) -> Any?
```

#### Discussion

If there’s a corresponding document and the window is the main window of the document, it forwards the `save` command to the corresponding document. Otherwise, this method does nothing.

## See Also

- [func handleClose(NSCloseCommand) -> Any?](nswindow/handleclose(_:).md)
  Handles the AppleScript command to close the window (and its associated document, if any).
- [func handlePrint(NSScriptCommand) -> Any?](nswindow/handleprint(_:).md)
  Handles the AppleScript command to print the contents of the window (or its associated document, if any).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/handlesave(_:))*