# init(clamping:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new instance with the representable value that’s closest to the given integer.

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
init<Other>(clamping source: Other) where Other : BinaryInteger
```

## Discussion

If the value passed as `source` is greater than the maximum representable value in this type, the result is the type’s `max` value. If `source` is less than the smallest representable value in this type, the result is the type’s `min` value.

In this example, `x` is initialized as an `Int8` instance by clamping `500` to the range `-128...127`, and `y` is initialized as a `UInt` instance by clamping `-500` to the range `0...UInt.max`.

```swift
let x = Int8(clamping: 500)
// x == 127
// x == Int8.max

let y = UInt(clamping: -500)
// y == 0
```

## Parameters

- `source`: An integer to convert to this type.

## See Also

### Converting Integers
- [init<T>(T)](./init%28_%29-4ekvl.md)
  Creates a new instance from the given integer.
- [init?<T>(exactly: T)](./init%28exactly%29-b1dy.md)
- [init<T>(truncatingIfNeeded: T)](./init%28truncatingifneeded%29.md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init(bitPattern: UInt)](./init%28bitpattern%29-72037.md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: NSNumber)](./init%28exactly%29-177ax.md)
- [init(truncating: NSNumber)](./init%28truncating%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/init(clamping:))*