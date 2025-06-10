# backupFileURL

**Framework**: AppKit  
**Kind**: property

The URL for the document’s backup file that was created during an autosave operation.

**Availability**:
- macOS 10.8+

## Declaration

```swift
nonisolated
var backupFileURL: URL? { get }
```

#### Discussion

This property specifies the location of the backup file, if any. If a backup file cannot be created or is not needed, the value of this property is `nil`.

Starting in OS X v10.8, document versions can be preserved using a backup file created during an autosave operation, which supports document versioning. This property gives you access to the backup file’s URL.

Using an autosave backup file for preserving versions is efficient. This is because an [`NSDocument`](nsdocument.md) instance is able to use the [`byMoving`](https://developer.apple.com/documentation/Foundation/NSFileVersion/ReplacingOptions/byMoving) option when it calls the [`replaceItem(at:options:)`](https://developer.apple.com/documentation/Foundation/NSFileVersion/replaceItem(at:options:)) method. The document gets the value of this property twice during saving:

1. Before calling the [`writeSafely(to:ofType:for:)`](nsdocument/writesafely(to:oftype:for:).md) method: This is to check whether using the replace-by-moving option is possible and, if not, to allow the system to preserve data by instead using copying.
2. Within the [`writeSafely(to:ofType:for:)`](nsdocument/writesafely(to:oftype:for:).md) method: This is to discover where to put the backup file.

When you implement the [`writeSafely(to:ofType:for:)`](nsdocument/writesafely(to:oftype:for:).md) method with the [`NSDocument.SaveOperationType.saveOperation`](nsdocument/saveoperationtype/saveoperation.md) or [`NSDocument.SaveOperationType.autosaveInPlaceOperation`](nsdocument/saveoperationtype/autosaveinplaceoperation.md) operation type, you must check this property’s value. If it is not `nil`, move the previous contents of the file (that would be overwritten) to the URL’s location. The default implementation of [`writeSafely(to:ofType:for:)`](nsdocument/writesafely(to:oftype:for:).md) does this.

To create a backup file from within your custom implementation of the [`writeSafely(to:ofType:for:)`](nsdocument/writesafely(to:oftype:for:).md) method, call the [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager) method [`replaceItem(at:withItemAt:backupItemName:options:resultingItemURL:)`](https://developer.apple.com/documentation/Foundation/FileManager/replaceItem(at:withItemAt:backupItemName:options:resultingItemURL:)), using a backup item name of `[[self backupFileURL] lastPathComponent]` and an option of [`withoutDeletingBackupItem`](https://developer.apple.com/documentation/Foundation/FileManager/ItemReplacementOptions/withoutDeletingBackupItem) option. If your custom implementation is unable to keep the backup file, you must override this property and return `nil` to ensure that the document’s file gets correctly preserved before it gets overwritten.

The default implementation of the [`writeSafely(to:ofType:for:)`](nsdocument/writesafely(to:oftype:for:).md) method returns a non-`nil` value based on the value of `[self fileURL]`, but only if the document’s file needs to be preserved prior to saving or if the [`preservesVersions`](nsdocument/preservesversions.md) method returns [`false`](https://developer.apple.com/documentation/swift/false). Otherwise, it returns `nil`.

## See Also

- [func checkAutosavingSafety() throws](nsdocument/checkautosavingsafety.md)
  Returns a Boolean value that indicates whether it is safe to autosave document changes.
- [var hasUnautosavedChanges: Bool](nsdocument/hasunautosavedchanges.md)
  A Boolean value that indicates whether the document has changes that have not been autosaved.
- [func scheduleAutosaving()](nsdocument/scheduleautosaving.md)
  Schedules periodic autosaving for the purpose of crash protection.
- [func autosave(withDelegate: Any?, didAutosave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/autosave(withdelegate:didautosave:contextinfo:).md)
  Autosaves the document’s contents to an appropriate location in the file system.
- [func autosave(withImplicitCancellability: Bool, completionHandler: ((any Error)?) -> Void)](nsdocument/autosave(withimplicitcancellability:completionhandler:).md)
  Autosaves the document’s contents to an appropriate file-system location, as needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/backupfileurl)*