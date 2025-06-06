# lastComponentOfFileName

**Framework**: AppKit  
**Kind**: property

The name of the document seen by the user in AppleScript.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var lastComponentOfFileName: String { get set }
```

#### Discussion

This property contains the document name used during scripting. Note that this name may be different than the name used in [`fileURL`](nsdocument/fileurl.md).

## See Also

- [var displayName: String!](nsdocument/displayname.md)
  The name of the document as displayed in the title bars of the document’s windows and in alert dialogs related to the document.
- [func handleClose(NSCloseCommand) -> Any?](nsdocument/handleclose(_:).md)
  Handles the Close AppleScript command by attempting to close the document.
- [func handlePrint(NSScriptCommand) -> Any?](nsdocument/handleprint(_:).md)
  Handles the Print AppleScript command by attempting to print the document.
- [func handleSave(NSScriptCommand) -> Any?](nsdocument/handlesave(_:).md)
  Handles the Save AppleScript command by attempting to save the document.
- [var objectSpecifier: NSScriptObjectSpecifier](nsdocument/objectspecifier.md)
  Returns the object specifier that represents the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/lastcomponentoffilename)*