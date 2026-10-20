# onDeleteCommand(perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func onDeleteCommand(perform action: (() -> Void)?) -> some View
```

## See Also

### Responding to commands
- [func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View](./onmovecommand%28perform%29.md)
  Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some View](./pagecommand%28value,in,step%29.md)
  Steps a value through a range in response to page up or page down commands.
- [func onExitCommand(perform: (() -> Void)?) -> some View](./onexitcommand%28perform%29.md)
  Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [func onPlayPauseCommand(perform: (() -> Void)?) -> some View](./onplaypausecommand%28perform%29.md)
  Adds an action to perform in response to the system’s Play/Pause command.
- [func onCommand(Selector, perform: (() -> Void)?) -> some View](./oncommand%28_,perform%29.md)
  Adds an action to perform in response to the given selector.
- [enum MoveCommandDirection](../movecommanddirection.md)
  Specifies the direction of an arrow key movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ondeletecommand(perform:))*