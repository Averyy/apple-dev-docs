# Range

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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

## Overview

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

## Using a Range as a Collection of Consecutive Values

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
- [static func ..< (Self, Self) -> Range<Self>](./comparable/dotdotop%28_,_%29.md)
  Returns a half-open range that contains its lower bound but not its upper bound.
### Converting Ranges
- [func relative<C>(to: C) -> Range<Bound>](./range/relative%28to%29.md)
  Returns the range of indices described by this range expression within the given collection.
- [init?(NSRange, in: String)](./range/init%28_,in%29-5cclx.md)
- [init?<S>(NSRange, in: S)](./range/init%28_,in%29-5qfor.md)
### Inspecting a Range
- [var isEmpty: Bool](./range/isempty.md)
  A Boolean value indicating whether the range contains no elements.
- [let lowerBound: Bound](./range/lowerbound.md)
  The range’s lower bound.
- [let upperBound: Bound](./range/upperbound.md)
  The range’s upper bound.
### Checking for Containment
- [static func ~= (Self, Self.Bound) -> Bool](./range/tildeeq%28_,_%29.md)
  Returns a Boolean value indicating whether a value is included in a range.
### Clamping a Range
- [func clamped(to: Range<Bound>) -> Range<Bound>](./range/clamped%28to%29.md)
  Returns a copy of this range clamped to the given limiting range.
