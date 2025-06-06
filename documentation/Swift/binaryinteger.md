# BinaryInteger

**Framework**: Swift  
**Kind**: protocol

An integer type with a binary representation.

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
protocol BinaryInteger : CustomStringConvertible, Hashable, Numeric, Strideable where Self.Magnitude : BinaryInteger, Self.Magnitude == Self.Magnitude.Magnitude
```

#### Overview

The `BinaryInteger` protocol is the basis for all the integer types provided by the standard library. All of the standard library’s integer types, such as `Int` and `UInt32`, conform to `BinaryInteger`.

### Converting Between Numeric Types

You can create new instances of a type that conforms to the `BinaryInteger` protocol from a floating-point number or another binary integer of any type. The `BinaryInteger` protocol provides initializers for four different kinds of conversion.

#### Range Checked Conversion

You use the default `init(_:)` initializer to create a new instance when you’re sure that the value passed is representable in the new type. For example, an instance of `Int16` can represent the value `500`, so the first conversion in the code sample below succeeds. That same value is too large to represent as an `Int8` instance, so the second conversion fails, triggering a runtime error.

```swift
let x: Int = 500
let y = Int16(x)
// y == 500

let z = Int8(x)
// Error: Not enough bits to represent...
```

When you create a binary integer from a floating-point value using the default initializer, the value is rounded toward zero before the range is checked. In the following example, the value `127.75` is rounded to `127`, which is representable by the `Int8` type.  `128.25` is rounded to `128`, which is not representable as an `Int8` instance, triggering a runtime error.

```swift
let e = Int8(127.75)
// e == 127

let f = Int8(128.25)
// Error: Double value cannot be converted...
```

#### Exact Conversion

Use the `init?(exactly:)` initializer to create a new instance after checking whether the passed value is representable. Instead of trapping on out-of-range values, using the failable `init?(exactly:)` initializer results in `nil`.

```swift
let x = Int16(exactly: 500)
// x == Optional(500)

let y = Int8(exactly: 500)
// y == nil
```

When converting floating-point values, the `init?(exactly:)` initializer checks both that the passed value has no fractional part and that the value is representable in the resulting type.

```swift
let e = Int8(exactly: 23.0)       // integral value, representable
// e == Optional(23)

let f = Int8(exactly: 23.75)      // fractional value, representable
// f == nil

let g = Int8(exactly: 500.0)      // integral value, nonrepresentable
// g == nil
```

#### Clamping Conversion

Use the `init(clamping:)` initializer to create a new instance of a binary integer type where out-of-range values are clamped to the representable range of the type. For a type `T`, the resulting value is in the range `T.min...T.max`.

```swift
let x = Int16(clamping: 500)
// x == 500

let y = Int8(clamping: 500)
// y == 127

let z = UInt8(clamping: -500)
// z == 0
```

#### Bit Pattern Conversion

Use the `init(truncatingIfNeeded:)` initializer to create a new instance with the same bit pattern as the passed value, extending or truncating the value’s representation as necessary. Note that the value may not be preserved, particularly when converting between signed to unsigned integer types or when the destination type has a smaller bit width than the source type. The following example shows how extending and truncating work for nonnegative integers:

```swift
let q: Int16 = 850
// q == 0b00000011_01010010

let r = Int8(truncatingIfNeeded: q)      // truncate 'q' to fit in 8 bits
// r == 82
//   == 0b01010010

let s = Int16(truncatingIfNeeded: r)     // extend 'r' to fill 16 bits
// s == 82
//   == 0b00000000_01010010
```

Any padding is performed by  the passed value. When nonnegative integers are extended, the result is padded with zeroes. When negative integers are extended, the result is padded with ones. This example shows several extending conversions of a negative value—note that negative values are sign-extended even when converting to an unsigned type.

```swift
let t: Int8 = -100
// t == -100
// t's binary representation == 0b10011100

let u = UInt8(truncatingIfNeeded: t)
// u == 156
// u's binary representation == 0b10011100

let v = Int16(truncatingIfNeeded: t)
// v == -100
// v's binary representation == 0b11111111_10011100

let w = UInt16(truncatingIfNeeded: t)
// w == 65436
// w's binary representation == 0b11111111_10011100
```

### Comparing Across Integer Types

You can use relational operators, such as the less-than and equal-to operators (`<` and `==`), to compare instances of different binary integer types. The following example compares instances of the `Int`, `UInt`, and `UInt8` types:

```swift
let x: Int = -23
let y: UInt = 1_000
let z: UInt8 = 23

if x < y {
    print("\(x) is less than \(y).")
}
// Prints "-23 is less than 1000."

