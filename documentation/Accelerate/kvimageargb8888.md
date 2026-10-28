# kvImageARGB8888

**Framework**: Accelerate  
**Kind**: var  
**Role**: Global Variable

Any 16-bit signed fixed-point, four-channel interleaved buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var kvImageARGB8888: vImageARGBType { get }
```

```c
kvImageARGB8888
```

## Discussion

This type doesn’t specify channel order.

## See Also

### Constants
- [init(UInt32)](./vimageargbtype/init%28_%29.md)
  Creates a new ARGB type.
- [init(rawValue: UInt32)](./vimageargbtype/init%28rawvalue%29.md)
  Creates a new ARGB type with an unsigned integer value.
- [var rawValue: UInt32](./vimageargbtype/rawvalue.md)
  The unsigned integer raw value.
- [var kvImageARGB16Q12: vImageARGBType](./kvimageargb16q12.md)
  Any 8-bit four-channel interleaved buffer.
- [var kvImageARGB16U: vImageARGBType](./kvimageargb16u.md)
  Any 16-bit unsigned, four-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/kvimageargb8888)*