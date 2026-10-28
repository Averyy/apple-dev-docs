# hasUnsavedChanges

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document has any unsaved changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var hasUnsavedChanges: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasUnsavedChanges;
```

## Return Value

[`true`](../../Swift/true.md) if the document has unsaved changes, otherwise [`false`](../../Swift/false.md).

## Discussion

The default implementation of [`autosave(completionHandler:)`](./autosave%28completionhandler%29.md) initiates a save if this property returns [`true`](../../Swift/true.md). Typical subclasses don’t need to override [`hasUnsavedChanges`](./hasunsavedchanges.md). To implement change tracking, they should instead use an [`UndoManager`](../../Foundation/undomanager.md) object (assigned to [`undoManager`](./undomanager.md)) to register changes or call [`updateChangeCount(_:)`](./updatechangecount%28_%29.md) every time the user makes a change; UIKit then automatically determines whether there are unsaved changes.

## See Also

### Tracking changes and autosaving
- [func updateChangeCount(UIDocument.ChangeKind)](./updatechangecount%28_%29.md)
  Updates the change counter by indicating the kind of change.
- [var undoManager: UndoManager!](./undomanager.md)
  The undo manager for the document.
- [func changeCountToken(for: UIDocument.SaveOperation) -> Any](./changecounttoken%28for%29.md)
  Returns a change token for a specific save operation.
- [func updateChangeCount(withToken: Any, for: UIDocument.SaveOperation)](./updatechangecount%28withtoken,for%29.md)
  Updates the change count with reference to a change-count token passed in by UIKit.
- [func autosave(completionHandler: ((Bool) -> Void)?)](./autosave%28completionhandler%29.md)
  Initiates automatic saving of documents with unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/hasunsavedchanges)*