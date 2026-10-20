# objectSpecifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the object specifier that represents the document.

**Availability**:
- macOS

## Declaration

```swift
var objectSpecifier: NSScriptObjectSpecifier { get }
```

```objc
@property (strong, readonly) NSScriptObjectSpecifier * objectSpecifier;
```

#### Return Value

The document object specifier.

#### Discussion

An object specifier represents an AppleScript reference form, which is a natural-language expression such as `words 10 through 20` or `front document`. During script processing, an object contained by a document (such as the `second paragraph` or the `third rectangle`) may need to specify its container (the document).

## See Also

### Handling Script Commands
- [func handleClose(NSCloseCommand) -> Any?](./handleclose%28_%29.md)
  Handles the Close AppleScript command by attempting to close the document.
- [func handlePrint(NSScriptCommand) -> Any?](./handleprint%28_%29.md)
  Handles the Print AppleScript command by attempting to print the document.
- [func handleSave(NSScriptCommand) -> Any?](./handlesave%28_%29.md)
  Handles the Save AppleScript command by attempting to save the document.
- [var lastComponentOfFileName: String](./lastcomponentoffilename.md)
  The name of the document seen by the user in AppleScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/objectspecifier)*