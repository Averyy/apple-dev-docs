# fileNameExtensionWasHiddenInLastRunSavePanel

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the user chose to hide the document’s filename extension.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
var fileNameExtensionWasHiddenInLastRunSavePanel: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if a Save panel was presented and the user chose to hide the extension; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The Save panel includes an option to hide a document’s filename extension. If the user selects this option, AppKit sets the value of this property to [`true`](https://developer.apple.com/documentation/swift/true); otherwise, the value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func runModalSavePanel(for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/runmodalsavepanel(for:delegate:didsave:contextinfo:).md)
  Presents a modal Save panel to the user, then tries to save the document if the user approves the operation.
- [func prepareSavePanel(NSSavePanel) -> Bool](nsdocument/preparesavepanel(_:).md)
  Tells the document to customize the specified Save panel.
- [var shouldRunSavePanelWithAccessoryView: Bool](nsdocument/shouldrunsavepanelwithaccessoryview.md)
  A Boolean value that indicates whether the document’s Save panel displays a list of supported writable document types.
- [var fileTypeFromLastRunSavePanel: String?](nsdocument/filetypefromlastrunsavepanel.md)
  The file type that was last selected in the Save panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/filenameextensionwashiddeninlastrunsavepanel)*