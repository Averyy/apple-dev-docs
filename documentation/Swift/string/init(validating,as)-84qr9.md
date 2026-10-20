# init(validating:as:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.

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
init?<Encoding>(validating codeUnits: some Sequence, as encoding: Encoding.Type) where Encoding : _UnicodeEncoding
```

#### Discussion

This initializer does not try to repair ill-formed code unit sequences. If any are found, the result of the initializer is `nil`.

The following example calls this initializer with the contents of two different arrays—first with a well-formed UTF-8 code unit sequence and then with an ill-formed UTF-16 code unit sequence.

```swift
let validUTF8: [UInt8] = [67, 97, 0, 102, 195, 169]
let valid = String(validating: validUTF8, as: UTF8.self)
print(valid ?? "nil")
// Prints "Café"

let invalidUTF16: [UInt16] = [0x41, 0x42, 0xd801]
let invalid = String(validating: invalidUTF16, as: UTF16.self)
print(invalid ?? "nil")
// Prints "nil"
```

## Parameters

- `codeUnits`: A sequence of code units that encode a `String`
- `encoding`: A conformer to `Unicode.Encoding` to be used to decode `codeUnits`.

## See Also

### Creating a String from Unicode Data
- [init(Unicode.Scalar)](./init%28_%29-8ay23.md)
- [init?(data: Data, encoding: String.Encoding)](./init%28data,encoding%29.md)
  Returns a `String` initialized by converting given `data` into Unicode characters using a given `encoding`.
- [init?(validatingUTF8: UnsafePointer<CChar>)](./init%28validatingutf8%29-208fn.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(validating:as:)-84qr9)*