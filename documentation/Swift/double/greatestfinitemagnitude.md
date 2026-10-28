# greatestFiniteMagnitude

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

The greatest finite number representable by this type.

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
static var greatestFiniteMagnitude: Double { get }
```

## Discussion

This value compares greater than or equal to all finite numbers, but less than `infinity`.

This value corresponds to type-specific C macros such as `FLT_MAX` and `DBL_MAX`. The naming of those macros is slightly misleading, because `infinity` is greater than this value.

## See Also

### Accessing Numeric Constants
- [static var pi: Double](./pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var infinity: Double](./infinity.md)
  Positive infinity.
- [static var nan: Double](./nan.md)
  A quiet NaN (“not a number”).
- [static var signalingNaN: Double](./signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Double](./ulpofone.md)
  The unit in the last place of 1.0.
- [static var leastNonzeroMagnitude: Double](./leastnonzeromagnitude.md)
  The least positive number.
- [static var leastNormalMagnitude: Double](./leastnormalmagnitude.md)
  The least positive normal number.
- [static var zero: Self](./zero.md)
  The zero value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/greatestfinitemagnitude)*