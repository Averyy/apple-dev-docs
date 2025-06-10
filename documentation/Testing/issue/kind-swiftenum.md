# Issue.Kind

**Framework**: Swift Testing  
**Kind**: enum

Kinds of issues which may be recorded.

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
enum Kind
```

## Topics

### Enumeration Cases
- [Issue.Kind.apiMisused](issue/kind-swift.enum/apimisused.md)
  An issue occurred due to misuse of the testing library.
- [case confirmationMiscounted(actual: Int, expected: any RangeExpression & Sendable)](issue/kind-swift.enum/confirmationmiscounted(actual:expected:).md)
  An issue due to a confirmation being confirmed the wrong number of times.
- [case errorCaught(any Error)](issue/kind-swift.enum/errorcaught(_:).md)
  An issue due to an `Error` being thrown by a test function and caught by the testing library.
- [case expectationFailed(Expectation)](issue/kind-swift.enum/expectationfailed(_:).md)
  An issue due to a failed expectation, such as those produced by [`expect(_:_:sourceLocation:)`](expect(_:_:sourcelocation:).md).
- [Issue.Kind.knownIssueNotRecorded](issue/kind-swift.enum/knownissuenotrecorded.md)
  A known issue was expected, but was not recorded.
- [Issue.Kind.system](issue/kind-swift.enum/system.md)
  An issue due to a failure in the underlying system, not due to a failure within the tests being run.
- [case timeLimitExceeded(timeLimitComponents: (seconds: Int64, attoseconds: Int64))](issue/kind-swift.enum/timelimitexceeded(timelimitcomponents:).md)
  An issue due to a test reaching its time limit and timing out.
- [Issue.Kind.unconditional](issue/kind-swift.enum/unconditional.md)
  An issue which occurred unconditionally, for example by using [`record(_:sourceLocation:)`](issue/record(_:sourcelocation:).md).
- [case valueAttachmentFailed(any Error)](issue/kind-swift.enum/valueattachmentfailed(_:).md)
  An issue due to an `Error` being thrown while attempting to save an attachment to a test report or to disk.
### Default Implementations
- [CustomStringConvertible Implementations](issue/kind-swift.enum/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue/kind-swift.enum)*