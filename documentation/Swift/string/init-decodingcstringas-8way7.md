# init(decodingCString:as:)

**Framework**: Swift  
**Kind**: init

Creates a new string by copying the null-terminated sequence of code units referenced by the given array.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift ?+

## Declaration

```swift
init<Encoding>(decodingCString nullTerminatedCodeUnits: [Encoding.CodeUnit], as encoding: Encoding.Type) where Encoding : _UnicodeEncoding
```

#### Discussion

If `nullTerminatedCodeUnits` contains ill-formed code unit sequences, this initializer replaces them with the Unicode replacement character (`"\u{FFFD}"`).

> **Note**: This initializer is deprecated. Use the initializer `String.init(decoding: array, as: Encoding.self)` instead, remembering that “\0” is a valid character in Swift.

## Parameters

- `nullTerminatedCodeUnits`: An array containing a null-terminated   sequence of code units encoded in  .
- `encoding`: The encoding in which the code units should be   interpreted.

## See Also

- [init?<S>(bytes: S, encoding: String.Encoding)](string/init(bytes:encoding:).md)
  Creates a new string equivalent to the given bytes interpreted in the specified encoding. Note: This API does not interpret embedded nulls as termination of the string. Use `String?(validatingCString:)` instead for null-terminated C strings.
- [init?(bytesNoCopy: UnsafeMutableRawPointer, length: Int, encoding: String.Encoding, freeWhenDone: Bool)](string/init(bytesnocopy:length:encoding:freewhendone:).md)
  Creates a new string that contains the specified number of bytes from the given buffer, interpreted in the specified encoding, and optionally frees the buffer.
- [init?(validatingCString: UnsafePointer<CChar>)](string/init(validatingcstring:)-992vo.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init?(validatingCString: [CChar])](string/init(validatingcstring:)-98wra.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.
- [init(cString: UnsafePointer<CChar>)](string/init(cstring:)-2p84k.md)
  Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString: UnsafePointer<UInt8>)](string/init(cstring:)-6kr8s.md)
  Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init?(cString: [CChar], encoding: String.Encoding)](string/init(cstring:encoding:)-3h7bc.md)
  Produces a string by copying the null-terminated bytes in a given array, interpreted according to a given encoding.
- [init?(cString: UnsafePointer<CChar>, encoding: String.Encoding)](string/init(cstring:encoding:)-3qgzd.md)
  Produces a string by copying the null-terminated bytes in a given C array, interpreted according to a given encoding.
- [static func decodeCString<Encoding>(UnsafePointer<Encoding.CodeUnit>?, as: Encoding.Type, repairingInvalidCodeUnits: Bool) -> (result: String, repairsMade: Bool)?](string/decodecstring(_:as:repairinginvalidcodeunits:)-46n2p.md)
  Creates a new string by copying the null-terminated data referenced by the given pointer using the specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(decodingcstring:as:)-8way7)*