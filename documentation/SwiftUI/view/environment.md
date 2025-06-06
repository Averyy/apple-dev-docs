# environment(_:_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the environment value of the specified key path to the given value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func environment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, _ value: V) -> some View
```

## Mentions

- [Applying custom fonts to text](applying-custom-fonts-to-text.md)

#### Return Value

A view that has the given value set in its environment.

#### Discussion

Use this modifier to set one of the writable properties of the [`EnvironmentValues`](environmentvalues.md) structure, including custom values that you create. For example, you can set the value associated with the [`truncationMode`](environmentvalues/truncationmode.md) key:

```swift
MyView()
    .environment(\.truncationMode, .head)
```

You then read the value inside `MyView` or one of its descendants using the [`Environment`](environment.md) property wrapper:

```swift
struct MyView: View {
    @Environment(\.truncationMode) var truncationMode: Text.TruncationMode

    var body: some View { ... }
}
```

SwiftUI provides dedicated view modifiers for setting most environment values, like the [`truncationMode(_:)`](view/truncationmode(_:).md) modifier which sets the [`truncationMode`](environmentvalues/truncationmode.md) value:

```swift
MyView()
    .truncationMode(.head)
```

Prefer the dedicated modifier when available, and offer your own when defining custom environment values, as described in [`Entry()`](entry().md).

This modifier affects the given view, as well as that view’s descendant views. It has no effect outside the view hierarchy on which you call it.

## Parameters

- `keyPath`: A key path that indicates the property of the    structure to update.
- `value`: The new value to set for the item specified by  .

## See Also

- [func environment<T>(T?) -> some View](view/environment(_:).md)
  Places an observable object in the view’s environment.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some View](view/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/environment(_:_:))*