### Working with Foundation Ranges
- [init?(NSRange)](./range/init%28_%29-15u6b.md)
- [init?(NSRange)](./range/init%28_%29-1q7lu.md)
### Comparing Ranges
- [static func == (Range<Bound>, Range<Bound>) -> Bool](./range/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two ranges are equal.
- [static func != (borrowing Self, borrowing Self) -> Bool](./range/noteq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are not equal.
- [func overlaps(Range<Bound>) -> Bool](./range/overlaps%28_%29-7osha.md)
  Returns a Boolean value indicating whether this range and the given range contain an element in common.
- [func overlaps(ClosedRange<Bound>) -> Bool](./range/overlaps%28_%29-9fkb2.md)
  Returns a Boolean value indicating whether this range and the given closed range contain an element in common.
### Manipulating Indices
- [func hash(into: inout Hasher)](./range/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Describing a Range
- [var description: String](./range/description.md)
  A textual representation of the range.
- [var debugDescription: String](./range/debugdescription.md)
  A textual representation of the range, suitable for debugging.
- [var customMirror: Mirror](./range/custommirror.md)
  The custom mirror for this instance.
### Encoding and Decoding a Range
- [func encode(to: any Encoder) throws](./range/encode%28to%29.md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](./range/init%28from%29.md)
  Creates a new instance by decoding from the given decoder.
### Infrequently Used Functionality
- [init(uncheckedBounds: (lower: Bound, upper: Bound))](./range/init%28uncheckedbounds%29.md)
  Creates an instance with the given bounds.
- [var hashValue: Int](./range/hashvalue.md)
  The hash value.
### Initializers
- [init(Range<Bound>)](./range/init%28_%29-35b1j.md)
  Now that Range is conditionally a collection when Bound: Strideable, CountableRange is no longer needed. This is a deprecated initializer for any remaining uses of Range(countableRange).
- [init(ClosedRange<Bound>)](./range/init%28_%29-79g1a.md)
  Creates an instance equivalent to the given `ClosedRange`.
- [init?<S>(NSRange, in: S)](./range/init%28_,in%29-24465.md)
- [init?<R, S>(R, in: S)](./range/init%28_,in%29-612lr.md)
- [init?<R, S>(R, in: S)](./range/init%28_,in%29-75xo3.md)
- [init?<S>(AttributedString.MarkdownSourcePosition, in: S)](./range/init%28_,in%29-9vre5.md)
### Instance Methods
- [func contains(Range<Bound>) -> Bool](./range/contains%28_%29-4xxju.md)
  Returns a Boolean value indicating whether the given range is contained within this range.
- [func contains(ClosedRange<Bound>) -> Bool](./range/contains%28_%29-680jp.md)
  Returns a Boolean value indicating whether the given closed range is contained within this range.
- [func contains(Bound) -> Bool](./range/contains%28_%29-76nb4.md)
  Returns a Boolean value indicating whether the given element is contained within the range.
- [func formatted() -> String](./range/formatted%28%29.md)
  Formats the date range as an interval.
- [func formatted<S>(S) -> S.FormatOutput](./range/formatted%28_%29.md)
  Formats the date range using the specified style.
- [func formatted(date: Date.IntervalFormatStyle.DateStyle, time: Date.IntervalFormatStyle.TimeStyle) -> String](./range/formatted%28date,time%29.md)
  Formats the date range using the specified date and time format styles.
- [func isValid(within: some AttributedStringProtocol) -> Bool](./range/isvalid%28within%29-2fba2.md)
  Indicates whether the range is valid for use with the provided attributed string.
- [func isValid(within: DiscontiguousAttributedSubstring) -> Bool](./range/isvalid%28within%29-8h4h8.md)
  Indicates whether the range is valid for use with the provided discontiguous attributed string.
### Type Methods
- [static func upToNextMajor(from: Version) -> Range<Bound>](./range/uptonextmajor%28from%29.md)
  Returns a requirement for a version range, starting at the given minimum version and going up to the next major version. This is the recommended version requirement.
- [static func upToNextMinor(from: Version) -> Range<Bound>](./range/uptonextminor%28from%29.md)
  Returns a requirement for a version range, starting at the given minimum version and going up to the next minor version.
### Default Implementations
- [BidirectionalCollection Implementations](./range/bidirectionalcollection-implementations.md)
- [Collection Implementations](./range/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](./range/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](./range/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./range/customstringconvertible-implementations.md)
- [Decodable Implementations](./range/decodable-implementations.md)
- [Encodable Implementations](./range/encodable-implementations.md)
- [Equatable Implementations](./range/equatable-implementations.md)
- [Hashable Implementations](./range/hashable-implementations.md)
- [RangeExpression Implementations](./range/rangeexpression-implementations.md)
- [Sequence Implementations](./range/sequence-implementations.md)

## Relationships

### Conforms To
- [BNNSGraph.Builder.SliceIndex](../Accelerate/bnnsgraph/builder/sliceindex.md)
- [BidirectionalCollection](./bidirectionalcollection.md)
- [Collection](./collection.md)
- [ConvertibleToBytes](./convertibletobytes.md)
- [Copyable](./copyable.md)
- [CustomDebugStringConvertible](./customdebugstringconvertible.md)
- [CustomReflectable](./customreflectable.md)
- [CustomStringConvertible](./customstringconvertible.md)
- [CustomTestStringConvertible](../Testing/customteststringconvertible.md)
- [Decodable](./decodable.md)
- [Encodable](./encodable.md)
- [Equatable](./equatable.md)
- [Escapable](./escapable.md)
- [Hashable](./hashable.md)
- [HomeAccessoryRangeSettingDescriptor](../homeextensions/homeaccessoryrangesettingdescriptor.md)
- [MLShapedArrayRangeExpression](../CoreML/mlshapedarrayrangeexpression.md)
- [MLTensorRangeExpression](../CoreML/mltensorrangeexpression.md)
- [NDArray.RangeExpression](../CoreAI/ndarray/rangeexpression.md)
- [RandomAccessCollection](./randomaccesscollection.md)
- [RangeExpression](./rangeexpression.md)
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)
- [Sequence](./sequence.md)

## See Also

### Ranges
- [static func ..< (Self, Self) -> Range<Self>](./comparable/dotdotop%28_,_%29.md)
  Returns a half-open range that contains its lower bound but not its upper bound.
- [struct RangeSet](./rangeset.md)
  A set of values of any comparable type, represented by ranges.
- [static func ... (Self, Self) -> ClosedRange<Self>](./comparable/dotdotdot%28_,_%29.md)
  Returns a closed range that contains both of its bounds.
- [struct ClosedRange](./closedrange.md)
  An interval from a lower bound up to, and including, an upper bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range)*