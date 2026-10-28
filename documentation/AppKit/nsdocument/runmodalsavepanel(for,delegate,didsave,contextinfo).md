# runModalSavePanel(for:delegate:didSave:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents a modal Save panel to the user, then tries to save the document if the user approves the operation.

**Availability**:
- macOS

## Declaration

```swift
func runModalSavePanel(for saveOperation: NSDocument.SaveOperationType, delegate: Any?, didSave didSaveSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) runModalSavePanelForSaveOperation:(NSSaveOperationType) saveOperation delegate:(id) delegate didSaveSelector:(SEL) didSaveSelector contextInfo:(void *) contextInfo;
```

## Discussion

When saving is completed, regardless of success or failure, or has been canceled, sends the message selected by `didSaveSelector` to the `delegate`, with `contextInfo` as the last argument. The method selected by `didSaveSelector` must have the same signature as:

```objc
- (void)document:(NSDocument *)doc didSave:(BOOL)didSave contextInfo:(void  *)contextInfo
```

Invoked from [`save(withDelegate:didSave:contextInfo:)`](./save%28withdelegate,didsave,contextinfo%29.md), and from the [`saveAs(_:)`](./saveas%28_%29.md) and [`saveTo(_:)`](./saveto%28_%29.md) action methods. The default implementation of this method first makes sure that any editor registered using the Cocoa Bindings [`NSEditorRegistration`](../nseditorregistration.md) informal protocol has committed its changes, then creates a Save panel, adds a standard file format accessory view (if there is more than one file type for the user to choose from and [`shouldRunSavePanelWithAccessoryView`](./shouldrunsavepanelwithaccessoryview.md) returns [`true`](../../Swift/true.md)), sets various attributes of the panel, invokes [`prepareSavePanel(_:)`](./preparesavepanel%28_%29.md) to provide an opportunity for customization, then presents the panel. If the user approves the panel, the default implementation sends the message [`save(to:ofType:for:delegate:didSave:contextInfo:)`](./save%28to,oftype,for,delegate,didsave,contextinfo%29.md).

For backward binary compatibility with Mac OS v10.3 and earlier, the default implementation of this method instead invokes the deprecated [`saveToFile:saveOperation:delegate:didSaveSelector:contextInfo:`](./savetofile_saveoperation_delegate_didsaveselector_contextinfo_.md) if it is overridden, even if the user cancels the panel.

## Parameters

- `saveOperation`: The type of save operation.
- `delegate`: The delegate to which the selector message is sent.
- `didSaveSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

## See Also

### Presenting a Save Panel
- [func prepareSavePanel(NSSavePanel) -> Bool](./preparesavepanel%28_%29.md)
  Tells the document to customize the specified Save panel.
- [var fileTypeFromLastRunSavePanel: String?](./filetypefromlastrunsavepanel.md)
  The file type that was last selected in the Save panel.
- [var fileNameExtensionWasHiddenInLastRunSavePanel: Bool](./filenameextensionwashiddeninlastrunsavepanel.md)
  A Boolean value that indicates whether the user chose to hide the document’s filename extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/runmodalsavepanel(for:delegate:didsave:contextinfo:))*