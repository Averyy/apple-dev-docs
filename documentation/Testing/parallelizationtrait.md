# ParallelizationTrait

**Framework**: Swift Testing  
**Kind**: struct

A type that defines whether the testing library runs this test serially or in parallel.

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
struct ParallelizationTrait
```

#### Overview

When you add this trait to a parameterized test function, that test runs its cases serially instead of in parallel. This trait has no effect when you apply it to a non-parameterized test function.

When you add this trait to a test suite, that suite runs its contained test functions (including their cases, when parameterized) and sub-suites serially instead of in parallel. If the sub-suites have children, they also run serially.

This trait does not affect the execution of a test relative to its peers or to unrelated tests. This trait has no effect if you disable test parallelization globally (for example, by passing `--no-parallel` to the `swift test` command.)

To add this trait to a test, use [`serialized`](trait/serialized.md).

## Topics

### Type Aliases
- [ParallelizationTrait.TestScopeProvider](parallelizationtrait/testscopeprovider.md)
  The type of the test scope provider for this trait.
### Default Implementations
- [SuiteTrait Implementations](parallelizationtrait/suitetrait-implementations.md)
- [TestScoping Implementations](parallelizationtrait/testscoping-implementations.md)
- [Trait Implementations](parallelizationtrait/trait-implementations.md)

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
- [struct Tag](tag.md)
  A type representing a tag that can be applied to a test.
- [struct List](tag/list.md)
  A type representing one or more tags applied to a test.
- [struct TimeLimitTrait](timelimittrait.md)
  A type that defines a time limit to apply to a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/parallelizationtrait)*