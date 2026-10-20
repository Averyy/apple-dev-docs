# ConditionTrait

**Framework**: Swift Testing  
**Kind**: struct  
**Role**: Structure

A type that defines a condition which must be satisfied for the testing library to enable a test.

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
struct ConditionTrait
```

## Mentions

- [Migrating a test from XCTest](./migratingfromxctest.md)

#### Overview

To add this trait to a test, use one of the following functions:

- [`enabled(if:_:sourceLocation:)`](./trait/enabled%28if,_,sourcelocation%29.md)
- [`enabled(_:sourceLocation:_:)`](./trait/enabled%28_,sourcelocation,_%29.md)
- [`disabled(_:sourceLocation:)`](./trait/disabled%28_,sourcelocation%29.md)
- [`disabled(if:_:sourceLocation:)`](./trait/disabled%28if,_,sourcelocation%29.md)
- [`disabled(_:sourceLocation:_:)`](./trait/disabled%28_,sourcelocation,_%29.md)

## Topics

### Instance Properties
- [var sourceLocation: SourceLocation](./conditiontrait/sourcelocation.md)
  The source location where this trait is specified.
### Instance Methods
- [func evaluate() async throws -> Bool](./conditiontrait/evaluate%28%29.md)
  Evaluate this instance’s underlying condition.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SuiteTrait](./suitetrait.md)
- [TestTrait](./testtrait.md)
- [Trait](./trait.md)

## See Also

### Supporting types
- [struct Bug](./bug.md)
  A type that represents a bug report tracked by a test.
- [struct Comment](./comment.md)
  A type that represents a comment related to a test.
- [struct IssueHandlingTrait](./issuehandlingtrait.md)
  A type that allows transforming or filtering the issues recorded by a test.
- [struct ParallelizationTrait](./parallelizationtrait.md)
  A type that defines whether the testing library runs this test serially or in parallel.
- [struct Tag](./tag.md)
  A type representing a tag that can be applied to a test.
- [struct List](./tag/list.md)
  A type representing one or more tags applied to a test.
- [struct TimeLimitTrait](./timelimittrait.md)
  A type that defines a time limit to apply to a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/conditiontrait)*