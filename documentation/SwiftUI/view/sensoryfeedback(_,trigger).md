# sensoryFeedback(_:trigger:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Plays the specified `feedback` when the provided `trigger` value changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func sensoryFeedback<T>(_ feedback: SensoryFeedback, trigger: T) -> some View where T : Equatable
```

## Discussion

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

## See Also

### Providing haptic feedback
- [func sensoryFeedback(trigger:_:)](./sensoryfeedback%28trigger,_%29.md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) -> Bool) -> some View](./sensoryfeedback%28_,trigger,condition%29.md)
  Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
- [struct SensoryFeedback](../sensoryfeedback.md)
  Represents a type of haptic and/or audio feedback that can be played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/sensoryfeedback(_:trigger:))*