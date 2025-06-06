# NSDocument.SaveOperationType.autosaveAsOperation

**Framework**: AppKit  
**Kind**: case

An operation that writes a document’s contents to a new file or file package even though the user has not explicitly requested it, then changes the document’s current location to point to the just-written file or file package.

**Availability**:
- macOS 10.8+

## Declaration

```swift
case autosaveAsOperation
```

## See Also

- [NSDocument.SaveOperationType.saveOperation](nsdocument/saveoperationtype/saveoperation.md)
  An operation that overwrites a document’s file or file package with the document’s contents.
- [NSDocument.SaveOperationType.saveAsOperation](nsdocument/saveoperationtype/saveasoperation.md)
  An operation that writes the document’s contents to a new location and updates the document to point to that location
- [NSDocument.SaveOperationType.saveToOperation](nsdocument/saveoperationtype/savetooperation.md)
  An operation that writes a copy of the document’s contents to the specified location, without changing the original document’s location.
- [NSDocument.SaveOperationType.autosaveElsewhereOperation](nsdocument/saveoperationtype/autosaveelsewhereoperation.md)
  An operation that writes an autosave version of the file to a different location.
- [NSDocument.SaveOperationType.autosaveInPlaceOperation](nsdocument/saveoperationtype/autosaveinplaceoperation.md)
  An operation that overwrites the document’s current contents with autosave data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/saveoperationtype/autosaveasoperation)*