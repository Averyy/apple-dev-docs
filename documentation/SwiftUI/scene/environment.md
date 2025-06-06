# environment(_:_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the environment value of the specified key path to the given value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func environment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, _ value: V) -> some Scene
```

#### Return Value

A view that has the given value set in its environment.

#### Discussion

Use this modifier to set one of the writable properties of the [`EnvironmentValues`](environmentvalues.md) structure, including custom values that you create. For example, you can create a custom environment key `styleOverrides` to set a value that represents style settings that for the entire app:

```swift
WindowGroup {
    ContentView()
}
.environment(\.styleOverrides, StyleOverrides())
```

You then read the value inside `ContentView` or one of its descendants using the [`Environment`](environment.md) property wrapper:

```swift
struct MyView: View {
    @Environment(\.styleOverrides) var styleOverrides: StyleOverrides

    var body: some View { ... }
}
```

This modifier affects the given scene, as well as that scene’s descendant views. It has no effect outside the view hierarchy on which you call it.

## Parameters

- `keyPath`: A key path that indicates the property of the    structure to update.
- `value`: The new value to set for the item specified by  .

## See Also

- [func environment<T>(T?) -> some Scene](scene/environment(_:).md)
  Places an observable object in the scene’s environment.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some Scene](scene/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/environment(_:_:))*