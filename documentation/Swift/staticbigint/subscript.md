# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Returns a 32-bit or 64-bit word of this value’s binary representation.

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
subscript(wordIndex: Int) -> UInt { get }
```

#### Overview

The words are ordered from least significant to most significant, with an infinite sign extension. Negative values are in two’s complement.

```swift
let negative: StaticBigInt = -0x0011223344556677_8899AABBCCDDEEFF
negative.signum()  //-> -1
negative.bitWidth  //-> 118
negative[0]        //-> 0x7766554433221101
negative[1]        //-> 0xFFEEDDCCBBAA9988
negative[2]        //-> 0xFFFFFFFFFFFFFFFF

let positive: StaticBigInt =  0x0011223344556677_8899AABBCCDDEEFF
positive.signum()  //-> +1
positive.bitWidth  //-> 118
positive[0]        //-> 0x8899AABBCCDDEEFF
positive[1]        //-> 0x0011223344556677
positive[2]        //-> 0x0000000000000000
```

## Parameters

- `wordIndex`: A nonnegative zero-based offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/staticbigint/subscript(_:))*