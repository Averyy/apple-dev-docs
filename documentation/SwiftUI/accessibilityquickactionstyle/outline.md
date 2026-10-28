# outline

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A presentation style that animates an outline around the view when the accessibility quick action is active.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
static var outline: AccessibilityQuickActionOutlineStyle { get }
```

Available when `Self` is `AccessibilityQuickActionOutlineStyle`.

## Discussion

Use the [`contentShape(_:_:eoFill:)`](../view/contentshape%28_,_,eofill%29.md) modifier to provide a shape for [`focusEffect`](../contentshapekinds/focuseffect.md) if necessary.

The following example shows how to add an [`accessibilityQuickAction(style:content:)`](../view/accessibilityquickaction%28style,content%29.md) to play and pause music.

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

### Getting built-in menu styles
- [static var prompt: AccessibilityQuickActionPromptStyle](./prompt.md)
  A presentation style that displays a prompt to the user when the accessibility quick action is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityquickactionstyle/outline)*