if z > x {
    print("\(z) is greater than \(x).")
}
// Prints "23 is greater than -23."
```

## Topics

### Creating a Binary Integer
- [init()](binaryinteger/init.md)
  Creates a new value equal to zero.
### Converting Integers
- [init<T>(T)](binaryinteger/init(_:)-8gmdl.md)
  Creates a new instance from the given integer.
- [init<T>(clamping: T)](binaryinteger/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](binaryinteger/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Converting Floating-Point Values
- [init<T>(T)](binaryinteger/init(_:)-2ln0u.md)
  Creates an integer from the given floating-point value, rounding toward zero.
### Converting with No Loss of Precision
- [init?<T>(exactly: T)](binaryinteger/init(exactly:).md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
### Performing Calculations
- [Binary Integer Operators](binary-integer-operators.md)
  Perform arithmetic and bitwise operations or compare values.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](binaryinteger/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.
- [func isMultiple(of: Self) -> Bool](binaryinteger/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
### Finding the Sign and Magnitude
- [func signum() -> Self](binaryinteger/signum.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
### Accessing Numeric Constants
- [static var isSigned: Bool](binaryinteger/issigned.md)
  A Boolean value indicating whether this type is a signed integer type.
### Working with Binary Representation
- [var bitWidth: Int](binaryinteger/bitwidth.md)
  The number of bits in the current binary representation of this value.
- [var trailingZeroBitCount: Int](binaryinteger/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: Self.Words](binaryinteger/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
- [associatedtype Words : RandomAccessCollection](binaryinteger/words-swift.associatedtype.md)
  A type that represents the words of a binary integer.
### Operators
- [static func % (Self, Self) -> Self](binaryinteger/_(_:_:)-30ngi.md)
  Returns the remainder of dividing the first value by the second.
- [static func ^ (Self, Self) -> Self](binaryinteger/_(_:_:)-3qw5d.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func | (Self, Self) -> Self](binaryinteger/_(_:_:)-6qhsw.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func ^= (inout Self, Self)](binaryinteger/_=(_:_:)-1fatv.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [static func |= (inout Self, Self)](binaryinteger/_=(_:_:)-4vfmj.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func %= (inout Self, Self)](binaryinteger/_=(_:_:)-79wgi.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [static func << <RHS>(Self, RHS) -> Self](binaryinteger/__(_:_:)-28lmu.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <RHS>(Self, RHS) -> Self](binaryinteger/__(_:_:)-4vnij.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >>= <RHS>(inout Self, RHS)](binaryinteger/__=(_:_:)-5lhky.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func <<= <RHS>(inout Self, RHS)](binaryinteger/__=(_:_:)-9pzpp.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
### Initializers
- [init(String, format: IntegerFormatStyle<Self>, lenient: Bool) throws](binaryinteger/init(_:format:lenient:)-2qv61.md)
- [init(String, format: IntegerFormatStyle<Self>.Currency, lenient: Bool) throws](binaryinteger/init(_:format:lenient:)-50z9r.md)
- [init(String, format: IntegerFormatStyle<Self>.Percent, lenient: Bool) throws](binaryinteger/init(_:format:lenient:)-86j1g.md)
- [init<S>(S.ParseInput, strategy: S) throws](binaryinteger/init(_:strategy:)-207i8.md)
  Initialize an instance by parsing `value` with the given `strategy`.
### Instance Methods
- [func formatted() -> String](binaryinteger/formatted.md)
  Format `self` using `IntegerFormatStyle()`
- [func formatted<S>(S) -> S.FormatOutput](binaryinteger/formatted(_:)-4qd73.md)
  Format `self` with the given format.
- [func formatted<S>(S) -> S.FormatOutput](binaryinteger/formatted(_:)-73k3e.md)
  Format `self` with the given format. `self` is first converted to `S.FormatInput` type, then format with the given format.
### Default Implementations
- [BinaryInteger Implementations](binaryinteger/binaryinteger-implementations.md)
- [Equatable Implementations](binaryinteger/equatable-implementations.md)

## Relationships

### Inherits From
- [AdditiveArithmetic](additivearithmetic.md)
- [Comparable](comparable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
- [Hashable](hashable.md)
- [Numeric](numeric.md)
- [Strideable](strideable.md)
### Inherited By
- [FixedWidthInteger](fixedwidthinteger.md)
- [SignedInteger](signedinteger.md)
- [UnsignedInteger](unsignedinteger.md)
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

- [protocol FixedWidthInteger](fixedwidthinteger.md)
  An integer type that uses a fixed size for every instance.
- [protocol SignedInteger](signedinteger.md)
  An integer type that can represent both positive and negative values.
- [protocol UnsignedInteger](unsignedinteger.md)
  An integer type that can represent only nonnegative values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryinteger)*