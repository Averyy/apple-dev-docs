# init(validating:as:)

**Framework**: Swift  
**Kind**: init

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
init?<Encoding>(validating codeUnits: some Sequence<Int8>, as encoding: Encoding.Type) where Encoding : _UnicodeEncoding, Encoding.CodeUnit == UInt8
```

#### Discussion

This initializer does not try to repair ill-formed code unit sequences. If any are found, the result of the initializer is `nil`.

The following example calls this initializer with the contents of two different arrays—first with a well-formed UTF-8 code unit sequence and then with an ill-formed ASCII code unit sequence.

```swift
let validUTF8: [Int8] = [67, 97, 0, 102, -61, -87]
let valid = String(validating: validUTF8, as: UTF8.self)
print(valid ?? "nil")
// Prints "Café"

let invalidASCII: [Int8] = [67, 97, -5]
let invalid = String(validating: invalidASCII, as: Unicode.ASCII.self)
print(invalid ?? "nil")
// Prints "nil"
```

## Parameters

- `codeUnits`: A sequence of code units that encode a 
- `encoding`: A conformer to   that can decode    as 

## See Also

- [init(Unicode.Scalar)](string/init(_:)-8ay23.md)
- [init?(data: Data, encoding: String.Encoding)](string/init(data:encoding:).md)
  Returns a `String` initialized by converting given `data` into Unicode characters using a given `encoding`.
- [init?(validatingUTF8: UnsafePointer<CChar>)](string/init(validatingutf8:)-208fn.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init?<Encoding>(validating: some Sequence, as: Encoding.Type)](string/init(validating:as:)-84qr9.md)
  Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init?(utf8String: [CChar])](string/init(utf8string:)-8qmaq.md)
  Creates a string by copying the data from a given null-terminated array of UTF8-encoded bytes.
- [init?(utf8String: UnsafePointer<CChar>)](string/init(utf8string:)-3mcco.md)
  Creates a string by copying the data from a given null-terminated C array of UTF8-encoded bytes.
- [init(utf16CodeUnits: UnsafePointer<unichar>, count: Int)](string/init(utf16codeunits:count:).md)
  Creates a new string that contains the specified number of characters from the given C array of Unicode characters.
- [init(utf16CodeUnitsNoCopy: UnsafePointer<unichar>, count: Int, freeWhenDone: Bool)](string/init(utf16codeunitsnocopy:count:freewhendone:).md)
  Creates a new string that contains the specified number of characters from the given C array of UTF-16 code units.
- [init<C, Encoding>(decoding: C, as: Encoding.Type)](string/init(decoding:as:).md)
  Creates a string from the given Unicode code units in the specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(validating:as:)-5cw2c)*