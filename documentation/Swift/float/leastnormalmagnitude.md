# leastNormalMagnitude

**Framework**: Swift  
**Kind**: property

The least positive normal number.

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
static var leastNormalMagnitude: Float { get }
```

#### Discussion

This value compares less than or equal to all positive normal numbers. There may be smaller positive numbers, but they are , meaning that they are represented with less precision than normal numbers.

This value corresponds to type-specific C macros such as `FLT_MIN` and `DBL_MIN`. The naming of those macros is slightly misleading, because subnormals, zeros, and negative numbers are smaller than this value.

## See Also

- [static var pi: Float](float/pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var infinity: Float](float/infinity.md)
  Positive infinity.
- [static var greatestFiniteMagnitude: Float](float/greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var nan: Float](float/nan.md)
  A quiet NaN (“not a number”).
- [static var signalingNaN: Float](float/signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Float](float/ulpofone.md)
  The unit in the last place of 1.0.
- [static var leastNonzeroMagnitude: Float](float/leastnonzeromagnitude.md)
  The least positive number.
- [static var zero: Self](float/zero.md)
  The zero value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/leastnormalmagnitude)*