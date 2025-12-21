# ConditionTrait

**Framework**: Swift Testing  
**Kind**: struct

A type that defines a condition which must be satisfied for the testing library to enable a test.

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
struct ConditionTrait
```

## Mentions

- [Migrating a test from XCTest](migratingfromxctest.md)

#### Overview

To add this trait to a test, use one of the following functions:

- [`enabled(if:_:sourceLocation:)`](trait/enabled(if:_:sourcelocation:).md)
- [`enabled(_:sourceLocation:_:)`](trait/enabled(_:sourcelocation:_:).md)
- [`disabled(_:sourceLocation:)`](trait/disabled(_:sourcelocation:).md)
- [`disabled(if:_:sourceLocation:)`](trait/disabled(if:_:sourcelocation:).md)
- [`disabled(_:sourceLocation:_:)`](trait/disabled(_:sourcelocation:_:).md)

## Topics

### Instance Properties
- [var sourceLocation: SourceLocation](conditiontrait/sourcelocation.md)
  The source location where this trait is specified.
### Instance Methods
- [func evaluate() async throws -> Bool](conditiontrait/evaluate.md)
  Evaluate this instance’s underlying condition.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SuiteTrait](suitetrait.md)
- [TestTrait](testtrait.md)
- [Trait](trait.md)

## See Also

- [struct Bug](bug.md)
  A type that represents a bug report tracked by a test.
- [struct Comment](comment.md)
  A type that represents a comment related to a test.
- [struct IssueHandlingTrait](issuehandlingtrait.md)
  A type that allows transforming or filtering the issues recorded by a test.
- [struct ParallelizationTrait](parallelizationtrait.md)
  A type that defines whether the testing library runs this test serially or in parallel.
- [struct Tag](tag.md)
  A type representing a tag that can be applied to a test.
- [struct List](tag/list.md)
  A type representing one or more tags applied to a test.
- [struct TimeLimitTrait](timelimittrait.md)
  A type that defines a time limit to apply to a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/conditiontrait)*