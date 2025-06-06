# handleClose(_:)

**Framework**: AppKit  
**Kind**: method

Handles the AppleScript command to close the window (and its associated document, if any).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func handleClose(_ command: NSCloseCommand) -> Any?
```

#### Discussion

Extracts `close` command arguments from the `command` object and uses them to determine how to close the associated document—specifically, whether to ignore unsaved changes, save changes automatically, or ask the user—and identifies the file to save the document to. By default, the window saves the document to the file that was opened or previously saved to. Otherwise, the window saves it with an “untitled” name.

If there’s a corresponding document and the window is the main window of the document, this function forwards the `close` command to the corresponding document; otherwise, the window sends itself a `performClose` message, if it has a close box.

## See Also

- [func handlePrint(NSScriptCommand) -> Any?](nswindow/handleprint(_:).md)
  Handles the AppleScript command to print the contents of the window (or its associated document, if any).
- [func handleSave(NSScriptCommand) -> Any?](nswindow/handlesave(_:).md)
  Handles the AppleScript command to save the window (and its associated document, if any).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/handleclose(_:))*