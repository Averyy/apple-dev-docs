# abs(_:)

**Framework**: Swift  
**Kind**: func

Returns the absolute value of the given number.

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
func abs<T>(_ x: T) -> T where T : Comparable, T : SignedNumeric
```

#### Return Value

The absolute value of `x`.

#### Discussion

The absolute value of `x` must be representable in the same type. In particular, the absolute value of a signed, fixed-width integer type’s minimum cannot be represented.

```swift
let x = Int8.min
// x == -128
let y = abs(x)
// Overflow error
```

## Parameters

- `x`: A signed number.

## See Also

- [var magnitude: UInt](int/magnitude-swift.property.md)
  The magnitude of this value.
- [typealias Magnitude](int/magnitude-swift.typealias.md)
  A type that can represent the absolute value of any possible value of this type.
- [func signum() -> Int](int/signum.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/abs(_:))*