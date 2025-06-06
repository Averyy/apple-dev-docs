# bitWidth

**Framework**: Swift  
**Kind**: property

Returns the minimal number of bits in this value’s binary representation, including the sign bit, and excluding the sign extension.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
var bitWidth: Int { get }
```

#### Discussion

The following examples show the least significant byte of each value’s binary representation, separated (by an underscore) into excluded and included bits. Negative values are in two’s complement.

- `-4` (`0b11111_100`) is 3 bits.
- `-3` (`0b11111_101`) is 3 bits.
- `-2` (`0b111111_10`) is 2 bits.
- `-1` (`0b1111111_1`) is 1 bit.
- `+0` (`0b0000000_0`) is 1 bit.
- `+1` (`0b000000_01`) is 2 bits.
- `+2` (`0b00000_010`) is 3 bits.
- `+3` (`0b00000_011`) is 3 bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/staticbigint/bitwidth)*