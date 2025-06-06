# onCommand(_:perform:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform in response to the given selector.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func onCommand(_ selector: Selector, perform action: (() -> Void)?) -> some View
```

#### Return Value

A view that triggers `action` when the `command` occurs.

#### Discussion

This view or one of the views it contains must be in focus in order for the action to trigger. Other actions for the same command on views  to the view in focus take priority, potentially overriding this action.

## Parameters

- `selector`: The selector to register for  .
- `action`: The action to perform. If   is  ,    keeps its association with this view but doesn’t trigger.

## See Also

- [func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View](view/onmovecommand(perform:).md)
  Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [func onDeleteCommand(perform: (() -> Void)?) -> some View](view/ondeletecommand(perform:).md)
  Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some View](view/pagecommand(value:in:step:).md)
  Steps a value through a range in response to page up or page down commands.
- [func onExitCommand(perform: (() -> Void)?) -> some View](view/onexitcommand(perform:).md)
  Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [func onPlayPauseCommand(perform: (() -> Void)?) -> some View](view/onplaypausecommand(perform:).md)
  Adds an action to perform in response to the system’s Play/Pause command.
- [enum MoveCommandDirection](movecommanddirection.md)
  Specifies the direction of an arrow key movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/oncommand(_:perform:))*