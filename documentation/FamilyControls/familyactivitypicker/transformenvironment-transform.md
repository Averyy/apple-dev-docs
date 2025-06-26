# transformEnvironment(_:transform:)

**Framework**: FamilyControls  
**Kind**: method

Transforms the environment value of the specified key path with the given function.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func transformEnvironment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, transform: @escaping (inout V) -> Void) -> some View
```

## See Also

- [func environmentObject<T>(T) -> some View](familyactivitypicker/environmentobject(_:).md)
  Supplies an observable object to a view’s hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/transformenvironment(_:transform:))*