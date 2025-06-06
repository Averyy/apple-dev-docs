# StringProtocol Implementations

**Framework**: Swift

## Topics

### Structures
- [String.UTF16View](string/utf16view.md)
  A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](string/utf8view.md)
  A view of a string’s contents as a collection of UTF-8 code units.
- [String.UnicodeScalarView](string/unicodescalarview.md)
  A view of a string’s contents as a collection of Unicode scalar values.
### Operators
- [static func != <RHS>(Self, RHS) -> Bool](string/!=(_:_:)-frzf.md)
- [static func == <RHS>(Self, RHS) -> Bool](string/==(_:_:)-8kzxf.md)
- [static func > <RHS>(Self, RHS) -> Bool](string/_(_:_:)-6o7qv.md)
- [static func < <RHS>(Self, RHS) -> Bool](string/_(_:_:)-8d1wy.md)
- [static func <= <RHS>(Self, RHS) -> Bool](string/_=(_:_:)-5y22v.md)
- [static func >= <RHS>(Self, RHS) -> Bool](string/_=(_:_:)-nd86.md)
### Initializers
- [init(cString: UnsafePointer<CChar>)](string/init(cstring:)-2p84k.md)
  Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init<C, Encoding>(decoding: C, as: Encoding.Type)](string/init(decoding:as:).md)
  Creates a string from the given Unicode code units in the specified encoding.
- [init<Encoding>(decodingCString: UnsafePointer<Encoding.CodeUnit>, as: Encoding.Type)](string/init(decodingcstring:as:)-8yowf.md)
  Creates a new string by copying the null-terminated sequence of code units referenced by the given pointer.
### Instance Properties
- [var unicodeScalars: String.UnicodeScalarView](string/unicodescalars.md)
  The string’s value represented as a collection of Unicode scalar values.
- [var utf16: String.UTF16View](string/utf16.md)
  A UTF-16 encoding of `self`.
- [var utf8: String.UTF8View](string/utf8.md)
  A UTF-8 encoding of `self`.
### Instance Methods
- [func hasPrefix(String) -> Bool](string/hasprefix(_:).md)
- [func hasSuffix(String) -> Bool](string/hassuffix(_:).md)
- [func lowercased() -> String](string/lowercased.md)
  Returns a lowercase version of the string.
- [func uppercased() -> String](string/uppercased.md)
  Returns an uppercase version of the string.
- [func withCString<Result>((UnsafePointer<Int8>) throws -> Result) rethrows -> Result](string/withcstring(_:).md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [func withCString<Result, TargetEncoding>(encodedAs: TargetEncoding.Type, (UnsafePointer<TargetEncoding.CodeUnit>) throws -> Result) rethrows -> Result](string/withcstring(encodedas:_:).md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/stringprotocol-implementations)*