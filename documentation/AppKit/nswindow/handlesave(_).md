# handleSave(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handles the AppleScript command to save the window (and its associated document, if any).

**Availability**:
- macOS

## Declaration

```swift
func handleSave(_ command: NSScriptCommand) -> Any?
```

```objc
- (id) handleSaveScriptCommand:(NSScriptCommand *) command;
```

#### Discussion

If there’s a corresponding document and the window is the main window of the document, it forwards the `save` command to the corresponding document. Otherwise, this method does nothing.

## See Also

### Handling Script Commands
- [func handleClose(NSCloseCommand) -> Any?](./handleclose%28_%29.md)
  Handles the AppleScript command to close the window (and its associated document, if any).
- [func handlePrint(NSScriptCommand) -> Any?](./handleprint%28_%29.md)
  Handles the AppleScript command to print the contents of the window (or its associated document, if any).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/handlesave(_:))*