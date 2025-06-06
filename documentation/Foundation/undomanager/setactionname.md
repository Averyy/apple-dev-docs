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
func setActionName(_ actionName: String)
```

#### Discussion

If `actionName` is an empty string, the action name currently associated with the menu command is removed. There is no effect if `actionName` is `nil`.

## Parameters

- `actionName`: The name of the action.

## See Also

- [var undoActionName: String](undomanager/undoactionname.md)
  The name identifying the undo action.
- [var redoActionName: String](undomanager/redoactionname.md)
  The name identifying the redo action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/setactionname(_:))*