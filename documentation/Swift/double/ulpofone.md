# ulpOfOne

**Framework**: Swift  
**Kind**: property

The unit in the last place of 1.0.

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
static var ulpOfOne: Double { get }
```

#### Discussion

The positive difference between 1.0 and the next greater representable number. The `ulpOfOne` constant corresponds to the C macros `FLT_EPSILON`, `DBL_EPSILON`, and others with a similar purpose.

## See Also

- [static var pi: Double](double/pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var infinity: Double](double/infinity.md)
  Positive infinity.
- [static var greatestFiniteMagnitude: Double](double/greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var nan: Double](double/nan.md)
  A quiet NaN (“not a number”).
- [static var signalingNaN: Double](double/signalingnan.md)
  A signaling NaN (“not a number”).
- [static var leastNonzeroMagnitude: Double](double/leastnonzeromagnitude.md)
  The least positive number.
- [static var leastNormalMagnitude: Double](double/leastnormalmagnitude.md)
  The least positive normal number.
- [static var zero: Self](double/zero.md)
  The zero value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/ulpofone)*