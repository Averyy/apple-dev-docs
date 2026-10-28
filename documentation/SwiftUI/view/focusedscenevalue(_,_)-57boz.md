# focusedSceneValue(_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Creates a new view that exposes the provided value to other views whose state depends on the active scene.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func focusedSceneValue<T>(_ keyPath: WritableKeyPath<FocusedValues, T?>, _ value: T?) -> some View
```

**Other overloads**:

```swift
nonisolated
func focusedSceneValue<T>(_ keyPath: WritableKeyPath<FocusedValues, T?>, _ value: T) -> some View
```

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of [`focusedValue(_:_:)`](./focusedvalue%28_,_%29.md) for values that must be visible regardless of where focus is located in the active scene. For example, if an app needs a command for moving focus to a particular text field in the sidebar, it could use this modifier to publish a button action that’s visible to command views as long as the scene is active, and regardless of where focus happens to be in it.

```swift
struct Sidebar: View {
    @FocusState var isFiltering: Bool

    var body: some View {
        VStack {
            TextField(...)
                .focused(when: $isFiltering)
                .focusedSceneValue(\.filterAction) {
                    isFiltering = true
                }
        }
    }
}

struct NavigationCommands: Commands {
    @FocusedValue(\.filterAction) var filterAction

    var body: some Commands {
        CommandMenu("Navigate") {
            Button("Filter in Sidebar") {
                filterAction?()
            }
        }
        .disabled(filterAction == nil)
    }
}

extension FocusedValues {
    @Entry var filterAction: (() -> Void)?
}
```

## Parameters

- `keyPath`: The key path to associate `value` with when adding it to the existing table of published focus values.
- `value`: The focus value to publish, or `nil` if no value is currently available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/focusedscenevalue(_:_:)-57boz)*