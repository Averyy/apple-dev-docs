# accessibilityQuickAction(style:content:)

**Framework**: App Intents  
**Kind**: method

Adds a quick action to be shown by the system when active.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accessibilityQuickAction<Style, Content>(style: Style, @ViewBuilder content: () -> Content) -> some View where Style : AccessibilityQuickActionStyle, Content : View
```

#### Discussion

The quick action will automatically become active when the view appears. If the view is disabled, the action will defer becoming active until the view is no longer disabled.

The following example shows how to add a quick action to pause and resume a workout, with the `AccessibilityQuickActionStyle/prompt` style.

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

The following example shows how to add a quick action to play and pause music, with the `AccessibilityQuickActionStyle/outline` style.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/accessibilityquickaction(style:content:))*