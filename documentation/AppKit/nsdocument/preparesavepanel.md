# prepareSavePanel(_:)

**Framework**: AppKit  
**Kind**: method

Tells the document to customize the specified Save panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func prepareSavePanel(_ savePanel: NSSavePanel) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successfully prepared; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The default implementation is empty and returns [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `savePanel`: The Save panel.

## See Also

- [func runModalSavePanel(for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/runmodalsavepanel(for:delegate:didsave:contextinfo:).md)
  Presents a modal Save panel to the user, then tries to save the document if the user approves the operation.
- [var shouldRunSavePanelWithAccessoryView: Bool](nsdocument/shouldrunsavepanelwithaccessoryview.md)
  A Boolean value that indicates whether the document’s Save panel displays a list of supported writable document types.
- [var fileTypeFromLastRunSavePanel: String?](nsdocument/filetypefromlastrunsavepanel.md)
  The file type that was last selected in the Save panel.
- [var fileNameExtensionWasHiddenInLastRunSavePanel: Bool](nsdocument/filenameextensionwashiddeninlastrunsavepanel.md)
  A Boolean value that indicates whether the user chose to hide the document’s filename extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/preparesavepanel(_:))*