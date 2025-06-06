# sensoryFeedback(_:trigger:condition:)

**Framework**: SwiftUI  
**Kind**: method

Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func sensoryFeedback<T>(_ feedback: SensoryFeedback, trigger: T, condition: @escaping (T, T) -> Bool) -> some View where T : Equatable
```

#### Discussion

For example, you could play feedback for certain state transitions:

```swift
struct MyView: View {
    @State private var phase = Phase.inactive

    var body: some View {
        ContentView(phase: $phase)
            .sensoryFeedback(.selection, trigger: phase) { old, new in
                old == .inactive || new == .expanded
            }
    }

    enum Phase {
        case inactive
        case preparing
        case active
        case expanded
    }
}
```

## Parameters

- `feedback`: Which type of feedback to play.
- `trigger`: A value to monitor for changes to determine when to play.
- `condition`: A closure to determine whether to play the feedback when    changes.

## See Also

- [func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View](view/sensoryfeedback(_:trigger:).md)
  Plays the specified `feedback` when the provided `trigger` value changes.
- [func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View](view/sensoryfeedback(trigger:_:).md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [struct SensoryFeedback](sensoryfeedback.md)
  Represents a type of haptic and/or audio feedback that can be played.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/sensoryfeedback(_:trigger:condition:))*