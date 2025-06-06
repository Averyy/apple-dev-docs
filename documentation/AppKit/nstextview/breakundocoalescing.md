# breakUndoCoalescing()

**Framework**: AppKit  
**Kind**: method

Informs the receiver that it should begin coalescing successive typing operations in a new undo grouping.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func breakUndoCoalescing()
```

#### Discussion

This method should be invoked when saving the receiver’s contents to preserve proper tracking of unsaved changes and the document’s dirty state.

## See Also

- [var isCoalescingUndo: Bool](nstextview/iscoalescingundo.md)
  A Boolean value that indicates whether undo coalescing is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/breakundocoalescing())*