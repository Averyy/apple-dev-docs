# undoMenuTitle(forUndoActionName:)

**Framework**: Foundation  
**Kind**: method

Returns the localized title of the Undo menu command for the identified action.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@MainActor
func undoMenuTitle(forUndoActionName actionName: String) -> String
```

#### Return Value

The localized title of the undo menu item.

#### Discussion

Override this method if you want to customize the localization behavior. This method is invoked by [`undoMenuItemTitle`](undomanager/undomenuitemtitle.md).

## Parameters

- `actionName`: The name of the undo action.

## See Also

- [var undoMenuItemTitle: String](undomanager/undomenuitemtitle.md)
  The title of the Undo menu command, such as Undo Paste.
- [var redoMenuItemTitle: String](undomanager/redomenuitemtitle.md)
  The title of the Redo menu command, such as Redo Paste.
- [func redoMenuTitle(forUndoActionName: String) -> String](undomanager/redomenutitle(forundoactionname:).md)
  Returns the localized title of the Redo menu command for the identified action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/undomenutitle(forundoactionname:))*