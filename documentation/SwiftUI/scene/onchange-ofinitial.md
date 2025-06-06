# onChange(of:initial:_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when the given value changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func onChange<V>(of value: V, initial: Bool = false, _ action: @escaping () -> Void) -> some Scene where V : Equatable
```

#### Return Value

A scene that triggers an action in response to a change.

#### Discussion

Use this modifier to trigger a side effect when a value changes, like the value associated with an [`Environment`](environment.md) key or a [`Binding`](binding.md). For example, you can clear a cache when you notice that a scene moves to the background:

```swift
struct MyScene: Scene {
    @Environment(\.locale) private var locale
    @StateObject private var cache = LocalizationDataCache()

    var body: some Scene {
        WindowGroup {
            MyRootView(cache: cache)
        }
        .onChange(of: locale) {
            cache.empty()
        }
    }
}
```

The system may call the action closure on the main actor, so avoid long-running tasks in the closure. If you need to perform such tasks, detach an asynchronous background task:

```swift
.onChange(of: locale) {
    Task.detached(priority: .background) {
        // ...
    }
}
```

When the value changes, the new version of the closure will be called, so any captured values will have their values from the time that the observed value has its new value.

## Parameters

- `value`: The value to check when determining whether to run the   closure. The value must conform to the     protocol.
- `initial`: Whether the action should be run when this scene initially   appears.
- `action`: A closure to run when the value changes.

## See Also

- [func handlesExternalEvents(matching: Set<String>) -> some Scene](scene/handlesexternalevents(matching:).md)
  Specifies the external events for which SwiftUI opens a new instance of the modified scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/onchange(of:initial:_:))*