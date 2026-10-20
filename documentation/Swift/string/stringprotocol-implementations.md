# StringProtocol Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Structures
- [String.UTF16View](./utf16view.md)
  A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](./utf8view.md)
  A view of a string’s contents as a collection of UTF-8 code units.
- [String.UnicodeScalarView](./unicodescalarview.md)
  A view of a string’s contents as a collection of Unicode scalar values.
### Operators
- [static func != <RHS>(Self, RHS) -> Bool](./noteq%28_,_%29-frzf.md)
- [static func == <RHS>(Self, RHS) -> Bool](./eqeq%28_,_%29-8kzxf.md)
- [static func > <RHS>(Self, RHS) -> Bool](./op%28_,_%29-6o7qv.md)
- [static func < <RHS>(Self, RHS) -> Bool](./op%28_,_%29-8d1wy.md)
- [static func <= <RHS>(Self, RHS) -> Bool](./opeq%28_,_%29-5y22v.md)
- [static func >= <RHS>(Self, RHS) -> Bool](./opeq%28_,_%29-nd86.md)
### Initializers
- [init(cString: UnsafePointer<CChar>)](./init%28cstring%29-2p84k.md)
  Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init<C, Encoding>(decoding: C, as: Encoding.Type)](./init%28decoding,as%29.md)
  Creates a string from the given Unicode code units in the specified encoding.
- [init<Encoding>(decodingCString: UnsafePointer<Encoding.CodeUnit>, as: Encoding.Type)](./init%28decodingcstring,as%29-8yowf.md)
  Creates a new string by copying the null-terminated sequence of code units referenced by the given pointer.
### Instance Properties
- [var unicodeScalars: String.UnicodeScalarView](./unicodescalars.md)
  The string’s value represented as a collection of Unicode scalar values.
- [var utf16: String.UTF16View](./utf16.md)
  A UTF-16 encoding of `self`.
- [var utf8: String.UTF8View](./utf8.md)
  A UTF-8 encoding of `self`.
### Instance Methods
- [func hasPrefix(String) -> Bool](./hasprefix%28_%29.md)
- [func hasSuffix(String) -> Bool](./hassuffix%28_%29.md)
- [func lowercased() -> String](./lowercased%28%29.md)
  Returns a lowercase version of the string.
- [func uppercased() -> String](./uppercased%28%29.md)
  Returns an uppercase version of the string.
- [func withCString<Result, E>((UnsafePointer<Int8>) throws(E) -> Result) throws(E) -> Result](./withcstring%28_%29.md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [func withCString<Result, TargetEncoding, E>(encodedAs: TargetEncoding.Type, (UnsafePointer<TargetEncoding.CodeUnit>) throws(E) -> Result) throws(E) -> Result](./withcstring%28encodedas,_%29.md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/stringprotocol-implementations)*