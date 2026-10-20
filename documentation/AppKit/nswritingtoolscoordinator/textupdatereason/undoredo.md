# NSWritingToolsCoordinator.TextUpdateReason.undoRedo

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An operation that changed the view’s text as part of an undo or redo command.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case undoRedo
```

```c
NSWritingToolsCoordinatorTextUpdateReasonUndoRedo
```

#### Discussion

Specify this option when an undo or redo command initiated the change to your view.

## See Also

### Getting the reasons
- [NSWritingToolsCoordinator.TextUpdateReason.typing](./typing.md)
  An operation that involved a person editing the text in your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textupdatereason/undoredo)*