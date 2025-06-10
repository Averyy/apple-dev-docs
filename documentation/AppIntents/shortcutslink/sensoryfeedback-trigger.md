# sensoryFeedback(_:trigger:)

**Framework**: App Intents  
**Kind**: method

Plays the specified `feedback` when the provided `trigger` value changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS 26.0+ (Beta)
- watchOS 10.0+

## Declaration

```swift
nonisolated
func sensoryFeedback<T>(_ feedback: SensoryFeedback, trigger: T) -> some View where T : Equatable
```

#### Discussion

For example, you could play feedback when a state value changes:

```swift
struct MyView: View {
    @State private var showAccessory = false

    var body: some View {
        ContentView()
            .sensoryFeedback(.selection, trigger: showAccessory)
            .onLongPressGesture {
                showAccessory.toggle()
            }

        if showAccessory {
            AccessoryView()
        }
    }
}
```

## Parameters

- `feedback`: Which type of feedback to play.
- `trigger`: A value to monitor for changes to determine when to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/sensoryfeedback(_:trigger:))*