# ClosedRange

**Framework**: Swift  
**Kind**: struct

An interval from a lower bound up to, and including, an upper bound.

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
struct ClosedRange<Bound> where Bound : Comparable
```

#### Overview

You create a `ClosedRange` instance by using the closed range operator (`...`).

```swift
let throughFive = 0...5
```

A `ClosedRange` instance contains both its lower bound and its upper bound.

```swift
throughFive.contains(3)
// true
throughFive.contains(10)
// false
throughFive.contains(5)
// true
```

Because a closed range includes its upper bound, a closed range whose lower bound is equal to the upper bound contains that value. Therefore, a `ClosedRange` instance cannot represent an empty range.

```swift
let zeroInclusive = 0...0
zeroInclusive.contains(0)
// true
zeroInclusive.isEmpty
// false
```

#### Using a Closed Range As a Collection of Consecutive Values

When a closed range uses integers as its lower and upper bounds, or any other type that conforms to the `Strideable` protocol with an integer stride, you can use that range in a `for`-`in` loop or with any sequence or collection method. The elements of the range are the consecutive values from its lower bound up to, and including, its upper bound.

```swift
for n in 3...5 {
    print(n)
}
// Prints "3"
// Prints "4"
// Prints "5"
```

Because floating-point types such as `Float` and `Double` are their own `Stride` types, they cannot be used as the bounds of a countable range. If you need to iterate over consecutive floating-point values, see the `stride(from:through:by:)` function.

## Topics

### Creating a Range
- [static func ... (Self, Self) -> ClosedRange<Self>](comparable/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
### Converting Ranges
- [func relative<C>(to: C) -> Range<Bound>](closedrange/relative(to:).md)
  Returns the range of indices described by this range expression within the given collection.
### Inspecting a Range
- [var isEmpty: Bool](closedrange/isempty.md)
  A Boolean value indicating whether the range contains no elements.
- [let lowerBound: Bound](closedrange/lowerbound.md)
  The range’s lower bound.
- [let upperBound: Bound](closedrange/upperbound.md)
  The range’s upper bound.
### Checking for Containment
- [static func ~= (Self, Self.Bound) -> Bool](closedrange/~=(_:_:).md)
  Returns a Boolean value indicating whether a value is included in a range.
### Clamping a Range
- [func clamped(to: ClosedRange<Bound>) -> ClosedRange<Bound>](closedrange/clamped(to:).md)
  Returns a copy of this range clamped to the given limiting range.
### Comparing Ranges
- [static func == (ClosedRange<Bound>, ClosedRange<Bound>) -> Bool](closedrange/==(_:_:).md)
  Returns a Boolean value indicating whether two ranges are equal.
- [static func != (Self, Self) -> Bool](closedrange/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func overlaps(Range<Bound>) -> Bool](closedrange/overlaps(_:)-947dt.md)
  Returns a Boolean value indicating whether this range and the given range contain an element in common.
- [func overlaps(ClosedRange<Bound>) -> Bool](closedrange/overlaps(_:)-7dfep.md)
  Returns a Boolean value indicating whether this range and the given closed range contain an element in common.
### Manipulating Indices
- [func hash(into: inout Hasher)](closedrange/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Describing a Range
- [var description: String](closedrange/description.md)
  A textual representation of the range.
- [var debugDescription: String](closedrange/debugdescription.md)
  A textual representation of the range, suitable for debugging.
- [var customMirror: Mirror](closedrange/custommirror.md)
  The custom mirror for this instance.
### Encoding and Decoding a Range
- [func encode(to: any Encoder) throws](closedrange/encode(to:).md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](closedrange/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Infrequently Used Functionality
- [init(uncheckedBounds: (lower: Bound, upper: Bound))](closedrange/init(uncheckedbounds:).md)
  Creates an instance with the given bounds.
- [var hashValue: Int](closedrange/hashvalue.md)
  The hash value.
### Initializers
- [init(Range<Bound>)](closedrange/init(_:)-er19.md)
  Creates an instance equivalent to the given `Range`.
- [init(ClosedRange<Bound>)](closedrange/init(_:)-rhzn.md)
  Now that Range is conditionally a collection when Bound: Strideable, CountableRange is no longer needed. This is a deprecated initializer for any remaining uses of Range(countableRange).
### Instance Methods
- [func contains(Range<Bound>) -> Bool](closedrange/contains(_:)-29358.md)
  Returns a Boolean value indicating whether the given range is contained within this closed range.
- [func contains(ClosedRange<Bound>) -> Bool](closedrange/contains(_:)-822cl.md)
  Returns a Boolean value indicating whether the given closed range is contained within this closed range.
### Default Implementations
- [BidirectionalCollection Implementations](closedrange/bidirectionalcollection-implementations.md)
- [Collection Implementations](closedrange/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](closedrange/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](closedrange/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](closedrange/customstringconvertible-implementations.md)
- [CustomTestStringConvertible Implementations](closedrange/customteststringconvertible-implementations.md)
- [Decodable Implementations](closedrange/decodable-implementations.md)
- [Encodable Implementations](closedrange/encodable-implementations.md)
- [Equatable Implementations](closedrange/equatable-implementations.md)
- [Hashable Implementations](closedrange/hashable-implementations.md)
- [RangeExpression Implementations](closedrange/rangeexpression-implementations.md)
- [Sequence Implementations](closedrange/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [CustomTestStringConvertible](../Testing/CustomTestStringConvertible.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [MLShapedArrayRangeExpression](../CoreML/MLShapedArrayRangeExpression.md)
- [MLTensorRangeExpression](../CoreML/MLTensorRangeExpression.md)
- [PositionScaleRange](../Charts/PositionScaleRange.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [RangeExpression](rangeexpression.md)
- [ScaleDomain](../Charts/ScaleDomain.md)
- [ScaleRange](../Charts/ScaleRange.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)

## See Also

- [static func ..< (Self, Self) -> Range<Self>](comparable/'.._(_:_:).md)
  Returns a half-open range that contains its lower bound but not its upper bound.
- [struct Range](range.md)
  A half-open interval from a lower bound up to, but not including, an upper bound.
- [struct RangeSet](rangeset.md)
  A set of values of any comparable type, represented by ranges.
- [static func ... (Self, Self) -> ClosedRange<Self>](comparable/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange)*