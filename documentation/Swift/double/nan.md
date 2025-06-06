# nan

**Framework**: Swift  
**Kind**: property

A quiet NaN (“not a number”).

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
static var nan: Double { get }
```

#### Discussion

A NaN compares not equal, not greater than, and not less than every value, including itself. Passing a NaN to an operation generally results in NaN.

```swift
let x = 1.21
// x > Double.nan == false
// x < Double.nan == false
// x == Double.nan == false
```

Because a NaN always compares not equal to itself, to test whether a floating-point value is NaN, use its `isNaN` property instead of the equal-to operator (`==`). In the following example, `y` is NaN.

```swift
let y = x + Double.nan
print(y == Double.nan)
// Prints "false"
print(y.isNaN)
// Prints "true"
```

## See Also

- [static var pi: Double](double/pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var infinity: Double](double/infinity.md)
  Positive infinity.
- [static var greatestFiniteMagnitude: Double](double/greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var signalingNaN: Double](double/signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Double](double/ulpofone.md)
  The unit in the last place of 1.0.
- [static var leastNonzeroMagnitude: Double](double/leastnonzeromagnitude.md)
  The least positive number.
- [static var leastNormalMagnitude: Double](double/leastnormalmagnitude.md)
  The least positive normal number.
- [static var zero: Self](double/zero.md)
  The zero value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/nan)*