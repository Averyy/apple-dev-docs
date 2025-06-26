# withGroup(resultType:returning:body:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
static func withGroup<TaskResult, BodyResult>(resultType: TaskResult.Type, returning returnType: BodyResult.Type = BodyResult.self, body: (inout Task<Success, Failure>.Group<TaskResult>) async throws -> BodyResult) async rethrows -> BodyResult where TaskResult : Sendable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/withgroup(resulttype:returning:body:))*