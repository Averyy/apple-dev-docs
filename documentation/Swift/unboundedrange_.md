# UnboundedRange_

**Framework**: Swift  
**Kind**: enum  
**Role**: Enumeration

A range expression that represents the entire range of a collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
enum UnboundedRange_
```

## Overview

You can use the unbounded range operator (`...`) to create a slice of a collection that contains all of the collection’s elements. Slicing with an unbounded range is essentially a conversion of a collection instance into its slice type.

For example, the following code declares `countLetterChanges(_:_:)`, a function that finds the number of changes required to change one word or phrase into another. The function uses a recursive approach to perform the same comparisons on smaller and smaller pieces of the original strings. In order to use recursion without making copies of the strings at each step, `countLetterChanges(_:_:)` uses `Substring`, a string’s slice type, for its parameters.

```swift
func countLetterChanges(_ s1: Substring, _ s2: Substring) -> Int {
    if s1.isEmpty { return s2.count }
    if s2.isEmpty { return s1.count }

    let cost = s1.first == s2.first ? 0 : 1

    return min(
        countLetterChanges(s1.dropFirst(), s2) + 1,
        countLetterChanges(s1, s2.dropFirst()) + 1,
        countLetterChanges(s1.dropFirst(), s2.dropFirst()) + cost)
}
```

To call `countLetterChanges(_:_:)` with two strings, use an unbounded range in each string’s subscript.

```swift
let word1 = "grizzly"
let word2 = "grisly"
let changes = countLetterChanges(word1[...], word2[...])
// changes == 2
```

## Topics

### Creating an Unbounded Range
- [static func ... (UnboundedRange_)](./unboundedrange_/dotdotdot%28_%29.md)
  Creates an unbounded range expression.
- [typealias UnboundedRange](./unboundedrange.md)
  The type of an unbounded range operator.

## Relationships

### Conforms To
- [BitwiseCopyable](./bitwisecopyable.md)
- [Copyable](./copyable.md)
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)

## See Also

### Range Expressions
- [struct PartialRangeUpTo](./partialrangeupto.md)
  A partial half-open interval up to, but not including, an upper bound.
- [struct PartialRangeThrough](./partialrangethrough.md)
  A partial interval up to, and including, an upper bound.
- [struct PartialRangeFrom](./partialrangefrom.md)
  A partial interval extending upward from a lower bound.
- [protocol RangeExpression](./rangeexpression.md)
  A type that can be used to slice a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unboundedrange_)*