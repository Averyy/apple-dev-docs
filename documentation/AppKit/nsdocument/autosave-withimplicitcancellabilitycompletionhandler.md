# autosave(withImplicitCancellability:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Autosaves the document’s contents to an appropriate file-system location, as needed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func autosave(withImplicitCancellability autosavingIsImplicitlyCancellable: Bool) async throws
```

#### Discussion

The default implementation of this method does the following:

1. Checks the value of the [`hasUnautosavedChanges`](nsdocument/hasunautosavedchanges.md) property.
2. If the value of that property is [`false`](https://developer.apple.com/documentation/Swift/false), the method runs the completion handler with a `nil` error and returns immediately.

If the value is [`true`](https://developer.apple.com/documentation/Swift/true), calls [`autosavesInPlace`](nsdocument/autosavesinplace.md) on the class to determine where the autosaved document contents should go.

The method also gets the value in [`fileURL`](nsdocument/fileurl.md) to ensure that the file has an actual URL, because it is not possible to autosave in place if the document does not yet have a permanent location. 3. Checks the value in the [`autosavingFileType`](nsdocument/autosavingfiletype.md) property to determine the file type for the autosaved file. 4. Calls [`save(to:ofType:for:completionHandler:)`](nsdocument/save(to:oftype:for:completionhandler:).md).

The value of the `saveToURL` parameter is the location where the file should be saved. If the file has a URL and the class specifies that autosave should occur in place, this is the URL of the file. Otherwise, this is the location of a nonexistent file in the specified autosave location.

The value for the `ofType` parameter is determined by a call to [`autosavingFileType`](nsdocument/autosavingfiletype.md).

The value of the `forSaveOperation` parameter is `NSAutosaveInPlaceOperation` if the class is configured to autosave in place and the file has a URL. Otherwise, the value is `NSAutosaveElsewhereOperation`.

## Parameters

- `autosavingIsImplicitlyCancellable`: The value in the   property while autosaving is happening.
- `completionHandler`: The block takes one argument:

## See Also

- [func checkAutosavingSafety() throws](nsdocument/checkautosavingsafety.md)
  Returns a Boolean value that indicates whether it is safe to autosave document changes.
- [var hasUnautosavedChanges: Bool](nsdocument/hasunautosavedchanges.md)
  A Boolean value that indicates whether the document has changes that have not been autosaved.
- [func scheduleAutosaving()](nsdocument/scheduleautosaving.md)
  Schedules periodic autosaving for the purpose of crash protection.
- [func autosave(withDelegate: Any?, didAutosave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/autosave(withdelegate:didautosave:contextinfo:).md)
  Autosaves the document’s contents to an appropriate location in the file system.
- [var backupFileURL: URL?](nsdocument/backupfileurl.md)
  The URL for the document’s backup file that was created during an autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/autosave(withimplicitcancellability:completionhandler:))*