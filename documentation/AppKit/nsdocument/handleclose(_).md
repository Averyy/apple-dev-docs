# handleClose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handles the Close AppleScript command by attempting to close the document.

**Availability**:
- macOS

## Declaration

```swift
func handleClose(_ command: NSCloseCommand) -> Any?
```

```objc
- (id) handleCloseScriptCommand:(NSCloseCommand *) command;
```

## Discussion

Extracts Close command arguments from the `command` object and uses them to determine how to close the document—specifically, whether to ignore unsaved changes, save changes automatically, or ask the user and to identify the file in which to save the document (by default, the file that was opened or previously saved to). A Close AppleScript command may specify more than one document to close. If so, a message is sent to each document object.

## Parameters

- `command`: A Close AppleScript command object.

## See Also

### Handling Script Commands
- [func handlePrint(NSScriptCommand) -> Any?](./handleprint%28_%29.md)
  Handles the Print AppleScript command by attempting to print the document.
- [func handleSave(NSScriptCommand) -> Any?](./handlesave%28_%29.md)
  Handles the Save AppleScript command by attempting to save the document.
- [var objectSpecifier: NSScriptObjectSpecifier](./objectspecifier.md)
  Returns the object specifier that represents the document.
- [var lastComponentOfFileName: String](./lastcomponentoffilename.md)
  The name of the document seen by the user in AppleScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/handleclose(_:))*