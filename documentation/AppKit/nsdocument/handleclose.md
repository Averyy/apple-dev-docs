# handleClose(_:)

**Framework**: AppKit  
**Kind**: method

Handles the Close AppleScript command by attempting to close the document.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func handleClose(_ command: NSCloseCommand) -> Any?
```

#### Discussion

Extracts Close command arguments from the `command` object and uses them to determine how to close the document—specifically, whether to ignore unsaved changes, save changes automatically, or ask the user and to identify the file in which to save the document (by default, the file that was opened or previously saved to). A Close AppleScript command may specify more than one document to close. If so, a message is sent to each document object.

## Parameters

- `command`: A Close AppleScript command object.

## See Also

- [func handlePrint(NSScriptCommand) -> Any?](nsdocument/handleprint(_:).md)
  Handles the Print AppleScript command by attempting to print the document.
- [func handleSave(NSScriptCommand) -> Any?](nsdocument/handlesave(_:).md)
  Handles the Save AppleScript command by attempting to save the document.
- [var objectSpecifier: NSScriptObjectSpecifier](nsdocument/objectspecifier.md)
  Returns the object specifier that represents the document.
- [var lastComponentOfFileName: String](nsdocument/lastcomponentoffilename.md)
  The name of the document seen by the user in AppleScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/handleclose(_:))*