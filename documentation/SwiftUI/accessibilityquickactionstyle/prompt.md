# prompt

**Framework**: SwiftUI  
**Kind**: property

A presentation style that displays a prompt to the user when the accessibility quick action is active.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
static var prompt: AccessibilityQuickActionPromptStyle { get }
```

#### Discussion

The following example shows how to add an [`accessibilityQuickAction(style:content:)`](view/accessibilityquickaction(style:content:).md) to pause and resume a workout.

```swift
@State private var isPaused = false

var body: some View {
    WorkoutView(isPaused: $isPaused)
        .accessibilityQuickAction(style: .prompt) {
            Button(isPaused ? "Resume" : "Pause") {
                isPaused.toggle()
            }
        }
}
```

## See Also

- [static var outline: AccessibilityQuickActionOutlineStyle](accessibilityquickactionstyle/outline.md)
  A presentation style that animates an outline around the view when the accessibility quick action is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityquickactionstyle/prompt)*