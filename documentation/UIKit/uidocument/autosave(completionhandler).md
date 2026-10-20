# autosave(completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Initiates automatic saving of documents with unsaved changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func autosave(completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func autosave() async -> Bool
```

```objc
- (void) autosaveWithCompletionHandler:(void (^)(BOOL success)) completionHandler;
```

#### Discussion

[`UIDocument`](../uidocument.md) periodically invokes this method to initiate a save operation if there are unsaved changes. You shouldn’t call this method directly. Subclasses can override it if they want to do special things with autosaving. The default implementation of this method invokes the [`hasUnsavedChanges`](./hasunsavedchanges.md) method and, if that returns [`true`](../../Swift/true.md), it invokes the [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md) method.

This method should only be invoked for period-based saves. You may invoke it with the `success` parameter of the completion-handler parameter set to [`false`](../../Swift/false.md) and return; this makes it safe to not actually save when [`autosave(completionHandler:)`](./autosave%28completionhandler%29.md) is invoked. However, if you call [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md), saving of document data must occur.

## Parameters

- `completionHandler`: A block with code to execute after automatic saving concludes. The block returns no value and has one parameter:

  - **`success`**: [`true`](../../Swift/true.md) if the autosaving operation succeeds, otherwise [`false`](../../Swift/false.md).

  The block is invoked on the calling queue.

## See Also

### Tracking changes and autosaving
- [var hasUnsavedChanges: Bool](./hasunsavedchanges.md)
  A Boolean value that indicates whether the document has any unsaved changes.
- [func updateChangeCount(UIDocument.ChangeKind)](./updatechangecount%28_%29.md)
  Updates the change counter by indicating the kind of change.
- [var undoManager: UndoManager!](./undomanager.md)
  The undo manager for the document.
- [func changeCountToken(for: UIDocument.SaveOperation) -> Any](./changecounttoken%28for%29.md)
  Returns a change token for a specific save operation.
- [func updateChangeCount(withToken: Any, for: UIDocument.SaveOperation)](./updatechangecount%28withtoken,for%29.md)
  Updates the change count with reference to a change-count token passed in by UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/autosave(completionhandler:))*