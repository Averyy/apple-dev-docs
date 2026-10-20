# init(validatingCString:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift - Deprecated in 6.0

> **Deprecated**: Use String(validating: array, as: UTF8.self) instead, after truncating the null termination.

## Declaration

```swift
init?(validatingCString nullTerminatedUTF8: [CChar])
```

#### Discussion

This initializer does not try to repair ill-formed UTF-8 code unit sequences. If any are found, the result of the initializer is `nil`.

> **Note**: This initializer is deprecated. Use the initializer `String.init?(validating: array, as: UTF8.self)` instead, remembering that “\0” is a valid character in Swift.

## Parameters

- `nullTerminatedUTF8`:  An array containing a null-terminated sequence of UTF-8 code units.

## See Also

### Converting a C String
- [init?<S>(bytes: S, encoding: String.Encoding)](./init%28bytes,encoding%29.md)
  Creates a new string equivalent to the given bytes interpreted in the specified encoding. Note: This API does not interpret embedded nulls as termination of the string. Use `String?(validatingCString:)` instead for null-terminated C strings.
- [init?(bytesNoCopy: UnsafeMutableRawPointer, length: Int, encoding: String.Encoding, freeWhenDone: Bool)](./init%28bytesnocopy,length,encoding,freewhendone%29.md)
  Creates a new string that contains the specified number of bytes from the given buffer, interpreted in the specified encoding, and optionally frees the buffer.
- [init?(validatingCString: UnsafePointer<CChar>)](./init%28validatingcstring%29-992vo.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(validatingcstring:)-98wra)*