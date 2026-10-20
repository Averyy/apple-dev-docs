# init(bytesNoCopy:length:encoding:freeWhenDone:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new string that contains the specified number of bytes from the given buffer, interpreted in the specified encoding, and optionally frees the buffer.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 8.0+ - Deprecated in 16.0
- macOS 10.10+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+
- watchOS 2.0+ - Deprecated in 9.0

> **Deprecated**: String does not support no-copy initialization

## Declaration

```swift
init?(bytesNoCopy bytes: UnsafeMutableRawPointer, length: Int, encoding: String.Encoding, freeWhenDone flag: Bool)
```

#### Discussion

> ⚠️ **Warning**: This initializer is not memory-safe!

## See Also

### Converting a C String
- [init?<S>(bytes: S, encoding: String.Encoding)](./init%28bytes,encoding%29.md)
  Creates a new string equivalent to the given bytes interpreted in the specified encoding. Note: This API does not interpret embedded nulls as termination of the string. Use `String?(validatingCString:)` instead for null-terminated C strings.
- [init?(validatingCString: UnsafePointer<CChar>)](./init%28validatingcstring%29-992vo.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init?(validatingCString: [CChar])](./init%28validatingcstring%29-98wra.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.
- [init(cString: UnsafePointer<CChar>)](./init%28cstring%29-2p84k.md)
  Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString: UnsafePointer<UInt8>)](./init%28cstring%29-6kr8s.md)
  Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init?(cString: [CChar], encoding: String.Encoding)](./init%28cstring,encoding%29-3h7bc.md)
  Produces a string by copying the null-terminated bytes in a given array, interpreted according to a given encoding.
- [init?(cString: UnsafePointer<CChar>, encoding: String.Encoding)](./init%28cstring,encoding%29-3qgzd.md)
  Produces a string by copying the null-terminated bytes in a given C array, interpreted according to a given encoding.
- [init<Encoding>(decodingCString: [Encoding.CodeUnit], as: Encoding.Type)](./init%28decodingcstring,as%29-8way7.md)
  Creates a new string by copying the null-terminated sequence of code units referenced by the given array.
- [static func decodeCString<Encoding>(UnsafePointer<Encoding.CodeUnit>?, as: Encoding.Type, repairingInvalidCodeUnits: Bool) -> (result: String, repairsMade: Bool)?](./decodecstring%28_,as,repairinginvalidcodeunits%29-46n2p.md)
  Creates a new string by copying the null-terminated data referenced by the given pointer using the specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(bytesnocopy:length:encoding:freewhendone:))*