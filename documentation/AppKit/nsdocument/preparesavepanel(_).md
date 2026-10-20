# prepareSavePanel(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the document to customize the specified Save panel.

**Availability**:
- macOS

## Declaration

```swift
func prepareSavePanel(_ savePanel: NSSavePanel) -> Bool
```

```objc
- (BOOL) prepareSavePanel:(NSSavePanel *) savePanel;
```

#### Return Value

[`true`](../../Swift/true.md) if successfully prepared; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The default implementation is empty and returns [`true`](../../Swift/true.md).

## Parameters

- `savePanel`: The Save panel.

## See Also

### Presenting a Save Panel
- [func runModalSavePanel(for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](./runmodalsavepanel%28for,delegate,didsave,contextinfo%29.md)
  Presents a modal Save panel to the user, then tries to save the document if the user approves the operation.
- [var fileTypeFromLastRunSavePanel: String?](./filetypefromlastrunsavepanel.md)
  The file type that was last selected in the Save panel.
- [var fileNameExtensionWasHiddenInLastRunSavePanel: Bool](./filenameextensionwashiddeninlastrunsavepanel.md)
  A Boolean value that indicates whether the user chose to hide the document’s filename extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/preparesavepanel(_:))*