# leastNormalMagnitude

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

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
static var leastNormalMagnitude: Double { get }
```

#### Discussion

This value compares less than or equal to all positive normal numbers. There may be smaller positive numbers, but they are *subnormal*, meaning that they are represented with less precision than normal numbers.

This value corresponds to type-specific C macros such as `FLT_MIN` and `DBL_MIN`. The naming of those macros is slightly misleading, because subnormals, zeros, and negative numbers are smaller than this value.

## See Also

### Accessing Numeric Constants
- [static var pi: Double](./pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var infinity: Double](./infinity.md)
  Positive infinity.
- [static var greatestFiniteMagnitude: Double](./greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var nan: Double](./nan.md)
  A quiet NaN (“not a number”).
- [static var signalingNaN: Double](./signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Double](./ulpofone.md)
  The unit in the last place of 1.0.
- [static var leastNonzeroMagnitude: Double](./leastnonzeromagnitude.md)
  The least positive number.
- [static var zero: Self](./zero.md)
  The zero value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/leastnormalmagnitude)*