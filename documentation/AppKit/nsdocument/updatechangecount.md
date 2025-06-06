# updateChangeCount(_:)

**Framework**: AppKit  
**Kind**: method

Updates the receiver’s change count according to the given change type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func updateChangeCount(_ change: NSDocument.ChangeType)
```

#### Discussion

The change count indicates the document’s edited status; if the change count is 0, the document has no changes to save, and if the change count is greater than 0, the document has been edited and is unsaved. If you are implementing undo and redo in an app, you should increment the change count every time you create an undo group and decrement the change count when an undo or redo operation is performed.

Note that if you are using the `NSDocument` default undo/redo features, setting the document’s edited status by updating the change count happens automatically. You only need to invoke this method when you are not using these features.

## Parameters

- `change`: The type of change made to the document. For a list of values, see  .

## See Also

- [func updateChangeCount(withToken: Any, for: NSDocument.SaveOperationType)](nsdocument/updatechangecount(withtoken:for:).md)
  Updates the document’s change count settings after a successful save operation.
- [NSDocument.ChangeType](nsdocument/changetype.md)
  Values that indicate a document’s edit status.
- [func changeCountToken(for: NSDocument.SaveOperationType) -> Any](nsdocument/changecounttoken(for:).md)
  Returns an object that encapsulates the current record of document changes at the beginning of a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/updatechangecount(_:))*