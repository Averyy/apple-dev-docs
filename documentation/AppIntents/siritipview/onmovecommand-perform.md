# onMoveCommand(perform:)

**Framework**: App Intents  
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/onmovecommand(perform:))*