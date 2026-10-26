# NSDocument.SaveOperationType.saveToOperation

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An operation that writes a copy of the document’s contents to the specified location, without changing the original document’s location.

**Availability**:
- macOS

## Declaration

```swift
case saveToOperation
```

```c
NSSaveToOperation
```

## See Also

### Constants
- [NSDocument.SaveOperationType.saveOperation](./saveoperation.md)
  An operation that overwrites a document’s file or file package with the document’s contents.
- [NSDocument.SaveOperationType.saveAsOperation](./saveasoperation.md)
  An operation that writes the document’s contents to a new location and updates the document to point to that location
- [NSDocument.SaveOperationType.autosaveElsewhereOperation](./autosaveelsewhereoperation.md)
  An operation that writes an autosave version of the file to a different location.
- [NSDocument.SaveOperationType.autosaveInPlaceOperation](./autosaveinplaceoperation.md)
  An operation that overwrites the document’s current contents with autosave data.
- [NSDocument.SaveOperationType.autosaveAsOperation](./autosaveasoperation.md)
  An operation that writes a document’s contents to a new file or file package even though the user has not explicitly requested it, then changes the document’s current location to point to the just-written file or file package.
- [NSAutosaveOperation](../../nssaveoperationtype/nsautosaveoperation.md)
  Old name for the [`NSAutosaveElsewhereOperation`](./autosaveelsewhereoperation.md) operation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/saveoperationtype/savetooperation)*