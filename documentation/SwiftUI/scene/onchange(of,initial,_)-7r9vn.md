# onChange(of:initial:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
func onChange<V>(of value: V, initial: Bool = false, _ action: @escaping (V, V) -> Void) -> some Scene where V : Equatable
```

**Other overloads**:

```swift
nonisolated
func onChange<V>(of value: V, initial: Bool = false, _ action: @escaping () -> Void) -> some Scene where V : Equatable
```

## Return Value

A scene that triggers an action in response to a change.

## Discussion

Use this modifier to trigger a side effect when a value changes, like the value associated with an [`Environment`](../environment.md) key or a [`Binding`](../binding.md). For example, you can clear a cache when you notice that a scene moves to the background:

```swift
struct MyScene: Scene {
    @Environment(\.scenePhase) private var scenePhase
    @StateObject private var cache = DataCache()

    var body: some Scene {
        WindowGroup {
            MyRootView(cache: cache)
        }
        .onChange(of: scenePhase) { oldScenePhase, newScenePhase in
            if newScenePhase == .background {
                cache.empty()
            }
        }
    }
}
```

The system may call the action closure on the main actor, so avoid long-running tasks in the closure. If you need to perform such tasks, detach an asynchronous background task:

```swift
.onChange(of: scenePhase) { oldScenePhase, newScenePhase in
    if newScenePhase == .background {
        Task.detached(priority: .background) {
            // ...
        }
    }
}
```

When the value changes, the new version of the closure will be called, so any captured values will have their values from the time that the observed value has its new value. The system passes the old and new observed values into the closure.

## Parameters

- `value`: The value to check when determining whether to run the closure. The value must conform to the [`Equatable`](../../Swift/equatable.md) protocol.
- `initial`: Whether the action should be run when this scene initially appears.
- `action`: A closure to run when the value changes.

  - **oldValue**: The old value that failed the comparison check (or the initial value when requested).
  - **newValue**: The new value that failed the comparison check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/onchange(of:initial:_:)-7r9vn)*