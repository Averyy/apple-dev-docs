# fileNameExtensionWasHiddenInLastRunSavePanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user chose to hide the document’s filename extension.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
var fileNameExtensionWasHiddenInLastRunSavePanel: Bool { get }
```

```objc
@property (readonly) BOOL fileNameExtensionWasHiddenInLastRunSavePanel;
```

## Return Value

[`true`](../../Swift/true.md) if a Save panel was presented and the user chose to hide the extension; otherwise, [`false`](../../Swift/false.md).

## Discussion

The Save panel includes an option to hide a document’s filename extension. If the user selects this option, AppKit sets the value of this property to [`true`](../../Swift/true.md); otherwise, the value is [`false`](../../Swift/false.md).

## See Also

### Presenting a Save Panel
- [func runModalSavePanel(for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](./runmodalsavepanel%28for,delegate,didsave,contextinfo%29.md)
  Presents a modal Save panel to the user, then tries to save the document if the user approves the operation.
- [func prepareSavePanel(NSSavePanel) -> Bool](./preparesavepanel%28_%29.md)
  Tells the document to customize the specified Save panel.
- [var fileTypeFromLastRunSavePanel: String?](./filetypefromlastrunsavepanel.md)
  The file type that was last selected in the Save panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/filenameextensionwashiddeninlastrunsavepanel)*