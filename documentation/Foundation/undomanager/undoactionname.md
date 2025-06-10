# undoActionName

**Framework**: Foundation  
**Kind**: property

The name identifying the undo action.

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
var undoActionName: String { get }
```

#### Discussion

The undo action name. Returns an empty string (`@""`) if no action name has been assigned or if there is nothing to undo.

For example, if the menu title is “Undo Delete,” the string returned is “Delete.”

## See Also

- [var redoActionName: String](undomanager/redoactionname.md)
  The name identifying the redo action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/undoactionname)*