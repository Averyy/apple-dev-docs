# IssueHandlingTrait

**Framework**: Swift Testing  
**Kind**: struct

A type that allows transforming or filtering the issues recorded by a test.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
struct IssueHandlingTrait
```

#### Overview

Use this type to observe or customize the issue(s) recorded by the test this trait is applied to. You can transform a recorded issue by copying it, modifying one or more of its properties, and returning the copy. You can observe recorded issues by returning them unmodified. Or you can suppress an issue by either filtering it using [`filterIssues(_:)`](trait/filterissues(_:).md) or returning `nil` from the closure passed to [`compactMapIssues(_:)`](trait/compactmapissues(_:).md).

When an instance of this trait is applied to a suite, it is recursively inherited by all child suites and tests.

To add this trait to a test, use one of the following functions:

- [`compactMapIssues(_:)`](trait/compactmapissues(_:).md)
- [`filterIssues(_:)`](trait/filterissues(_:).md)

## Topics

### Instance Methods
- [func handleIssue(Issue) -> Issue?](issuehandlingtrait/handleissue(_:).md)
  Handle a specified issue.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SuiteTrait](suitetrait.md)
- [TestScoping](testscoping.md)
- [TestTrait](testtrait.md)
- [Trait](trait.md)

## See Also

- [struct Bug](bug.md)
  A type that represents a bug report tracked by a test.
- [struct Comment](comment.md)
  A type that represents a comment related to a test.
- [struct ConditionTrait](conditiontrait.md)
  A type that defines a condition which must be satisfied for the testing library to enable a test.
- [struct ParallelizationTrait](parallelizationtrait.md)
  A type that defines whether the testing library runs this test serially or in parallel.
- [struct Tag](tag.md)
  A type representing a tag that can be applied to a test.
- [struct List](tag/list.md)
  A type representing one or more tags applied to a test.
- [struct TimeLimitTrait](timelimittrait.md)
  A type that defines a time limit to apply to a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issuehandlingtrait)*