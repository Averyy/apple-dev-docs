# init(sign:exponentBitPattern:significandBitPattern:)

**Framework**: Swift  
**Kind**: init

Creates a new instance from the specified sign and bit patterns.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt16)
```

#### Discussion

The values passed as `exponentBitPattern` and `significandBitPattern` are interpreted in the binary interchange format defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `sign`: The sign of the new value.
- `exponentBitPattern`: The bit pattern to use for the exponent field of   the new value.
- `significandBitPattern`: The bit pattern to use for the significand   field of the new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/init(sign:exponentbitpattern:significandbitpattern:))*