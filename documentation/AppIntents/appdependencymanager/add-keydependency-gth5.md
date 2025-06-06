# add(key:dependency:)

**Framework**: App Intents  
**Kind**: method

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
final func add<Dependency>(key: AnyHashable? = nil, dependency dependencyProvider: @escaping () async throws -> Dependency) where Dependency : Sendable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appdependencymanager/add(key:dependency:)-gth5)*