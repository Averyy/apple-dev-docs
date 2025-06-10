# TimeLimitTrait

**Framework**: Swift Testing  
**Kind**: struct

A type that defines a time limit to apply to a test.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
struct TimeLimitTrait
```

#### Overview

To add this trait to a test, use [`timeLimit(_:)`](trait/timelimit(_:).md).

## Topics

### Structures
- [TimeLimitTrait.Duration](timelimittrait/duration.md)
  A type representing the duration of a time limit applied to a test.
### Instance Properties
- [var isRecursive: Bool](timelimittrait/isrecursive.md)
  Whether this instance should be applied recursively to child test suites and test functions.
- [var timeLimit: Duration](timelimittrait/timelimit.md)
  The maximum amount of time a test may run for before timing out.
### Type Aliases
- [TimeLimitTrait.TestScopeProvider](timelimittrait/testscopeprovider.md)
  The type of the test scope provider for this trait.
### Default Implementations
- [Trait Implementations](timelimittrait/trait-implementations.md)

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
- [struct ConditionTrait](conditiontrait.md)
  A type that defines a condition which must be satisfied for the testing library to enable a test.
- [struct ParallelizationTrait](parallelizationtrait.md)
  A type that defines whether the testing library runs this test serially or in parallel.
- [struct Tag](tag.md)
  A type representing a tag that can be applied to a test.
- [struct List](tag/list.md)
  A type representing one or more tags applied to a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/timelimittrait)*