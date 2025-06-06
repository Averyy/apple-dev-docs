# fileTypeFromLastRunSavePanel

**Framework**: AppKit  
**Kind**: property

The file type that was last selected in the Save panel.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
var fileTypeFromLastRunSavePanel: String? { get }
```

#### Discussion

This type is primarily used by the [`save(_:)`](nsdocument/save(_:).md), [`saveAs(_:)`](nsdocument/saveas(_:).md), and [`saveTo(_:)`](nsdocument/saveto(_:).md) methods to determine the type the user chose after the Save panel has been run. The string corresponds to the name of the document type as it is specified in the app’s `Info.plist` file.

## See Also

- [func runModalSavePanel(for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/runmodalsavepanel(for:delegate:didsave:contextinfo:).md)
  Presents a modal Save panel to the user, then tries to save the document if the user approves the operation.
- [func prepareSavePanel(NSSavePanel) -> Bool](nsdocument/preparesavepanel(_:).md)
  Tells the document to customize the specified Save panel.
- [var shouldRunSavePanelWithAccessoryView: Bool](nsdocument/shouldrunsavepanelwithaccessoryview.md)
  A Boolean value that indicates whether the document’s Save panel displays a list of supported writable document types.
- [var fileNameExtensionWasHiddenInLastRunSavePanel: Bool](nsdocument/filenameextensionwashiddeninlastrunsavepanel.md)
  A Boolean value that indicates whether the user chose to hide the document’s filename extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/filetypefromlastrunsavepanel)*