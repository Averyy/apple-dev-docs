# Comment

**Framework**: Swift Testing  
**Kind**: struct  
**Role**: Structure

A type that represents a comment related to a test.

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
struct Comment
```

#### Overview

Use this type to provide context or background information about a test’s purpose, explain how a complex test operates, or include details which may be helpful when diagnosing issues recorded by a test.

To add a comment to a test or suite, add a code comment before its `@Test` or `@Suite` attribute. See [Adding comments to tests](./addingcomments.md) for more details.

> **Note**: To reference bugs related to a test, use [`bug(_:_:)`](./trait/bug%28_,_%29.md), [`bug(_:id:_:)`](./trait/bug%28_,id,_%29-10yf5.md), or [`bug(_:id:_:)`](./trait/bug%28_,id,_%29-3vtpl.md).

## Topics

### Instance Properties
- [var rawValue: String](./comment/rawvalue.md)
  The single comment string that this comment contains.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringInterpolation](../Swift/expressiblebystringinterpolation.md)
- [ExpressibleByStringLiteral](../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SuiteTrait](./suitetrait.md)
- [TestTrait](./testtrait.md)
- [Trait](./trait.md)

## See Also

### Supporting types
- [struct Bug](./bug.md)
  A type that represents a bug report tracked by a test.
- [struct ConditionTrait](./conditiontrait.md)
  A type that defines a condition which must be satisfied for the testing library to enable a test.
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

*[View on Apple Developer](https://developer.apple.com/documentation/testing/comment)*