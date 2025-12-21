# PartialRangeThrough

**Framework**: Swift  
**Kind**: struct

A partial interval up to, and including, an upper bound.

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
struct PartialRangeThrough<Bound> where Bound : Comparable
```

#### Overview

You create `PartialRangeThrough` instances by using the prefix closed range operator (prefix `...`).

```swift
let throughFive = ...5.0
```

You can use a `PartialRangeThrough` instance to quickly check if a value is contained in a particular range of values. For example:

```swift
throughFive.contains(4.0)     // true
throughFive.contains(5.0)     // true
throughFive.contains(6.0)     // false
```

You can use a `PartialRangeThrough` instance of a collection’s indices to represent the range from the start of the collection up to, and including, the partial range’s upper bound.

```swift
let numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[...3])
// Prints "[10, 20, 30, 40]"
```

## Topics

### Initializers
- [init(Bound)](partialrangethrough/init(_:).md)
### Instance Properties
- [let upperBound: Bound](partialrangethrough/upperbound.md)
### Default Implementations
- [Decodable Implementations](partialrangethrough/decodable-implementations.md)
- [Encodable Implementations](partialrangethrough/encodable-implementations.md)
- [RangeExpression Implementations](partialrangethrough/rangeexpression-implementations.md)

## Relationships

### Conforms To
- [BNNSGraph.Builder.SliceIndex](../Accelerate/BNNSGraph/Builder/SliceIndex.md)
- [Copyable](copyable.md)
- [CustomTestStringConvertible](../Testing/CustomTestStringConvertible.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [MLShapedArrayRangeExpression](../CoreML/MLShapedArrayRangeExpression.md)
- [MLTensorRangeExpression](../CoreML/MLTensorRangeExpression.md)
- [RangeExpression](rangeexpression.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct PartialRangeUpTo](partialrangeupto.md)
  A partial half-open interval up to, but not including, an upper bound.
- [struct PartialRangeFrom](partialrangefrom.md)
  A partial interval extending upward from a lower bound.
- [protocol RangeExpression](rangeexpression.md)
  A type that can be used to slice a collection.
- [enum UnboundedRange_](unboundedrange_.md)
  A range expression that represents the entire range of a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/partialrangethrough)*