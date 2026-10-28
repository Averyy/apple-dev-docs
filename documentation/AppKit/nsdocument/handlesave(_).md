# handleSave(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handles the Save AppleScript command by attempting to save the document.

**Availability**:
- macOS

## Declaration

```swift
func handleSave(_ command: NSScriptCommand) -> Any?
```

```objc
- (id) handleSaveScriptCommand:(NSScriptCommand *) command;
```

## Discussion

Extracts Save command arguments from the `command` object and uses them to determine the file in which to save the document and the file type.

## Parameters

- `command`: An AppleScript command object.

## See Also

### Handling Script Commands
- [func handleClose(NSCloseCommand) -> Any?](./handleclose%28_%29.md)
  Handles the Close AppleScript command by attempting to close the document.
- [func handlePrint(NSScriptCommand) -> Any?](./handleprint%28_%29.md)
  Handles the Print AppleScript command by attempting to print the document.
- [var objectSpecifier: NSScriptObjectSpecifier](./objectspecifier.md)
  Returns the object specifier that represents the document.
- [var lastComponentOfFileName: String](./lastcomponentoffilename.md)
  The name of the document seen by the user in AppleScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/handlesave(_:))*