# transformEnvironment(_:transform:)

**Framework**: PermissionKit  
**Kind**: method

Transforms the environment value of the specified key path with the given function.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 26.0+ (Beta)
- watchOS 6.0+

## Declaration

```swift
nonisolated
func transformEnvironment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, transform: @escaping (inout V) -> Void) -> some View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/transformenvironment(_:transform:))*