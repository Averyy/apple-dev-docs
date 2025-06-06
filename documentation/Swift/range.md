# Range

**Framework**: Swift  
**Kind**: struct

A half-open interval from a lower bound up to, but not including, an upper bound.

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
struct Range<Bound> where Bound : Comparable
```

#### Overview

You create a `Range` instance by using the half-open range operator (`..<`).

```swift
let underFive = 0.0..<5.0
```

You can use a `Range` instance to quickly check if a value is contained in a particular range of values. For example:

```swift
underFive.contains(3.14)
// true
underFive.contains(6.28)
// false
underFive.contains(5.0)
// false
```

`Range` instances can represent an empty interval, unlike `ClosedRange`.

```swift
let empty = 0.0..<0.0
empty.contains(0.0)
// false
empty.isEmpty
// true
```

#### Using a Range As a Collection of Consecutive Values

When a range uses integers as its lower and upper bounds, or any other type that conforms to the `Strideable` protocol with an integer stride, you can use that range in a `for`-`in` loop or with any sequence or collection method. The elements of the range are the consecutive values from its lower bound up to, but not including, its upper bound.

```swift
for n in 3..<5 {
    print(n)
}
// Prints "3"
// Prints "4"
```

Because floating-point types such as `Float` and `Double` are their own `Stride` types, they cannot be used as the bounds of a countable range. If you need to iterate over consecutive floating-point values, see the `stride(from:to:by:)` function.

## Topics

### Creating a Range
- [static func ..< (Self, Self) -> Range<Self>](comparable/'.._(_:_:).md)
  Returns a half-open range that contains its lower bound but not its upper bound.
### Converting Ranges
- [func relative<C>(to: C) -> Range<Bound>](range/relative(to:).md)
  Returns the range of indices described by this range expression within the given collection.
- [init?(NSRange, in: String)](range/init(_:in:)-5cclx.md)
- [init?<S>(NSRange, in: S)](range/init(_:in:)-5qfor.md)
### Inspecting a Range
- [var isEmpty: Bool](range/isempty.md)
  A Boolean value indicating whether the range contains no elements.
- [let lowerBound: Bound](range/lowerbound.md)
  The range’s lower bound.
- [let upperBound: Bound](range/upperbound.md)
  The range’s upper bound.
### Checking for Containment
- [static func ~= (Self, Self.Bound) -> Bool](range/~=(_:_:).md)
  Returns a Boolean value indicating whether a value is included in a range.
### Clamping a Range
- [func clamped(to: Range<Bound>) -> Range<Bound>](range/clamped(to:).md)
  Returns a copy of this range clamped to the given limiting range.
### Working with Foundation Ranges
- [init?(NSRange)](range/init(_:)-15u6b.md)
- [init?(NSRange)](range/init(_:)-1q7lu.md)
### Comparing Ranges
- [static func == (Range<Bound>, Range<Bound>) -> Bool](range/==(_:_:).md)
  Returns a Boolean value indicating whether two ranges are equal.
- [static func != (Self, Self) -> Bool](range/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func overlaps(Range<Bound>) -> Bool](range/overlaps(_:)-7osha.md)
  Returns a Boolean value indicating whether this range and the given range contain an element in common.
- [func overlaps(ClosedRange<Bound>) -> Bool](range/overlaps(_:)-9fkb2.md)
  Returns a Boolean value indicating whether this range and the given closed range contain an element in common.
### Manipulating Indices
- [func hash(into: inout Hasher)](range/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Describing a Range
- [var description: String](range/description.md)
  A textual representation of the range.
- [var debugDescription: String](range/debugdescription.md)
  A textual representation of the range, suitable for debugging.
- [var customMirror: Mirror](range/custommirror.md)
  The custom mirror for this instance.
### Encoding and Decoding a Range
- [func encode(to: any Encoder) throws](range/encode(to:).md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](range/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Infrequently Used Functionality
- [init(uncheckedBounds: (lower: Bound, upper: Bound))](range/init(uncheckedbounds:).md)
  Creates an instance with the given bounds.
- [var hashValue: Int](range/hashvalue.md)
  The hash value.
### Initializers
- [init(Range<Bound>)](range/init(_:)-35b1j.md)
  Now that Range is conditionally a collection when Bound: Strideable, CountableRange is no longer needed. This is a deprecated initializer for any remaining uses of Range(countableRange).
- [init(ClosedRange<Bound>)](range/init(_:)-79g1a.md)
  Creates an instance equivalent to the given `ClosedRange`.
- [init?<S>(NSRange, in: S)](range/init(_:in:)-24465.md)
- [init?<R, S>(R, in: S)](range/init(_:in:)-612lr.md)
- [init?<R, S>(R, in: S)](range/init(_:in:)-75xo3.md)
- [init?<S>(AttributedString.MarkdownSourcePosition, in: S)](range/init(_:in:)-9vre5.md)
### Instance Methods
- [func contains(Range<Bound>) -> Bool](range/contains(_:)-4xxju.md)
  Returns a Boolean value indicating whether the given range is contained within this range.
- [func contains(ClosedRange<Bound>) -> Bool](range/contains(_:)-680jp.md)
  Returns a Boolean value indicating whether the given closed range is contained within this range.
- [func contains(Bound) -> Bool](range/contains(_:)-76nb4.md)
  Returns a Boolean value indicating whether the given element is contained within the range.
- [func formatted() -> String](range/formatted.md)
  Formats the date range as an interval.
- [func formatted<S>(S) -> S.FormatOutput](range/formatted(_:).md)
  Formats the date range using the specified style.
- [func formatted(date: Date.IntervalFormatStyle.DateStyle, time: Date.IntervalFormatStyle.TimeStyle) -> String](range/formatted(date:time:).md)
  Formats the date range using the specified date and time format styles.
### Type Methods
- [static func upToNextMajor(from: Version) -> Range<Bound>](range/uptonextmajor(from:).md)
  Returns a requirement for a version range, starting at the given minimum version and going up to the next major version. This is the recommended version requirement.
- [static func upToNextMinor(from: Version) -> Range<Bound>](range/uptonextminor(from:).md)
  Returns a requirement for a version range, starting at the given minimum version and going up to the next minor version.
### Default Implementations
- [BidirectionalCollection Implementations](range/bidirectionalcollection-implementations.md)
- [Collection Implementations](range/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](range/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](range/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](range/customstringconvertible-implementations.md)
- [CustomTestStringConvertible Implementations](range/customteststringconvertible-implementations.md)
- [Decodable Implementations](range/decodable-implementations.md)
- [Encodable Implementations](range/encodable-implementations.md)
- [Equatable Implementations](range/equatable-implementations.md)
- [Hashable Implementations](range/hashable-implementations.md)
- [RangeExpression Implementations](range/rangeexpression-implementations.md)
- [Sequence Implementations](range/sequence-implementations.md)

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
- [RandomAccessCollection](randomaccesscollection.md)
- [RangeExpression](rangeexpression.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)

## See Also

- [static func ..< (Self, Self) -> Range<Self>](comparable/'.._(_:_:).md)
  Returns a half-open range that contains its lower bound but not its upper bound.
- [struct RangeSet](rangeset.md)
  A set of values of any comparable type, represented by ranges.
- [static func ... (Self, Self) -> ClosedRange<Self>](comparable/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [struct ClosedRange](closedrange.md)
  An interval from a lower bound up to, and including, an upper bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range)*