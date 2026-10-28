# zero

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

The zero value.

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
static var zero: Self { get }
```

Available when `Self` conforms to `ExpressibleByIntegerLiteral`.

## Discussion

Zero is the identity element for addition. For any value, `x + .zero == x` and `.zero + x == x`.

## See Also

### Accessing Numeric Constants
- [static var pi: Float](./pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var infinity: Float](./infinity.md)
  Positive infinity.
- [static var greatestFiniteMagnitude: Float](./greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var nan: Float](./nan.md)
  A quiet NaN (“not a number”).
- [static var signalingNaN: Float](./signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Float](./ulpofone.md)
  The unit in the last place of 1.0.
- [static var leastNormalMagnitude: Float](./leastnormalmagnitude.md)
  The least positive normal number.
- [static var leastNonzeroMagnitude: Float](./leastnonzeromagnitude.md)
  The least positive number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/zero)*