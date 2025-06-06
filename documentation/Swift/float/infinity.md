# infinity

**Framework**: Swift  
**Kind**: property

Positive infinity.

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
static var infinity: Float { get }
```

#### Discussion

Infinity compares greater than all finite numbers and equal to other infinite values.

```swift
let x = Double.greatestFiniteMagnitude
let y = x * 2
// y == Double.infinity
// y > x
```

## See Also

- [static var pi: Float](float/pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var greatestFiniteMagnitude: Float](float/greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var nan: Float](float/nan.md)
  A quiet NaN (“not a number”).
- [static var signalingNaN: Float](float/signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Float](float/ulpofone.md)
  The unit in the last place of 1.0.
- [static var leastNormalMagnitude: Float](float/leastnormalmagnitude.md)
  The least positive normal number.
- [static var leastNonzeroMagnitude: Float](float/leastnonzeromagnitude.md)
  The least positive number.
- [static var zero: Self](float/zero.md)
  The zero value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/infinity)*