# pi

**Framework**: Swift  
**Kind**: property

The mathematical constant pi (π), approximately equal to 3.14159.

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
static var pi: Double { get }
```

#### Discussion

When measuring an angle in radians, π is equivalent to a half-turn.

This value is rounded toward zero to keep user computations with angles from inadvertently ending up in the wrong quadrant. A type that conforms to the `FloatingPoint` protocol provides the value for `pi` at its best possible precision.

```swift
print(Double.pi)
// Prints "3.14159265358979"
```

## See Also

- [static var infinity: Double](double/infinity.md)
  Positive infinity.
- [static var greatestFiniteMagnitude: Double](double/greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var nan: Double](double/nan.md)
  A quiet NaN (“not a number”).
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/pi)*