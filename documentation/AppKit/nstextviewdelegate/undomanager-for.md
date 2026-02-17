# undoManager(for:)

**Framework**: AppKit  
**Kind**: method

Returns the undo manager for the specified text view.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func undoManager(for view: NSTextView) -> UndoManager?
```

#### Return Value

The undo manager for `view`.

#### Discussion

This method provides the flexibility to return a custom undo manager for the text view. Although `NSTextView` implements undo and redo for changes to text, applications may need a custom undo manager to handle interactions between changes to text and changes to other items in the application.

## Parameters

- `view`: The text view whose undo manager should be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/undomanager(for:))*