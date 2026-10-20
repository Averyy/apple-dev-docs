# init(truncatingIfNeeded:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.

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
init<T>(truncatingIfNeeded source: T) where T : BinaryInteger
```

#### Discussion

When the bit width of `T` (the type of `source`) is equal to or greater than this type’s bit width, the result is the truncated least-significant bits of `source`. For example, when converting a 16-bit value to an 8-bit type, only the lower 8 bits of `source` are used.

```swift
let p: Int16 = -500
// 'p' has a binary representation of 11111110_00001100
let q = Int8(truncatingIfNeeded: p)
// q == 12
// 'q' has a binary representation of 00001100
```

When the bit width of `T` is less than this type’s bit width, the result is *sign-extended* to fill the remaining bits. That is, if `source` is negative, the result is padded with ones; otherwise, the result is padded with zeros.

```swift
let u: Int8 = 21
// 'u' has a binary representation of 00010101
let v = Int16(truncatingIfNeeded: u)
// v == 21
// 'v' has a binary representation of 00000000_00010101

let w: Int8 = -21
// 'w' has a binary representation of 11101011
let x = Int16(truncatingIfNeeded: w)
// x == -21
// 'x' has a binary representation of 11111111_11101011
let y = UInt16(truncatingIfNeeded: w)
// y == 65515
// 'y' has a binary representation of 11111111_11101011
```

## Parameters

- `source`: An integer to convert to this type.

## See Also

### Converting Integers
- [init<T>(T)](./init%28_%29-4ekvl.md)
  Creates a new instance from the given integer.
- [init?<T>(exactly: T)](./init%28exactly%29-b1dy.md)
- [init<Other>(clamping: Other)](./init%28clamping%29.md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init(bitPattern: UInt)](./init%28bitpattern%29-72037.md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: NSNumber)](./init%28exactly%29-177ax.md)
- [init(truncating: NSNumber)](./init%28truncating%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/init(truncatingifneeded:))*