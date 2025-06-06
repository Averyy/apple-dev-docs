# FloatingPoint

**Framework**: Swift  
**Kind**: protocol

A floating-point numeric type.

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
protocol FloatingPoint : Hashable, SignedNumeric, Strideable where Self == Self.Magnitude
```

#### Overview

Floating-point types are used to represent fractional numbers, like 5.5, 100.0, or 3.14159274. Each floating-point type has its own possible range and precision. The floating-point types in the standard library are `Float`, `Double`, and `Float80` where available.

Create new instances of floating-point types using integer or floating-point literals. For example:

```swift
let temperature = 33.2
let recordHigh = 37.5
```

The `FloatingPoint` protocol declares common arithmetic operations, so you can write functions and algorithms that work on any floating-point type. The following example declares a function that calculates the length of the hypotenuse of a right triangle given its two perpendicular sides. Because the `hypotenuse(_:_:)` function uses a generic parameter constrained to the `FloatingPoint` protocol, you can call it using any floating-point type.

```swift
func hypotenuse<T: FloatingPoint>(_ a: T, _ b: T) -> T {
    return (a * a + b * b).squareRoot()
}

let (dx, dy) = (3.0, 4.0)
let distance = hypotenuse(dx, dy)
// distance == 5.0
```

Floating-point values are represented as a  and a , where the magnitude is calculated using the type’s  and the instance’s  and . This magnitude calculation takes the following form for a floating-point value `x` of type `F`, where `**` is exponentiation:

```swift
x.significand * (F.radix ** x.exponent)
```

Here’s an example of the number -8.5 represented as an instance of the `Double` type, which defines a radix of 2.

```swift
let y = -8.5
// y.sign == .minus
// y.significand == 1.0625
// y.exponent == 3

let magnitude = 1.0625 * Double(2 ** 3)
// magnitude == 8.5
```

Types that conform to the `FloatingPoint` protocol provide most basic (clause 5) operations of the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933). The base, precision, and exponent range are not fixed in any way by this protocol, but it enforces the basic requirements of any IEEE 754 floating-point type.

### Additional Considerations

In addition to representing specific numbers, floating-point types also have special values for working with overflow and nonnumeric results of calculation.

#### Infinity

Any value whose magnitude is so great that it would round to a value outside the range of representable numbers is rounded to . For a type `F`, positive and negative infinity are represented as `F.infinity` and `-F.infinity`, respectively. Positive infinity compares greater than every finite value and negative infinity, while negative infinity compares less than every finite value and positive infinity. Infinite values with the same sign are equal to each other.

```swift
let values: [Double] = [10.0, 25.0, -10.0, .infinity, -.infinity]
print(values.sorted())
// Prints "[-inf, -10.0, 10.0, 25.0, inf]"
```

Operations with infinite values follow real arithmetic as much as possible: Adding or subtracting a finite value, or multiplying or dividing infinity by a nonzero finite value, results in infinity.

#### Nan Not a Number

Floating-point types represent values that are neither finite numbers nor infinity as NaN, an abbreviation for “not a number.” Comparing a NaN with any value, including another NaN, results in `false`.

```swift
let myNaN = Double.nan
print(myNaN > 0)
// Prints "false"
print(myNaN < 0)
// Prints "false"
print(myNaN == .nan)
// Prints "false"
```

Because testing whether one NaN is equal to another NaN results in `false`, use the `isNaN` property to test whether a value is NaN.

```swift
print(myNaN.isNaN)
// Prints "true"
```

NaN propagates through many arithmetic operations. When you are operating on many values, this behavior is valuable because operations on NaN simply forward the value and don’t cause runtime errors. The following example shows how NaN values operate in different contexts.

Imagine you have a set of temperature data for which you need to report some general statistics: the total number of observations, the number of valid observations, and the average temperature. First, a set of observations in Celsius is parsed from strings to `Double` values:

```swift
let temperatureData = ["21.5", "19.25", "27", "no data", "28.25", "no data", "23"]
let tempsCelsius = temperatureData.map { Double($0) ?? .nan }
print(tempsCelsius)
// Prints "[21.5, 19.25, 27, nan, 28.25, nan, 23.0]"
```

Note that some elements in the `temperatureData ` array are not valid numbers. When these invalid strings are parsed by the `Double` failable initializer, the example uses the nil-coalescing operator (`??`) to provide NaN as a fallback value.

Next, the observations in Celsius are converted to Fahrenheit:

```swift
let tempsFahrenheit = tempsCelsius.map { $0 * 1.8 + 32 }
print(tempsFahrenheit)
// Prints "[70.7, 66.65, 80.6, nan, 82.85, nan, 73.4]"
```

The NaN values in the `tempsCelsius` array are propagated through the conversion and remain NaN in `tempsFahrenheit`.

Because calculating the average of the observations involves combining every value of the `tempsFahrenheit` array, any NaN values cause the result to also be NaN, as seen in this example:

```swift
let badAverage = tempsFahrenheit.reduce(0.0, +) / Double(tempsFahrenheit.count)
// badAverage.isNaN == true
```

Instead, when you need an operation to have a specific numeric result, filter out any NaN values using the `isNaN` property.

```swift
let validTemps = tempsFahrenheit.filter { !$0.isNaN }
let average = validTemps.reduce(0.0, +) / Double(validTemps.count)
```

Finally, report the average temperature and observation counts:

```swift
print("Average: \(average)°F in \(validTemps.count) " +
      "out of \(tempsFahrenheit.count) observations.")
