# Known issues

**Framework**: Swift Testing

Highlight known issues when running tests.

#### Overview

The testing library provides a function, `withKnownIssue()`, that you use to mark issues as known. Use this function to inform the testing library at runtime not to mark the test as failing when issues occur.

## Topics

### Recording known issues in tests
- [func withKnownIssue(Comment?, isIntermittent: Bool, sourceLocation: SourceLocation, () throws -> Void)](withknownissue(_:isintermittent:sourcelocation:_:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, () async throws -> Void) async](withknownissue(_:isintermittent:isolation:sourcelocation:_:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, sourceLocation: SourceLocation, () throws -> Void, when: () -> Bool, matching: KnownIssueMatcher) rethrows](withknownissue(_:isintermittent:sourcelocation:_:when:matching:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [func withKnownIssue(Comment?, isIntermittent: Bool, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, () async throws -> Void, when: () async -> Bool, matching: KnownIssueMatcher) async rethrows](withknownissue(_:isintermittent:isolation:sourcelocation:_:when:matching:).md)
  Invoke a function that has a known issue that is expected to occur during its execution.
- [typealias KnownIssueMatcher](knownissuematcher.md)
  A function that is used to match known issues.
### Describing a failure or warning
- [struct Issue](issue.md)
  A type describing a failure or warning which occurred during a test.

## See Also

- [Expectations and confirmations](expectations.md)
  Check for expected values, outcomes, and asynchronous events in tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/known-issues)*