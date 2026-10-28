# prompt

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A presentation style that displays a prompt to the user when the accessibility quick action is active.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
static var prompt: AccessibilityQuickActionPromptStyle { get }
```

Available when `Self` is `AccessibilityQuickActionPromptStyle`.

## Discussion

The following example shows how to add an [`accessibilityQuickAction(style:content:)`](../view/accessibilityquickaction%28style,content%29.md) to pause and resume a workout.

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

### Getting built-in menu styles
- [static var outline: AccessibilityQuickActionOutlineStyle](./outline.md)
  A presentation style that animates an outline around the view when the accessibility quick action is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityquickactionstyle/prompt)*