# handlePrint(_:)

**Framework**: AppKit  
**Kind**: method

Handles the Print AppleScript command by attempting to print the document.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func handlePrint(_ command: NSScriptCommand) -> Any?
```

#### Discussion

Extracts Print command arguments from the `command` object and uses them to determine how to print the document—specifically, any print settings and whether to show the Print dialog. A Print AppleScript command may specify more than one document to print. If so, a message is sent to each document.

## Parameters

- `command`: An AppleScript command object.

## See Also

- [func handleClose(NSCloseCommand) -> Any?](nsdocument/handleclose(_:).md)
  Handles the Close AppleScript command by attempting to close the document.
- [func handleSave(NSScriptCommand) -> Any?](nsdocument/handlesave(_:).md)
  Handles the Save AppleScript command by attempting to save the document.
- [var objectSpecifier: NSScriptObjectSpecifier](nsdocument/objectspecifier.md)
  Returns the object specifier that represents the document.
- [var lastComponentOfFileName: String](nsdocument/lastcomponentoffilename.md)
  The name of the document seen by the user in AppleScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/handleprint(_:))*