# onExitCommand(perform:)

**Framework**: RealityKit  
**Kind**: method

Sets up an action that triggers in response to receiving the exit command while the view has focus.

**Availability**:
- macOS 10.15+
- tvOS 13.0+

## Declaration

```swift
nonisolated
func onExitCommand(perform action: (() -> Void)?) -> some View
```

#### Discussion

The user generates an exit command by pressing the Menu button on tvOS, or the escape key on macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/onexitcommand(perform:))*