# hasUnautosavedChanges

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document has changes that have not been autosaved.

**Availability**:
- macOS

## Declaration

```swift
var hasUnautosavedChanges: Bool { get }
```

```objc
@property (readonly) BOOL hasUnautosavedChanges;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the document has changes that have not been autosaved; otherwise, the value is [`false`](../../Swift/false.md). A document has unsaved changes when the [`updateChangeCount(_:)`](./updatechangecount%28_%29.md) method has been called since the last save.

## See Also

### Autosaving the Document
- [func checkAutosavingSafety() throws](./checkautosavingsafety%28%29.md)
  Returns a Boolean value that indicates whether it is safe to autosave document changes.
- [func scheduleAutosaving()](./scheduleautosaving%28%29.md)
  Schedules periodic autosaving for the purpose of crash protection.
- [func autosave(withDelegate: Any?, didAutosave: Selector?, contextInfo: UnsafeMutableRawPointer?)](./autosave%28withdelegate,didautosave,contextinfo%29.md)
  Autosaves the document’s contents to an appropriate location in the file system.
- [func autosave(withImplicitCancellability: Bool, completionHandler: ((any Error)?) -> Void)](./autosave%28withimplicitcancellability,completionhandler%29.md)
  Autosaves the document’s contents to an appropriate file-system location, as needed.
- [var backupFileURL: URL?](./backupfileurl.md)
  The URL for the document’s backup file that was created during an autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/hasunautosavedchanges)*