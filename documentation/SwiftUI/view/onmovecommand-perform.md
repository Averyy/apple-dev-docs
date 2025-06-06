# onMoveCommand(perform:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.

**Availability**:
- macOS 10.15+
- tvOS 13.0+

## Declaration

```swift
nonisolated
func onMoveCommand(perform action: ((MoveCommandDirection) -> Void)?) -> some View
```

## See Also

- [func onDeleteCommand(perform: (() -> Void)?) -> some View](view/ondeletecommand(perform:).md)
  Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some View](view/pagecommand(value:in:step:).md)
  Steps a value through a range in response to page up or page down commands.
- [func onExitCommand(perform: (() -> Void)?) -> some View](view/onexitcommand(perform:).md)
  Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [func onPlayPauseCommand(perform: (() -> Void)?) -> some View](view/onplaypausecommand(perform:).md)
  Adds an action to perform in response to the system’s Play/Pause command.
- [func onCommand(Selector, perform: (() -> Void)?) -> some View](view/oncommand(_:perform:).md)
  Adds an action to perform in response to the given selector.
- [enum MoveCommandDirection](movecommanddirection.md)
  Specifies the direction of an arrow key movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onmovecommand(perform:))*