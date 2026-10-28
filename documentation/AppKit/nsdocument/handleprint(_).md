# handlePrint(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handles the Print AppleScript command by attempting to print the document.

**Availability**:
- macOS

## Declaration

```swift
func handlePrint(_ command: NSScriptCommand) -> Any?
```

```objc
- (id) handlePrintScriptCommand:(NSScriptCommand *) command;
```

## Discussion

Extracts Print command arguments from the `command` object and uses them to determine how to print the document—specifically, any print settings and whether to show the Print dialog. A Print AppleScript command may specify more than one document to print. If so, a message is sent to each document.

## Parameters

- `command`: An AppleScript command object.

## See Also

### Handling Script Commands
- [func handleClose(NSCloseCommand) -> Any?](./handleclose%28_%29.md)
  Handles the Close AppleScript command by attempting to close the document.
- [func handleSave(NSScriptCommand) -> Any?](./handlesave%28_%29.md)
  Handles the Save AppleScript command by attempting to save the document.
- [var objectSpecifier: NSScriptObjectSpecifier](./objectspecifier.md)
  Returns the object specifier that represents the document.
- [var lastComponentOfFileName: String](./lastcomponentoffilename.md)
  The name of the document seen by the user in AppleScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/handleprint(_:))*