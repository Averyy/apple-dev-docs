# Strideable

**Framework**: Swift  
**Kind**: protocol

A type representing continuous, one-dimensional values that can be offset and measured.

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
protocol Strideable<Stride> : Comparable
```

#### Overview

You can use a type that conforms to the `Strideable` protocol with the `stride(from:to:by:)` and `stride(from:through:by:)` functions. For example, you can use `stride(from:to:by:)` to iterate over an interval of floating-point values:

```swift
for radians in stride(from: 0.0, to: .pi * 2, by: .pi / 2) {
    let degrees = Int(radians * 180 / .pi)
    print("Degrees: \(degrees), radians: \(radians)")
}
// Degrees: 0, radians: 0.0
// Degrees: 90, radians: 1.5707963267949
// Degrees: 180, radians: 3.14159265358979
// Degrees: 270, radians: 4.71238898038469
```

The last parameter of these functions is of the associated `Stride` type—the type that represents the distance between any two instances of the `Strideable` type.

Types that have an integer `Stride` can be used as the boundaries of a countable range or as the lower bound of an iterable one-sided range. For example, you can iterate over a range of `Int` and use sequence and collection methods.

```swift
var sum = 0
for x in 1...100 {
    sum += x
}
// sum == 5050

let digits = (0..<10).map(String.init)
// ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
```

### Conforming to the Strideable Protocol

To add `Strideable` conformance to a custom type, choose a `Stride` type that can represent the distance between two instances and implement the `advanced(by:)` and `distance(to:)` methods. For example, this hypothetical `Date` type stores its value as the number of days before or after January 1, 2000:

```swift
struct Date: Equatable, CustomStringConvertible {
    var daysAfterY2K: Int

    var description: String {
        // ...
    }
}
```

The `Stride` type for `Date` is `Int`, inferred from the parameter and return types of `advanced(by:)` and `distance(to:)`:

```swift
extension Date: Strideable {
    func advanced(by n: Int) -> Date {
        var result = self
        result.daysAfterY2K += n
        return result
    }

    func distance(to other: Date) -> Int {
        return other.daysAfterY2K - self.daysAfterY2K
    }
}
```

The `Date` type can now be used with the `stride(from:to:by:)` and `stride(from:through:by:)` functions and as the bounds of an iterable range.

```swift
let startDate = Date(daysAfterY2K: 0)   // January 1, 2000
let endDate = Date(daysAfterY2K: 15)    // January 16, 2000

for date in stride(from: startDate, to: endDate, by: 7) {
    print(date)
}
// January 1, 2000
// January 8, 2000
// January 15, 2000
```

> ❗ **Important**: The `Strideable` protocol provides default implementations for the equal-to (`==`) and less-than (`<`) operators that depend on the `Stride` type’s implementations. If a type conforming to `Strideable` is its own `Stride` type, it must provide concrete implementations of the two operators to avoid infinite recursion.

## Topics

### Getting an Offset Value
- [func advanced(by: Self.Stride) -> Self](strideable/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [static func + (Self, Self.Stride) -> Self](strideable/+(_:_:)-8m1px.md)
- [static func + (Self.Stride, Self) -> Self](strideable/+(_:_:)-94mlm.md)
- [static func - (Self, Self.Stride) -> Self](strideable/-(_:_:)-1kjns.md)
- [static func - (Self, Self) -> Self.Stride](strideable/-(_:_:)-2mot7.md)
### Comparing Values
- [func distance(to: Self) -> Self.Stride](strideable/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
### Operators
- [static func += (inout Self, Self.Stride)](strideable/+=(_:_:).md)
- [static func -= (inout Self, Self.Stride)](strideable/-=(_:_:).md)
### Associated Types
- [associatedtype Stride : Comparable, SignedNumeric](strideable/stride.md)
  A type that represents the distance between two values.

## Relationships

### Inherits From
- [Comparable](comparable.md)
- [Equatable](equatable.md)
### Inherited By
- [BinaryFloatingPoint](binaryfloatingpoint.md)
- [BinaryInteger](binaryinteger.md)
- [FixedWidthInteger](fixedwidthinteger.md)
- [FloatingPoint](floatingpoint.md)
- [SignedInteger](signedinteger.md)
- [UnsignedInteger](unsignedinteger.md)
### Conforming Types
- [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md)
- [Double](double.md)
- [Float](float.md)
- [Float16](float16.md)
- [Float80](float80.md)
- [Int](int.md)
- [Int128](int128.md)
- [Int16](int16.md)
- [Int32](int32.md)
- [Int64](int64.md)
- [Int8](int8.md)
- [UInt](uint.md)
- [UInt128](uint128.md)
- [UInt16](uint16.md)
- [UInt32](uint32.md)
- [UInt64](uint64.md)
- [UInt8](uint8.md)
- [UnsafeMutablePointer](unsafemutablepointer.md)
- [UnsafeMutableRawPointer](unsafemutablerawpointer.md)
- [UnsafePointer](unsafepointer.md)
- [UnsafeRawPointer](unsaferawpointer.md)

## See Also

- [protocol AdditiveArithmetic](additivearithmetic.md)
  A type with values that support addition and subtraction.
- [protocol Numeric](numeric.md)
  A type with values that support multiplication.
- [protocol SignedNumeric](signednumeric.md)
  A numeric type with a negation operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/strideable)*