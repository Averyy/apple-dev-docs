# PartialRangeUpTo

**Framework**: Swift  
**Kind**: struct

A partial half-open interval up to, but not including, an upper bound.

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
struct PartialRangeUpTo<Bound> where Bound : Comparable
```

#### Overview

You create `PartialRangeUpTo` instances by using the prefix half-open range operator (prefix `..<`).

```swift
let upToFive = ..<5.0
```

You can use a `PartialRangeUpTo` instance to quickly check if a value is contained in a particular range of values. For example:

```swift
upToFive.contains(3.14)       // true
upToFive.contains(6.28)       // false
upToFive.contains(5.0)        // false
```

You can use a `PartialRangeUpTo` instance of a collection’s indices to represent the range from the start of the collection up to, but not including, the partial range’s upper bound.

```swift
let numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[..<3])
// Prints "[10, 20, 30]"
```

## Topics

### Initializers
- [init(Bound)](partialrangeupto/init(_:).md)
### Instance Properties
- [let upperBound: Bound](partialrangeupto/upperbound.md)
### Default Implementations
- [CustomTestStringConvertible Implementations](partialrangeupto/customteststringconvertible-implementations.md)
- [Decodable Implementations](partialrangeupto/decodable-implementations.md)
- [Encodable Implementations](partialrangeupto/encodable-implementations.md)
- [RangeExpression Implementations](partialrangeupto/rangeexpression-implementations.md)

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

- [struct PartialRangeThrough](partialrangethrough.md)
  A partial interval up to, and including, an upper bound.
- [struct PartialRangeFrom](partialrangefrom.md)
  A partial interval extending upward from a lower bound.
- [protocol RangeExpression](rangeexpression.md)
  A type that can be used to slice a collection.
- [enum UnboundedRange_](unboundedrange_.md)
  A range expression that represents the entire range of a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/partialrangeupto)*