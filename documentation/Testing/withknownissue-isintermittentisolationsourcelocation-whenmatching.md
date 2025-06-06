# withKnownIssue(_:isIntermittent:isolation:sourceLocation:_:when:matching:)

**Framework**: Testing  
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
func withKnownIssue(_ comment: Comment? = nil, isIntermittent: Bool = false, isolation: isolated (any Actor)? = #isolation, sourceLocation: SourceLocation = #_sourceLocation, _ body: () async throws -> Void, when precondition: () async -> Bool = { true }, matching issueMatcher: @escaping KnownIssueMatcher = { _ in true }) async rethrows
```

## Mentions

- [Migrating a test from XCTest](migratingfromxctest.md)

#### Discussion

> **Note**: Whatever is thrown by `body`, unless it is matched by `issueMatcher`.

Use this function when a test is known to raise one or more issues that should not cause the test to fail, or if a precondition affects whether issues are known to occur. For example:

```swift
@Test func example() async throws {
  try await withKnownIssue {
    try await flakyCall()
  } when: {
    callsAreFlakyOnThisPlatform()
  } matching: { issue in
    issue.error is FileNotFoundError
  }
}
```

It is not necessary to specify both `precondition` and `issueMatcher` if only one is relevant. If all errors and issues should be considered known issues, use [`withKnownIssue(_:isIntermittent:isolation:sourceLocation:_:when:matching:)`](withknownissue(_:isintermittent:isolation:sourcelocation:_:when:matching:).md) instead.

> **Note**: `issueMatcher` may be invoked more than once for the same issue.

## Parameters

- `comment`: An optional comment describing the known issue.
- `isIntermittent`: Whether or not the known issue occurs intermittently. If   this argument is   and the known issue does not occur, no secondary   issue is recorded.
- `isolation`: The actor to which   is isolated, if any.
- `sourceLocation`: The source location to which any recorded issues should   be attributed.
- `body`: The function to invoke.
- `precondition`: A function that determines if issues are known to occur   during the execution of  . If this function returns  ,   encountered issues that are matched by   are considered to   be known issues; if this function returns  ,   is not   called and they are treated as unknown.
- `issueMatcher`: A function to invoke when an issue occurs that is used to   determine if the issue is known to occur. By default, all issues match.

## See Also

- [func withKnownIssue(Comment?, isIntermittent: Bool, sourceLocation: SourceLocation, () throws -> Void)](withknownissue(_:isintermittent:sourcelocation:_:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, () async throws -> Void) async](withknownissue(_:isintermittent:isolation:sourcelocation:_:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, sourceLocation: SourceLocation, () throws -> Void, when: () -> Bool, matching: KnownIssueMatcher) rethrows](withknownissue(_:isintermittent:sourcelocation:_:when:matching:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [typealias KnownIssueMatcher](knownissuematcher.md)
  A function that is used to match known issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/withknownissue(_:isintermittent:isolation:sourcelocation:_:when:matching:))*