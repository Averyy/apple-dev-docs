# transformEnvironment(_:transform:)

**Framework**: SwiftUI  
**Kind**: method

Transforms the environment value of the specified key path with the given function.

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
func transformEnvironment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, transform: @escaping (inout V) -> Void) -> some Scene
```

## See Also

- [func environment<T>(T?) -> some Scene](scene/environment(_:).md)
  Places an observable object in the scene’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some Scene](scene/environment(_:_:).md)
  Sets the environment value of the specified key path to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/transformenvironment(_:transform:))*