# NSDocument.SaveOperationType.autosaveElsewhereOperation

**Framework**: AppKit  
**Kind**: case

An operation that writes an autosave version of the file to a different location.

**Availability**:
- macOS 10.7+

## Declaration

```swift
case autosaveElsewhereOperation
```

#### Discussion

For an [`NSDocument`](nsdocument.md) subclass that overrides [`autosavesInPlace`](nsdocument/autosavesinplace.md) to have the value [`true`](https://developer.apple.com/documentation/Swift/true), this is used during autosaving of documents that have never been saved and therefore do not yet have a document file that can be overwritten during autosaving. `NSDocument` may also pass `NSAutosaveElsewhereOperation` when invoking `writeSafelyToURL:ofType:forSaveOperation:error:` while duplicating or reverting a document.

## See Also

- [NSDocument.SaveOperationType.saveOperation](nsdocument/saveoperationtype/saveoperation.md)
  An operation that overwrites a document’s file or file package with the document’s contents.
- [NSDocument.SaveOperationType.saveAsOperation](nsdocument/saveoperationtype/saveasoperation.md)
  An operation that writes the document’s contents to a new location and updates the document to point to that location
- [NSDocument.SaveOperationType.saveToOperation](nsdocument/saveoperationtype/savetooperation.md)
  An operation that writes a copy of the document’s contents to the specified location, without changing the original document’s location.
- [NSDocument.SaveOperationType.autosaveInPlaceOperation](nsdocument/saveoperationtype/autosaveinplaceoperation.md)
  An operation that overwrites the document’s current contents with autosave data.
- [NSDocument.SaveOperationType.autosaveAsOperation](nsdocument/saveoperationtype/autosaveasoperation.md)
  An operation that writes a document’s contents to a new file or file package even though the user has not explicitly requested it, then changes the document’s current location to point to the just-written file or file package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/saveoperationtype/autosaveelsewhereoperation)*