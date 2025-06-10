# defersSystemGestures(on:)

**Framework**: App Intents  
**Kind**: method

Sets the screen edge from which you want your gesture to take precedence over the system gesture.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+

## Declaration

```swift
nonisolated
func defersSystemGestures(on edges: Edge.Set) -> some View
```

#### Discussion

The following code defers the vertical screen edges system gestures of a given canvas.

```swift
struct DeferredView: View {
    var body: some View {
        Canvas()
            .defersSystemGestures(on: .vertical)
    }
}
```

## Parameters

- `edges`: A value that indicates the screen edge from which   you want your gesture to take precedence over the system gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/deferssystemgestures(on:))*