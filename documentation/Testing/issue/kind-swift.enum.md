# Issue.Kind

**Framework**: Swift Testing  
**Kind**: enum  
**Role**: Enumeration

Kinds of issues which may be recorded.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
enum Kind
```

## Topics

### Enumeration Cases
- [Issue.Kind.apiMisused](./kind-swift.enum/apimisused.md)
  An issue occurred due to misuse of the testing library.
- [case confirmationMiscounted(actual: Int, expected: any RangeExpression & Sendable)](./kind-swift.enum/confirmationmiscounted%28actual,expected%29.md)
  An issue due to a confirmation being confirmed the wrong number of times.
- [case errorCaught(any Error)](./kind-swift.enum/errorcaught%28_%29.md)
  An issue due to an `Error` being thrown by a test function and caught by the testing library.
- [case expectationFailed(Expectation)](./kind-swift.enum/expectationfailed%28_%29.md)
  An issue due to a failed expectation, such as those produced by [`expect(_:_:sourceLocation:)`](../expect%28_,_,sourcelocation%29.md).
- [Issue.Kind.knownIssueNotRecorded](./kind-swift.enum/knownissuenotrecorded.md)
  A known issue was expected, but was not recorded.
- [Issue.Kind.system](./kind-swift.enum/system.md)
  An issue due to a failure in the underlying system, not due to a failure within the tests being run.
- [case timeLimitExceeded(timeLimitComponents: (seconds: Int64, attoseconds: Int64))](./kind-swift.enum/timelimitexceeded%28timelimitcomponents%29.md)
  An issue due to a test reaching its time limit and timing out.
- [Issue.Kind.unconditional](./kind-swift.enum/unconditional.md)
  An issue which occurred unconditionally, for example by using [`record(_:severity:sourceLocation:)`](./record%28_,severity,sourcelocation%29.md).
- [case valueAttachmentFailed(any Error)](./kind-swift.enum/valueattachmentfailed%28_%29.md)
  An issue due to an `Error` being thrown while attempting to save an attachment to a test report or to disk.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue/kind-swift.enum)*