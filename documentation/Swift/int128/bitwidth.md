# bitWidth

**Framework**: Swift  
**Kind**: property

The number of bits used for the underlying binary representation of values of this type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static var bitWidth: Int { get }
```

#### Discussion

An unsigned, fixed-width integer type can represent values from 0 through `(2 ** bitWidth) - 1`, where `**` is exponentiation. A signed, fixed-width integer type can represent values from `-(2 ** (bitWidth - 1))` through `(2 ** (bitWidth - 1)) - 1`. For example, the `Int8` type has a `bitWidth` value of 8 and can store any integer in the range `-128...127`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/bitwidth)*