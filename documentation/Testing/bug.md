# Bug

**Framework**: Swift Testing  
**Kind**: struct

A type that represents a bug report tracked by a test.

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
struct Bug
```

## Mentions

- [Interpreting bug identifiers](bugidentifiers.md)
- [Adding comments to tests](addingcomments.md)

#### Overview

To add this trait to a test, use one of the following functions:

- [`bug(_:_:)`](trait/bug(_:_:).md)
- [`bug(_:id:_:)`](trait/bug(_:id:_:)-10yf5.md)
- [`bug(_:id:_:)`](trait/bug(_:id:_:)-3vtpl.md)

## Topics

### Instance Properties
- [var id: String?](bug/id.md)
  A unique identifier in this bug’s associated bug-tracking system, if available.
- [var title: Comment?](bug/title.md)
  The human-readable title of the bug, if specified by the test author.
- [var url: String?](bug/url.md)
  A URL that links to more information about the bug, if available.
### Default Implementations
- [Decodable Implementations](bug/decodable-implementations.md)
- [Encodable Implementations](bug/encodable-implementations.md)
- [Equatable Implementations](bug/equatable-implementations.md)
- [Hashable Implementations](bug/hashable-implementations.md)
- [SuiteTrait Implementations](bug/suitetrait-implementations.md)
- [Trait Implementations](bug/trait-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SuiteTrait](suitetrait.md)
- [TestTrait](testtrait.md)
- [Trait](trait.md)

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/testing/bug)*