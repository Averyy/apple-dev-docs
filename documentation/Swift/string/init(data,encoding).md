# init(data:encoding:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Returns a `String` initialized by converting given `data` into Unicode characters using a given `encoding`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(data: Data, encoding: String.Encoding)
```

## See Also

### Creating a String from Unicode Data
- [init(Unicode.Scalar)](./init%28_%29-8ay23.md)
- [init?(validatingUTF8: UnsafePointer<CChar>)](./init%28validatingutf8%29-208fn.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init?<Encoding>(validating: some Sequence, as: Encoding.Type)](./init%28validating,as%29-84qr9.md)
  Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init?<Encoding>(validating: some Sequence<Int8>, as: Encoding.Type)](./init%28validating,as%29-5cw2c.md)
  Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init?(utf8String: [CChar])](./init%28utf8string%29-8qmaq.md)
  Creates a string by copying the data from a given null-terminated array of UTF8-encoded bytes.
- [init?(utf8String: UnsafePointer<CChar>)](./init%28utf8string%29-3mcco.md)
  Creates a string by copying the data from a given null-terminated C array of UTF8-encoded bytes.
- [init(utf16CodeUnits: UnsafePointer<unichar>, count: Int)](./init%28utf16codeunits,count%29.md)
  Creates a new string that contains the specified number of characters from the given C array of Unicode characters.
- [init(utf16CodeUnitsNoCopy: UnsafePointer<unichar>, count: Int, freeWhenDone: Bool)](./init%28utf16codeunitsnocopy,count,freewhendone%29.md)
  Creates a new string that contains the specified number of characters from the given C array of UTF-16 code units.
- [init<C, Encoding>(decoding: C, as: Encoding.Type)](./init%28decoding,as%29.md)
  Creates a string from the given Unicode code units in the specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(data:encoding:))*