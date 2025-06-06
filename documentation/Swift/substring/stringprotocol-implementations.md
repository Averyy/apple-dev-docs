# StringProtocol Implementations

**Framework**: Swift

## Topics

### Structures
- [Substring.UTF16View](substring/utf16view.md)
- [Substring.UTF8View](substring/utf8view.md)
- [Substring.UnicodeScalarView](substring/unicodescalarview.md)
### Operators
- [static func != <RHS>(Self, RHS) -> Bool](substring/!=(_:_:)-fryj.md)
- [static func == <RHS>(Self, RHS) -> Bool](substring/==(_:_:).md)
- [static func > <RHS>(Self, RHS) -> Bool](substring/_(_:_:)-6o7pz.md)
- [static func < <RHS>(Self, RHS) -> Bool](substring/_(_:_:)-8d1w2.md)
- [static func <= <RHS>(Self, RHS) -> Bool](substring/_=(_:_:)-5y23r.md)
- [static func >= <RHS>(Self, RHS) -> Bool](substring/_=(_:_:)-nd7a.md)
### Initializers
- [init(cString: UnsafePointer<CChar>)](substring/init(cstring:).md)
  Creates a string from the null-terminated, UTF-8 encoded sequence of bytes at the given pointer.
- [init<C, Encoding>(decoding: C, as: Encoding.Type)](substring/init(decoding:as:).md)
  Creates a string from the given Unicode code units in the specified encoding.
- [init<Encoding>(decodingCString: UnsafePointer<Encoding.CodeUnit>, as: Encoding.Type)](substring/init(decodingcstring:as:).md)
  Creates a string from the null-terminated sequence of bytes at the given pointer.
### Instance Properties
- [var unicodeScalars: Substring.UnicodeScalarView](substring/unicodescalars.md)
- [var utf16: Substring.UTF16View](substring/utf16.md)
- [var utf8: Substring.UTF8View](substring/utf8.md)
### Instance Methods
- [func hasPrefix<Prefix>(Prefix) -> Bool](substring/hasprefix(_:).md)
  Returns a Boolean value indicating whether the string begins with the specified prefix.
- [func hasSuffix<Suffix>(Suffix) -> Bool](substring/hassuffix(_:).md)
  Returns a Boolean value indicating whether the string ends with the specified suffix.
- [func hash(into: inout Hasher)](substring/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [func lowercased() -> String](substring/lowercased.md)
- [func uppercased() -> String](substring/uppercased.md)
- [func withCString<Result>((UnsafePointer<CChar>) throws -> Result) rethrows -> Result](substring/withcstring(_:).md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [func withCString<Result, TargetEncoding>(encodedAs: TargetEncoding.Type, (UnsafePointer<TargetEncoding.CodeUnit>) throws -> Result) rethrows -> Result](substring/withcstring(encodedas:_:).md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/stringprotocol-implementations)*