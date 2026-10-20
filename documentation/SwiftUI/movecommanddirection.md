# MoveCommandDirection

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

Specifies the direction of an arrow key movement.

**Availability**:
- macOS 10.15+
- tvOS 13.0+

## Declaration

```swift
enum MoveCommandDirection
```

## Topics

### Getting move command directions
- [MoveCommandDirection.up](./movecommanddirection/up.md)
- [MoveCommandDirection.down](./movecommanddirection/down.md)
- [MoveCommandDirection.left](./movecommanddirection/left.md)
- [MoveCommandDirection.right](./movecommanddirection/right.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responding to commands
- [func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View](./view/onmovecommand%28perform%29.md)
  Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [func onDeleteCommand(perform: (() -> Void)?) -> some View](./view/ondeletecommand%28perform%29.md)
  Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some View](./view/pagecommand%28value,in,step%29.md)
  Steps a value through a range in response to page up or page down commands.
- [func onExitCommand(perform: (() -> Void)?) -> some View](./view/onexitcommand%28perform%29.md)
  Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [func onPlayPauseCommand(perform: (() -> Void)?) -> some View](./view/onplaypausecommand%28perform%29.md)
  Adds an action to perform in response to the system’s Play/Pause command.
- [func onCommand(Selector, perform: (() -> Void)?) -> some View](./view/oncommand%28_,perform%29.md)
  Adds an action to perform in response to the given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/movecommanddirection)*