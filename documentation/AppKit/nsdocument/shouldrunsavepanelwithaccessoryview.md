# shouldRunSavePanelWithAccessoryView

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the document’s Save panel displays a list of supported writable document types.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var shouldRunSavePanelWithAccessoryView: Bool { get }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the document includes a pop-up menu of supported writable document types when it displays the Save panel. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true). Subclasses can override this property to provide a different value. For example, you might provide the following implementation:

```objc
- (BOOL)shouldRunSavePanelWithAccessoryView {
    return [self fileURL] == nil;
}
```

## See Also

- [func runModalSavePanel(for: NSDocument.SaveOperationType, delegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/runmodalsavepanel(for:delegate:didsave:contextinfo:).md)
  Presents a modal Save panel to the user, then tries to save the document if the user approves the operation.
- [func prepareSavePanel(NSSavePanel) -> Bool](nsdocument/preparesavepanel(_:).md)
  Tells the document to customize the specified Save panel.
- [var fileTypeFromLastRunSavePanel: String?](nsdocument/filetypefromlastrunsavepanel.md)
  The file type that was last selected in the Save panel.
- [var fileNameExtensionWasHiddenInLastRunSavePanel: Bool](nsdocument/filenameextensionwashiddeninlastrunsavepanel.md)
  A Boolean value that indicates whether the user chose to hide the document’s filename extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/shouldrunsavepanelwithaccessoryview)*