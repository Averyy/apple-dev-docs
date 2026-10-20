# NSDocument.SaveOperationType.autosaveElsewhereOperation

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An operation that writes an autosave version of the file to a different location.

**Availability**:
- macOS 10.7+

## Declaration

```swift
case autosaveElsewhereOperation
```

```c
NSAutosaveElsewhereOperation
```

#### Discussion

For an [`NSDocument`](../../nsdocument.md) subclass that overrides [`autosavesInPlace`](../autosavesinplace.md) to have the value [`true`](../../../Swift/true.md), this is used during autosaving of documents that have never been saved and therefore do not yet have a document file that can be overwritten during autosaving. `NSDocument` may also pass `NSAutosaveElsewhereOperation` when invoking `writeSafelyToURL:ofType:forSaveOperation:error:` while duplicating or reverting a document.

## See Also

### Constants
- [NSDocument.SaveOperationType.saveOperation](./saveoperation.md)
  An operation that overwrites a document’s file or file package with the document’s contents.
- [NSDocument.SaveOperationType.saveAsOperation](./saveasoperation.md)
  An operation that writes the document’s contents to a new location and updates the document to point to that location
- [NSDocument.SaveOperationType.saveToOperation](./savetooperation.md)
  An operation that writes a copy of the document’s contents to the specified location, without changing the original document’s location.
- [NSDocument.SaveOperationType.autosaveInPlaceOperation](./autosaveinplaceoperation.md)
  An operation that overwrites the document’s current contents with autosave data.
- [NSDocument.SaveOperationType.autosaveAsOperation](./autosaveasoperation.md)
  An operation that writes a document’s contents to a new file or file package even though the user has not explicitly requested it, then changes the document’s current location to point to the just-written file or file package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/saveoperationtype/autosaveelsewhereoperation)*