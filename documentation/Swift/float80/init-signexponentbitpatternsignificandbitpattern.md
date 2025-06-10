# init(sign:exponentBitPattern:significandBitPattern:)

**Framework**: Swift  
**Kind**: init

Creates a new instance from the specified sign and bit patterns.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt64)
```

#### Discussion

The values passed as `exponentBitPattern` and `significandBitPattern` are interpreted in the binary interchange format defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `sign`: The sign of the new value.
- `exponentBitPattern`: The bit pattern to use for the exponent field of   the new value.
- `significandBitPattern`: The bit pattern to use for the significand   field of the new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/init(sign:exponentbitpattern:significandbitpattern:))*