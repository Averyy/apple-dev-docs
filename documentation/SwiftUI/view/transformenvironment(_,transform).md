# transformEnvironment(_:transform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Transforms the environment value of the specified key path with the given function.

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
func transformEnvironment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, transform: @escaping (inout V) -> Void) -> some View
```

## See Also

### Modifying the environment of a view
- [func environment<T>(T?) -> some View](./environment%28_%29.md)
  Places an observable object in the view’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View](./environment%28_,_%29.md)
  Sets the environment value of the specified key path to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/transformenvironment(_:transform:))*