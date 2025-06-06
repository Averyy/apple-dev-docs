# FixedWidthInteger

**Framework**: Swift  
**Kind**: protocol

An integer type that uses a fixed size for every instance.

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
protocol FixedWidthInteger : BinaryInteger, LosslessStringConvertible where Self.Magnitude : FixedWidthInteger, Self.Magnitude : UnsignedInteger, Self.Stride : FixedWidthInteger, Self.Stride : SignedInteger
```

#### Overview

The `FixedWidthInteger` protocol adds binary bitwise operations, bit shifts, and overflow handling to the operations supported by the `BinaryInteger` protocol.

Use the `FixedWidthInteger` protocol as a constraint or extension point when writing operations that depend on bit shifting, performing bitwise operations, catching overflows, or having access to the maximum or minimum representable value of a type. For example, the following code provides a `binaryString` property on every fixed-width integer that represents the number’s binary representation, split into 8-bit chunks.

```swift
extension FixedWidthInteger {
    var binaryString: String {
        var result: [String] = []
        for i in 0..<(Self.bitWidth / 8) {
            let byte = UInt8(truncatingIfNeeded: self >> (i * 8))
            let byteString = String(byte, radix: 2)
            let padding = String(repeating: "0",
                                 count: 8 - byteString.count)
            result.append(padding + byteString)
        }
        return "0b" + result.reversed().joined(separator: "_")
    }
}

print(Int16.max.binaryString)
// Prints "0b01111111_11111111"
print((101 as UInt8).binaryString)
// Prints "0b01100101"
```

The `binaryString` implementation uses the static `bitWidth` property and the right shift operator (`>>`), both of which are available to any type that conforms to the `FixedWidthInteger` protocol.

The next example declares a generic `squared` function, which accepts an instance `x` of any fixed-width integer type. The function uses the `multipliedReportingOverflow(by:)` method to multiply `x` by itself and check whether the result is too large to represent in the same type.

```swift
func squared<T: FixedWidthInteger>(_ x: T) -> T? {
    let (result, overflow) = x.multipliedReportingOverflow(by: x)
    if overflow {
        return nil
    }
    return result
}

let (x, y): (Int8, Int8) = (9, 123)
print(squared(x))
// Prints "Optional(81)"
print(squared(y))
// Prints "nil"
```

### Conforming to the Fixedwidthinteger Protocol

To make your own custom type conform to the `FixedWidthInteger` protocol, declare the required initializers, properties, and methods. The required methods that are suffixed with `ReportingOverflow` serve as the customization points for arithmetic operations. When you provide just those methods, the standard library provides default implementations for all other arithmetic methods and operators.

## Topics

### Operators
- [static func &* (Self, Self) -> Self](fixedwidthinteger/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](fixedwidthinteger/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](fixedwidthinteger/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](fixedwidthinteger/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](fixedwidthinteger/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](fixedwidthinteger/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &>> (Self, Self) -> Self](fixedwidthinteger/&__(_:_:)-1sn91.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](fixedwidthinteger/&__(_:_:)-4j1s7.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>>= (inout Self, Self)](fixedwidthinteger/&__=(_:_:)-2ffyd.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= (inout Self, Self)](fixedwidthinteger/&__=(_:_:)-q186.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init?<S>(S, radix: Int)](fixedwidthinteger/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](fixedwidthinteger/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init(littleEndian: Self)](fixedwidthinteger/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](fixedwidthinteger/bigendian.md)
  The big-endian representation of this integer.
- [var byteSwapped: Self](fixedwidthinteger/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var leadingZeroBitCount: Int](fixedwidthinteger/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var littleEndian: Self](fixedwidthinteger/littleendian.md)
  The little-endian representation of this integer.
- [var nonzeroBitCount: Int](fixedwidthinteger/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
### Instance Methods
- [func addingReportingOverflow(Self) -> (partialValue: Self, overflow: Bool)](fixedwidthinteger/addingreportingoverflow(_:).md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: Self) -> (partialValue: Self, overflow: Bool)](fixedwidthinteger/dividedreportingoverflow(by:).md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividingFullWidth((high: Self, low: Self.Magnitude)) -> (quotient: Self, remainder: Self)](fixedwidthinteger/dividingfullwidth(_:).md)
  Returns a tuple containing the quotient and remainder obtained by dividing the given value by this value.
- [func multipliedFullWidth(by: Self) -> (high: Self, low: Self.Magnitude)](fixedwidthinteger/multipliedfullwidth(by:).md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: Self) -> (partialValue: Self, overflow: Bool)](fixedwidthinteger/multipliedreportingoverflow(by:).md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: Self) -> (partialValue: Self, overflow: Bool)](fixedwidthinteger/remainderreportingoverflow(dividingby:).md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func subtractingReportingOverflow(Self) -> (partialValue: Self, overflow: Bool)](fixedwidthinteger/subtractingreportingoverflow(_:).md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Properties
- [static var bitWidth: Int](fixedwidthinteger/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
- [static var max: Self](fixedwidthinteger/max.md)
  The maximum representable integer in this type.
- [static var min: Self](fixedwidthinteger/min.md)
  The minimum representable integer in this type.
### Type Methods
- [static func random(in: Range<Self>) -> Self](fixedwidthinteger/random(in:)-3uaq4.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](fixedwidthinteger/random(in:)-467fr.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](fixedwidthinteger/random(in:using:)-33n1n.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](fixedwidthinteger/random(in:using:)-4byak.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.

## Relationships

### Inherits From
- [AdditiveArithmetic](additivearithmetic.md)
- [BinaryInteger](binaryinteger.md)
- [Comparable](comparable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
- [Hashable](hashable.md)
- [LosslessStringConvertible](losslessstringconvertible.md)
- [Numeric](numeric.md)
- [Strideable](strideable.md)
### Conforming Types
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

## See Also

- [protocol BinaryInteger](binaryinteger.md)
  An integer type with a binary representation.
- [protocol SignedInteger](signedinteger.md)
  An integer type that can represent both positive and negative values.
- [protocol UnsignedInteger](unsignedinteger.md)
  An integer type that can represent only nonnegative values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/fixedwidthinteger)*