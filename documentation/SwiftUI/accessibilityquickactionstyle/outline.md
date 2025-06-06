# outline

**Framework**: SwiftUI  
**Kind**: property

A presentation style that animates an outline around the view when the accessibility quick action is active.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
static var outline: AccessibilityQuickActionOutlineStyle { get }
```

#### Discussion

Use the [`contentShape(_:_:eoFill:)`](view/contentshape(_:_:eofill:).md) modifier to provide a shape for [`focusEffect`](contentshapekinds/focuseffect.md) if necessary.

The following example shows how to add an [`accessibilityQuickAction(style:content:)`](view/accessibilityquickaction(style:content:).md) to play and pause music.

```swift
@State private var isPlaying = false

var body: some View {
    PlayButton(isPlaying: $isPlaying)
        .contentShape(.focusEffect, Circle())
        .accessibilityQuickAction(style: .outline) {
            Button(isPlaying ? "Pause" : "Play") {
                isPlaying.toggle()
            }
        }
}
```

## See Also

- [static var prompt: AccessibilityQuickActionPromptStyle](accessibilityquickactionstyle/prompt.md)
  A presentation style that displays a prompt to the user when the accessibility quick action is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityquickactionstyle/outline)*