// Prints "Average: 74.84°F in 5 out of 7 observations."
```

## Topics

### Operators
- [static func * (Self, Self) -> Self](floatingpoint/*(_:_:).md)
  Multiplies two values and produces their product, rounding to a representable value.
- [static func *= (inout Self, Self)](floatingpoint/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [static func + (Self, Self) -> Self](floatingpoint/+(_:_:).md)
  Adds two values and produces their sum, rounded to a representable value.
- [static func += (inout Self, Self)](floatingpoint/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [static func - (Self) -> Self](floatingpoint/-(_:).md)
  Calculates the additive inverse of a value.
- [static func - (Self, Self) -> Self](floatingpoint/-(_:_:).md)
  Subtracts one value from another and produces their difference, rounded to a representable value.
- [static func -= (inout Self, Self)](floatingpoint/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [static func / (Self, Self) -> Self](floatingpoint/_(_:_:).md)
  Returns the quotient of dividing the first value by the second, rounded to a representable value.
- [static func /= (inout Self, Self)](floatingpoint/_=(_:_:).md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
### Associated Types
- [associatedtype Exponent : SignedInteger](floatingpoint/exponent-swift.associatedtype.md)
  A type that can represent any written exponent.
### Initializers
- [init<Source>(Source)](floatingpoint/init(_:)-2f8bx.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Int)](floatingpoint/init(_:)-2xwlo.md)
  Creates a new value, rounded to the closest possible representation.
- [init?<Source>(exactly: Source)](floatingpoint/init(exactly:).md)
  Creates a new value, if the given integer can be represented exactly.
- [init(sign: FloatingPointSign, exponent: Self.Exponent, significand: Self)](floatingpoint/init(sign:exponent:significand:).md)
  Creates a new value from the given sign, exponent, and significand.
- [init(signOf: Self, magnitudeOf: Self)](floatingpoint/init(signof:magnitudeof:).md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
### Instance Properties
- [var exponent: Self.Exponent](floatingpoint/exponent-swift.property.md)
  The exponent of the floating-point value.
- [var floatingPointClass: FloatingPointClassification](floatingpoint/floatingpointclass.md)
  The classification of this value.
- [var isCanonical: Bool](floatingpoint/iscanonical.md)
  A Boolean value indicating whether the instance’s representation is in its canonical form.
- [var isFinite: Bool](floatingpoint/isfinite.md)
  A Boolean value indicating whether this instance is finite.
- [var isInfinite: Bool](floatingpoint/isinfinite.md)
  A Boolean value indicating whether the instance is infinite.
- [var isNaN: Bool](floatingpoint/isnan.md)
  A Boolean value indicating whether the instance is NaN (“not a number”).
- [var isNormal: Bool](floatingpoint/isnormal.md)
  A Boolean value indicating whether this instance is normal.
- [var isSignalingNaN: Bool](floatingpoint/issignalingnan.md)
  A Boolean value indicating whether the instance is a signaling NaN.
- [var isSubnormal: Bool](floatingpoint/issubnormal.md)
  A Boolean value indicating whether the instance is subnormal.
- [var isZero: Bool](floatingpoint/iszero.md)
  A Boolean value indicating whether the instance is equal to zero.
- [var nextDown: Self](floatingpoint/nextdown.md)
  The greatest representable value that compares less than this value.
- [var nextUp: Self](floatingpoint/nextup.md)
  The least representable value that compares greater than this value.
- [var sign: FloatingPointSign](floatingpoint/sign.md)
  The sign of the floating-point value.
- [var significand: Self](floatingpoint/significand.md)
  The significand of the floating-point value.
- [var ulp: Self](floatingpoint/ulp.md)
  The unit in the last place of this value.
### Instance Methods
- [func addProduct(Self, Self)](floatingpoint/addproduct(_:_:).md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func addingProduct(Self, Self) -> Self](floatingpoint/addingproduct(_:_:).md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func formRemainder(dividingBy: Self)](floatingpoint/formremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value.
- [func formSquareRoot()](floatingpoint/formsquareroot.md)
  Replaces this value with its square root, rounded to a representable value.
- [func formTruncatingRemainder(dividingBy: Self)](floatingpoint/formtruncatingremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.
- [func isEqual(to: Self) -> Bool](floatingpoint/isequal(to:).md)
  Returns a Boolean value indicating whether this instance is equal to the given value.
- [func isLess(than: Self) -> Bool](floatingpoint/isless(than:).md)
  Returns a Boolean value indicating whether this instance is less than the given value.
- [func isLessThanOrEqualTo(Self) -> Bool](floatingpoint/islessthanorequalto(_:).md)
  Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [func isTotallyOrdered(belowOrEqualTo: Self) -> Bool](floatingpoint/istotallyordered(beloworequalto:).md)
  Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [func negate()](floatingpoint/negate.md)
  Replaces this value with its additive inverse.
- [func remainder(dividingBy: Self) -> Self](floatingpoint/remainder(dividingby:).md)
  Returns the remainder of this value divided by the given value.
- [func round()](floatingpoint/round.md)
- [func round(FloatingPointRoundingRule)](floatingpoint/round(_:).md)
  Rounds the value to an integral value using the specified rounding rule.
- [func rounded() -> Self](floatingpoint/rounded.md)
- [func rounded(FloatingPointRoundingRule) -> Self](floatingpoint/rounded(_:).md)
  Returns this value rounded to an integral value using the specified rounding rule.
- [func squareRoot() -> Self](floatingpoint/squareroot.md)
  Returns the square root of the value, rounded to a representable value.
- [func truncatingRemainder(dividingBy: Self) -> Self](floatingpoint/truncatingremainder(dividingby:).md)
  Returns the remainder of this value divided by the given value using truncating division.
### Type Properties
- [static var greatestFiniteMagnitude: Self](floatingpoint/greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var infinity: Self](floatingpoint/infinity.md)
  Positive infinity.
- [static var leastNonzeroMagnitude: Self](floatingpoint/leastnonzeromagnitude.md)
  The least positive number.
- [static var leastNormalMagnitude: Self](floatingpoint/leastnormalmagnitude.md)
  The least positive normal number.
- [static var nan: Self](floatingpoint/nan.md)
  A quiet NaN (“not a number”).
- [static var pi: Self](floatingpoint/pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var radix: Int](floatingpoint/radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [static var signalingNaN: Self](floatingpoint/signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Self](floatingpoint/ulpofone.md)
  The unit in the last place of 1.0.
### Type Methods
- [static func maximum(Self, Self) -> Self](floatingpoint/maximum(_:_:).md)
  Returns the greater of the two given values.
- [static func maximumMagnitude(Self, Self) -> Self](floatingpoint/maximummagnitude(_:_:).md)
  Returns the value with greater magnitude.
- [static func minimum(Self, Self) -> Self](floatingpoint/minimum(_:_:).md)
  Returns the lesser of the two given values.
- [static func minimumMagnitude(Self, Self) -> Self](floatingpoint/minimummagnitude(_:_:).md)
  Returns the value with lesser magnitude.

## Relationships

### Inherits From
- [AdditiveArithmetic](additivearithmetic.md)
- [Comparable](comparable.md)
- [Equatable](equatable.md)
- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
- [Hashable](hashable.md)
- [Numeric](numeric.md)
- [SignedNumeric](signednumeric.md)
- [Strideable](strideable.md)
### Inherited By
- [BinaryFloatingPoint](binaryfloatingpoint.md)
### Conforming Types
- [Double](double.md)
- [Float](float.md)
- [Float16](float16.md)
- [Float80](float80.md)

## See Also

- [protocol BinaryFloatingPoint](binaryfloatingpoint.md)
  A radix-2 (binary) floating-point type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpoint)*