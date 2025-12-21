# hasUnautosavedChanges

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the document has changes that have not been autosaved.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var hasUnautosavedChanges: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the document has changes that have not been autosaved; otherwise, the value is [`false`](https://developer.apple.com/documentation/Swift/false). A document has unsaved changes when the [`updateChangeCount(_:)`](nsdocument/updatechangecount(_:).md) method has been called since the last save.

## See Also

- [func checkAutosavingSafety() throws](nsdocument/checkautosavingsafety.md)
  Returns a Boolean value that indicates whether it is safe to autosave document changes.
- [func scheduleAutosaving()](nsdocument/scheduleautosaving.md)
  Schedules periodic autosaving for the purpose of crash protection.
- [func autosave(withDelegate: Any?, didAutosave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/autosave(withdelegate:didautosave:contextinfo:).md)
  Autosaves the document’s contents to an appropriate location in the file system.
- [func autosave(withImplicitCancellability: Bool, completionHandler: ((any Error)?) -> Void)](nsdocument/autosave(withimplicitcancellability:completionhandler:).md)
  Autosaves the document’s contents to an appropriate file-system location, as needed.
- [var backupFileURL: URL?](nsdocument/backupfileurl.md)
  The URL for the document’s backup file that was created during an autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/hasunautosavedchanges)*