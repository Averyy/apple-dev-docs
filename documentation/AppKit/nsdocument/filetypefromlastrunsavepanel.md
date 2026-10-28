# fileTypeFromLastRunSavePanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The file type that was last selected in the Save panel.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
var fileTypeFromLastRunSavePanel: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * fileTypeFromLastRunSavePanel;
```

## Discussion

This type is primarily used by the [`save(_:)`](./save%28_%29.md), [`saveAs(_:)`](./saveas%28_%29.md), and [`saveTo(_:)`](./saveto%28_%29.md) methods to determine the type the user chose after the Save panel has been run. The string corresponds to the name of the document type as it is specified in the app’s `Info.plist` file.

## See Also

### Presenting a Save Panel
- [func runModalSavePanel(for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](./runmodalsavepanel%28for,delegate,didsave,contextinfo%29.md)
  Presents a modal Save panel to the user, then tries to save the document if the user approves the operation.
- [func prepareSavePanel(NSSavePanel) -> Bool](./preparesavepanel%28_%29.md)
  Tells the document to customize the specified Save panel.
- [var fileNameExtensionWasHiddenInLastRunSavePanel: Bool](./filenameextensionwashiddeninlastrunsavepanel.md)
  A Boolean value that indicates whether the user chose to hide the document’s filename extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/filetypefromlastrunsavepanel)*