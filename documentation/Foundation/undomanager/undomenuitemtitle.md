# undoMenuItemTitle

**Framework**: Foundation  
**Kind**: property

The title of the Undo menu command, such as Undo Paste.

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
var undoMenuItemTitle: String { get }
```

#### Discussion

Returns “Undo” if no action name has been assigned or `nil` if there is nothing to undo.

## See Also

- [var redoMenuItemTitle: String](undomanager/redomenuitemtitle.md)
  The title of the Redo menu command, such as Redo Paste.
- [func undoMenuTitle(forUndoActionName: String) -> String](undomanager/undomenutitle(forundoactionname:).md)
  Returns the localized title of the Undo menu command for the identified action.
- [func redoMenuTitle(forUndoActionName: String) -> String](undomanager/redomenutitle(forundoactionname:).md)
  Returns the localized title of the Redo menu command for the identified action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/undomenuitemtitle)*