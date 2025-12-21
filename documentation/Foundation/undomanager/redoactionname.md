# redoActionName

**Framework**: Foundation  
**Kind**: property

The name identifying the redo action.

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
var redoActionName: String { get }
```

#### Discussion

The redo action name. Returns an empty string (`@""`) if no action name has been assigned or if there is nothing to redo.

For example, if the menu title is “Redo Delete,” the string returned is “Delete.”

## See Also

- [var undoActionName: String](undomanager/undoactionname.md)
  The name identifying the undo action.
- [func setActionName(LocalizedStringResource?)](undomanager/setactionname(_:)-cci9.md)
  Sets the name of the action associated with the Undo or Redo command using a localized string resource.
- [func setActionName(String)](undomanager/setactionname(_:)-8lzip.md)
  Sets the name of the action associated with the Undo or Redo command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/redoactionname)*