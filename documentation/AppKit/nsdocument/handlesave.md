# handleSave(_:)

**Framework**: AppKit  
**Kind**: method

Handles the Save AppleScript command by attempting to save the document.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func handleSave(_ command: NSScriptCommand) -> Any?
```

#### Discussion

Extracts Save command arguments from the `command` object and uses them to determine the file in which to save the document and the file type.

## Parameters

- `command`: An AppleScript command object.

## See Also

- [func handleClose(NSCloseCommand) -> Any?](nsdocument/handleclose(_:).md)
  Handles the Close AppleScript command by attempting to close the document.
- [func handlePrint(NSScriptCommand) -> Any?](nsdocument/handleprint(_:).md)
  Handles the Print AppleScript command by attempting to print the document.
- [var objectSpecifier: NSScriptObjectSpecifier](nsdocument/objectspecifier.md)
  Returns the object specifier that represents the document.
- [var lastComponentOfFileName: String](nsdocument/lastcomponentoffilename.md)
  The name of the document seen by the user in AppleScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/handlesave(_:))*