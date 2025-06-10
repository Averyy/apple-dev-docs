# withKnownIssue(_:isIntermittent:sourceLocation:_:)

**Framework**: Swift Testing  
**Kind**: func

Invoke a function that has a known issue that is expected to occur during its execution.

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
func withKnownIssue(_ comment: Comment? = nil, isIntermittent: Bool = false, sourceLocation: SourceLocation = #_sourceLocation, _ body: () throws -> Void)
```

## Mentions

- [Migrating a test from XCTest](migratingfromxctest.md)

#### Discussion

Use this function when a test is known to record one or more issues that should not cause the test to fail. For example:

```swift
@Test func example() {
  withKnownIssue {
    try flakyCall()
  }
}
```

Because all errors thrown by `body` are caught as known issues, this function is not throwing. If only some errors or issues are known to occur while others should continue to cause test failures, use [`withKnownIssue(_:isIntermittent:sourceLocation:_:when:matching:)`](withknownissue(_:isintermittent:sourcelocation:_:when:matching:).md) instead.

## Parameters

- `comment`: An optional comment describing the known issue.
- `isIntermittent`: Whether or not the known issue occurs intermittently. If   this argument is   and the known issue does not occur, no secondary   issue is recorded.
- `sourceLocation`: The source location to which any recorded issues should   be attributed.
- `body`: The function to invoke.

## See Also

- [Known issues](known-issues.md)
  Mark issues as known when running tests.
- [func withKnownIssue(Comment?, isIntermittent: Bool, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, () async throws -> Void) async](withknownissue(_:isintermittent:isolation:sourcelocation:_:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, sourceLocation: SourceLocation, () throws -> Void, when: () -> Bool, matching: KnownIssueMatcher) rethrows](withknownissue(_:isintermittent:sourcelocation:_:when:matching:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, () async throws -> Void, when: () async -> Bool, matching: KnownIssueMatcher) async rethrows](withknownissue(_:isintermittent:isolation:sourcelocation:_:when:matching:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [typealias KnownIssueMatcher](knownissuematcher.md)
  A function that is used to match known issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/withknownissue(_:isintermittent:sourcelocation:_:))*