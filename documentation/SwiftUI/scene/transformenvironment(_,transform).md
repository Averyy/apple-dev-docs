# transformEnvironment(_:transform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

### Modifying the environment of a scene
- [func environment<T>(T?) -> some Scene](./environment%28_%29.md)
  Places an observable object in the scene’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some Scene](./environment%28_,_%29.md)
  Sets the environment value of the specified key path to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/transformenvironment(_:transform:))*