# Tag

**Framework**: Swift Testing  
**Kind**: struct  
**Role**: Structure

A type representing a tag that can be applied to a test.

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
struct Tag
```

## Mentions

- [Adding tags to tests](./addingtags.md)

## Overview

To apply tags to a test, use the [`tags(_:)`](./trait/tags%28_%29.md) function.

## Topics

### Structures
- [struct List](./tag/list.md)
  A type representing one or more tags applied to a test.

## Relationships

### Conforms To
- [CodingKeyRepresentable](../Swift/codingkeyrepresentable.md)
- [Comparable](../Swift/comparable.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [struct Bug](./bug.md)
  A type that represents a bug report tracked by a test.
- [struct Comment](./comment.md)
  A type that represents a comment related to a test.
- [struct ConditionTrait](./conditiontrait.md)
  A type that defines a condition which must be satisfied for the testing library to enable a test.
- [struct IssueHandlingTrait](./issuehandlingtrait.md)
  A type that allows transforming or filtering the issues recorded by a test.
- [struct ParallelizationTrait](./parallelizationtrait.md)
  A type that defines whether the testing library runs this test serially or in parallel.
- [struct List](./tag/list.md)
  A type representing one or more tags applied to a test.
- [struct TimeLimitTrait](./timelimittrait.md)
  A type that defines a time limit to apply to a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/tag)*