# KnownIssueMatcher

**Framework**: Swift Testing  
**Kind**: typealias

A function that is used to match known issues.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
typealias KnownIssueMatcher = (Issue) -> Bool
```

#### Return Value

Whether or not `issue` is known to occur.

## Parameters

- `issue`: The issue to match.

## See Also

- [func withKnownIssue(Comment?, isIntermittent: Bool, sourceLocation: SourceLocation, () throws -> Void)](withknownissue(_:isintermittent:sourcelocation:_:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, () async throws -> Void) async](withknownissue(_:isintermittent:isolation:sourcelocation:_:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, sourceLocation: SourceLocation, () throws -> Void, when: () -> Bool, matching: KnownIssueMatcher) rethrows](withknownissue(_:isintermittent:sourcelocation:_:when:matching:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, () async throws -> Void, when: () async -> Bool, matching: KnownIssueMatcher) async rethrows](withknownissue(_:isintermittent:isolation:sourcelocation:_:when:matching:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/knownissuematcher)*