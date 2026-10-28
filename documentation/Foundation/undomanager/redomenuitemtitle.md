# redoMenuItemTitle

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The title of the Redo menu command, such as Redo Paste.

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
var redoMenuItemTitle: String { get }
```

```objc
@property (copy, readonly) NSString * redoMenuItemTitle;
```

## Discussion

Returns “Redo” if no action name has been assigned or `nil` if there is nothing to redo.

## See Also

### Getting and localizing the menu item title
- [var undoMenuItemTitle: String](./undomenuitemtitle.md)
  The title of the Undo menu command, such as Undo Paste.
- [func undoMenuTitle(forUndoActionName: String) -> String](./undomenutitle%28forundoactionname%29.md)
  Returns the localized title of the Undo menu command for the identified action.
- [func redoMenuTitle(forUndoActionName: String) -> String](./redomenutitle%28forundoactionname%29.md)
  Returns the localized title of the Redo menu command for the identified action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/redomenuitemtitle)*