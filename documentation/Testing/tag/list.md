# Tag.List

**Framework**: Swift Testing  
**Kind**: struct

A type representing one or more tags applied to a test.

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
struct List
```

#### Overview

To add this trait to a test, use the [`tags(_:)`](trait/tags(_:).md) function.

## Topics

### Instance Properties
- [var tags: [Tag]](tag/list/tags.md)
  The list of tags contained in this instance.
### Default Implementations
- [CustomStringConvertible Implementations](tag/list/customstringconvertible-implementations.md)
- [Equatable Implementations](tag/list/equatable-implementations.md)
- [Hashable Implementations](tag/list/hashable-implementations.md)
- [SuiteTrait Implementations](tag/list/suitetrait-implementations.md)
- [Trait Implementations](tag/list/trait-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [struct TimeLimitTrait](timelimittrait.md)
  A type that defines a time limit to apply to a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/tag/list)*