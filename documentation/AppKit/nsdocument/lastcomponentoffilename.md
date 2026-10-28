# lastComponentOfFileName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name of the document seen by the user in AppleScript.

**Availability**:
- macOS

## Declaration

```swift
var lastComponentOfFileName: String { get set }
```

```objc
@property (copy) NSString * lastComponentOfFileName;
```

## Discussion

This property contains the document name used during scripting. Note that this name may be different than the name used in [`fileURL`](./fileurl.md).

## See Also

### Related Documentation
- [var displayName: String!](./displayname.md)
  The name of the document as displayed in the title bars of the document’s windows and in alert dialogs related to the document.
### Handling Script Commands
- [func handleClose(NSCloseCommand) -> Any?](./handleclose%28_%29.md)
  Handles the Close AppleScript command by attempting to close the document.
- [func handlePrint(NSScriptCommand) -> Any?](./handleprint%28_%29.md)
  Handles the Print AppleScript command by attempting to print the document.
- [func handleSave(NSScriptCommand) -> Any?](./handlesave%28_%29.md)
  Handles the Save AppleScript command by attempting to save the document.
- [var objectSpecifier: NSScriptObjectSpecifier](./objectspecifier.md)
  Returns the object specifier that represents the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/lastcomponentoffilename)*