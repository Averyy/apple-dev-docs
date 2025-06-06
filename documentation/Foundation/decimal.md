# Decimal

**Framework**: Foundation  
**Kind**: struct

A structure representing a base-10 number.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Decimal
```

## Topics

### Creating an empty decimal
- [init()](decimal/init.md)
  Creates a decimal initialized to `0`.
### Creating a decimal from components
- [init(sign: FloatingPointSign, exponent: Int, significand: Decimal)](decimal/init(sign:exponent:significand:).md)
  Creates a decimal initialized with the given sign, exponent, and significand.
### Creating a decimal from a floating point number
- [init(Double)](decimal/init(_:)-6wgru.md)
  Creates and initializes a decimal with the provided floating point value.
### Creating a decimal from an integer
- [init(Int)](decimal/init(_:)-2tcho.md)
  Creates and initializes a decimal with the provided integer value.
- [init(Int8)](decimal/init(_:)-4gk29.md)
  Creates and initializes a decimal with the provided integer value.
- [init(Int16)](decimal/init(_:)-5aznh.md)
  Creates and initializes a decimal with the provided integer value.
- [init(Int32)](decimal/init(_:)-7dmlc.md)
  Creates and initializes a decimal with the provided integer value.
- [init(Int64)](decimal/init(_:)-7a033.md)
  Creates and initializes a decimal with the provided integer value.
### Creating a decimal from an unsigned integer
- [init(UInt)](decimal/init(_:)-2lxxy.md)
  Creates and initializes a decimal with the provided unsigned integer value.
- [init(UInt8)](decimal/init(_:)-4gbgq.md)
  Creates and initializes a decimal with the provided unsigned integer value.
- [init(UInt16)](decimal/init(_:)-9lio1.md)
  Creates and initializes a decimal with the provided unsigned integer value.
- [init(UInt32)](decimal/init(_:)-9okou.md)
  Creates and initializes a decimal with the provided unsigned integer value.
- [init(UInt64)](decimal/init(_:)-43cx6.md)
  Creates and initializes a decimal with the provided unsigned integer value.
### Creating a decimal from another decimal
- [init(signOf: Decimal, magnitudeOf: Decimal)](decimal/init(signof:magnitudeof:).md)
  Creates and initializes a decimal with the sign and magnitude of the given decimals.
- [func NSDecimalCopy(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>)](nsdecimalcopy(_:_:).md)
  Copies the value of a decimal number.
### Creating a decimal by parsing a string
- [init(String, format: Decimal.FormatStyle, lenient: Bool) throws](decimal/init(_:format:lenient:)-6fk71.md)
  Creates and initializes a decimal by parsing a string according to the provided format style.
- [init(String, format: Decimal.FormatStyle.Currency, lenient: Bool) throws](decimal/init(_:format:lenient:)-8t5o2.md)
  Creates and initializes a decimal by parsing a string according to the provided currency format style.
- [init(String, format: Decimal.FormatStyle.Percent, lenient: Bool) throws](decimal/init(_:format:lenient:)-3u6o6.md)
  Creates and initializes a percentage decimal by parsing a string according to the provided format style.
- [init?(string: String, locale: Locale?)](decimal/init(string:locale:).md)
  Creates and initializes a decimal by parsing a string according to the provided locale’s conventions.
- [init<S>(S.ParseInput, strategy: S) throws](decimal/init(_:strategy:).md)
  Creates and initializes a decimal by parsing an arbitrary type according to the provided parse strategy.
- [Decimal.ParseStrategy](decimal/parsestrategy.md)
  A parse strategy for creating decimal values from formatted strings.
### Performing arithmetic
- [func pow(Decimal, Int) -> Decimal](pow(_:_:).md)
  Returns a decimal number raised to a given power.
### Performing arithmetic using references
- [func NSDecimalCompact(UnsafeMutablePointer<Decimal>)](nsdecimalcompact(_:).md)
  Compacts the decimal structure for efficiency.
- [func NSDecimalAdd(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimaladd(_:_:_:_:).md)
  Adds two decimal values.
- [func NSDecimalSubtract(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimalsubtract(_:_:_:_:).md)
  Subtracts one decimal value from another.
- [func NSDecimalDivide(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimaldivide(_:_:_:_:).md)
  Divides one decimal value by another.
- [func NSDecimalMultiply(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, UnsafePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimalmultiply(_:_:_:_:).md)
  Multiplies two decimal numbers together.
- [func NSDecimalMultiplyByPowerOf10(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int16, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimalmultiplybypowerof10(_:_:_:_:).md)
  Multiplies a decimal by the specified power of 10.
- [func NSDecimalRound(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int, NSDecimalNumber.RoundingMode)](nsdecimalround(_:_:_:_:).md)
  Rounds off the decimal value.
- [func NSDecimalPower(UnsafeMutablePointer<Decimal>, UnsafePointer<Decimal>, Int, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimalpower(_:_:_:_:).md)
  Raises the decimal value to the specified power.
- [func NSDecimalNormalize(UnsafeMutablePointer<Decimal>, UnsafeMutablePointer<Decimal>, NSDecimalNumber.RoundingMode) -> NSDecimalNumber.CalculationError](nsdecimalnormalize(_:_:_:).md)
  Normalizes the internal format of two decimal numbers to simplify later operations.
- [typealias RoundingMode](decimal/roundingmode.md)
  An alias for an enumeration that specifies possible rounding modes.
- [NSDecimalNumber.RoundingMode](nsdecimalnumber/roundingmode.md)
  These constants specify rounding behaviors.
- [typealias CalculationError](decimal/calculationerror.md)
  An alias for a type that specifies possible calculation errors.
- [NSDecimalNumber.CalculationError](nsdecimalnumber/calculationerror.md)
  Calculation error constants used to describe an error in [`exceptionDuringOperation(_:error:leftOperand:rightOperand:)`](nsdecimalnumberbehaviors/exceptionduringoperation(_:error:leftoperand:rightoperand:).md).
### Getting a decimal’s characteristics
- [var sign: FloatingPointSign](decimal/sign.md)
  The sign of the decimal.
- [var exponent: Int](decimal/exponent.md)
  The exponent of the decimal.
- [var significand: Decimal](decimal/significand.md)
  The significand of the decimal.
- [var floatingPointClass: FloatingPointClassification](decimal/floatingpointclass.md)
  The IEEE 754 class of this type.
- [var isCanonical: Bool](decimal/iscanonical.md)
  A Boolean value indicating whether the representation of this decimal is canonical.
- [var isFinite: Bool](decimal/isfinite.md)
  A Boolean value indicating whether this decimal is zero, subnormal, or normal (not infinity or NaN).
- [var isInfinite: Bool](decimal/isinfinite.md)
  A Boolean value indicating whether this decimal is infinity.
- [var isNaN: Bool](decimal/isnan.md)
  A Boolean value indicating whether this decimal is NaN.
- [var isNormal: Bool](decimal/isnormal.md)
  A Boolean value indicating whether this decimal is normal (not zero, subnormal, infinity, or NaN).
- [var isSignMinus: Bool](decimal/issignminus.md)
  A Boolean value indicating whether this decimal has a negative sign.
- [var isSignaling: Bool](decimal/issignaling.md)
  A Boolean value indicating whether this decimal is a signaling NaN.``
- [var isSignalingNaN: Bool](decimal/issignalingnan.md)
  A Boolean value indicating whether this decimal is a signaling NaN.
- [var isSubnormal: Bool](decimal/issubnormal.md)
  A Boolean value indicating whether this decimal is subnormal.
- [var isZero: Bool](decimal/iszero.md)
  A Boolean value indicating whether this value is zero.
- [var nextDown: Decimal](decimal/nextdown.md)
  The greatest representable value that is less than this decimal.
- [var nextUp: Decimal](decimal/nextup.md)
  The least representable value that is greater than this decimal.
- [var ulp: Decimal](decimal/ulp.md)
  The unit in the last place of the decimal.
### Getting particular decimals
- [static let greatestFiniteMagnitude: Decimal](decimal/greatestfinitemagnitude.md)
  The decimal that contains the largest possible non-infinite magnitude for the underlying representation.
- [static let leastFiniteMagnitude: Decimal](decimal/leastfinitemagnitude.md)
  The decimal that contains the smallest possible non-infinite magnitude for the underlying representation.
- [static let leastNonzeroMagnitude: Decimal](decimal/leastnonzeromagnitude.md)
  The decimal value that represents the smallest possible non-zero value for the underlying representation.
- [static let leastNormalMagnitude: Decimal](decimal/leastnormalmagnitude.md)
  The decimal value that represents the smallest possible normal magnitude for the underlying representation.
- [static let pi: Decimal](decimal/pi.md)
  The mathematical constant pi.
- [static var nan: Decimal](decimal/nan.md)
  The value that represents “not a number.”
- [static var quietNaN: Decimal](decimal/quietnan.md)
  A quiet representation of not-a-number.
- [static var radix: Int](decimal/radix.md)
  The radix used by decimal numbers.
- [var NSDecimalMaxSize: Int32](nsdecimalmaxsize.md)
  The maximum size of [`Decimal`](decimal.md).
- [var NSDecimalNoScale: Int32](nsdecimalnoscale.md)
  Specifies that the number of digits allowed after the decimal separator in a decimal number should not be limited.
### Formatting decimals
- [func formatted() -> String](decimal/formatted.md)
  Formats the decimal using a default localized format style.
- [func formatted<S>(S) -> S.FormatOutput](decimal/formatted(_:).md)
  Formats the decimal using the provided format style.
- [Decimal.FormatStyle](decimal/formatstyle.md)
  A structure that converts between decimal values and their textual representations.
### Converting between decimals and strings
- [func NSDecimalString(UnsafePointer<Decimal>, Any?) -> String](nsdecimalstring(_:_:).md)
  Returns a string representation of the decimal value appropriate for the specified locale.
### Comparing decimals
- [func isEqual(to: Decimal) -> Bool](decimal/isequal(to:).md)
  Indicates whether this decimal is equal to the specified one.
- [func isLess(than: Decimal) -> Bool](decimal/isless(than:).md)
  Indicates whether this decimal is less than the specified one.
- [func isLessThanOrEqualTo(Decimal) -> Bool](decimal/islessthanorequalto(_:).md)
  Indicates whether this decimal is less than or equal to the specified one.
- [func isTotallyOrdered(belowOrEqualTo: Decimal) -> Bool](decimal/istotallyordered(beloworequalto:).md)
  Returns a Boolean value indicating whether this instance should precede the given value in an ascending sort.
- [func NSDecimalCompare(UnsafePointer<Decimal>, UnsafePointer<Decimal>) -> ComparisonResult](nsdecimalcompare(_:_:).md)
  Compares two decimal values.
### Using reference types
- [class NSDecimalNumber](nsdecimalnumber.md)
  An object for representing and performing arithmetic on base-10 numbers.
### Supporting Types
- [Decimal.FormatStyle](decimal/formatstyle.md)
  A structure that converts between decimal values and their textual representations.
### Operators
- [static func / (Decimal, Decimal) -> Decimal](decimal/_(_:_:).md)
- [static func /= (inout Decimal, Decimal)](decimal/_=(_:_:).md)
### Instance Methods
- [func add(Decimal)](decimal/add(_:).md)
- [func divide(by: Decimal)](decimal/divide(by:).md)
- [func multiply(by: Decimal)](decimal/multiply(by:).md)
- [func subtract(Decimal)](decimal/subtract(_:).md)

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Numeric](../Swift/Numeric.md)
- [Plottable](../Charts/Plottable.md)
- [Sendable](../Swift/Sendable.md)
- [SignedNumeric](../Swift/SignedNumeric.md)
- [Strideable](../Swift/Strideable.md)

## See Also

- [@frozen struct Int](../Swift/Int.md)
  A signed integer value type.
- [@frozen struct Double](../Swift/Double.md)
  A double-precision, floating-point value type.
- [class NumberFormatter](numberformatter.md)
  A formatter that converts between numeric values and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal)*