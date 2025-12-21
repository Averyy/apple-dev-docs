# setActionName(_:)

**Framework**: Foundation  
**Kind**: method

Sets the name of the action associated with the Undo or Redo command.

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
func setActionName(_ actionName: String)
```

#### Discussion

If `actionName` is an empty string, the undo manager removes the action name currently associated with the menu command.

## Parameters

- `actionName`: The name of the action.

## See Also

- [var undoActionName: String](undomanager/undoactionname.md)
  The name identifying the undo action.
- [var redoActionName: String](undomanager/redoactionname.md)
  The name identifying the redo action.
- [func setActionName(LocalizedStringResource?)](undomanager/setactionname(_:)-cci9.md)
  Sets the name of the action associated with the Undo or Redo command using a localized string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/setactionname(_:)-8lzip)*