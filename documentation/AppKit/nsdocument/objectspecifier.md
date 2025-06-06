# objectSpecifier

**Framework**: AppKit  
**Kind**: property

Returns the object specifier that represents the document.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var objectSpecifier: NSScriptObjectSpecifier { get }
```

#### Return Value

The document object specifier.

#### Discussion

An object specifier represents an AppleScript reference form, which is a natural-language expression such as `words 10 through 20` or `front document`. During script processing, an object contained by a document (such as the `second paragraph` or the `third rectangle`) may need to specify its container (the document).

## See Also

- [func handleClose(NSCloseCommand) -> Any?](nsdocument/handleclose(_:).md)
  Handles the Close AppleScript command by attempting to close the document.
- [func handlePrint(NSScriptCommand) -> Any?](nsdocument/handleprint(_:).md)
  Handles the Print AppleScript command by attempting to print the document.
- [func handleSave(NSScriptCommand) -> Any?](nsdocument/handlesave(_:).md)
  Handles the Save AppleScript command by attempting to save the document.
- [var lastComponentOfFileName: String](nsdocument/lastcomponentoffilename.md)
  The name of the document seen by the user in AppleScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/objectspecifier)*