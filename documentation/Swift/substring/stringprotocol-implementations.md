# StringProtocol Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Structures
- [Substring.UTF16View](./utf16view.md)
- [Substring.UTF8View](./utf8view.md)
- [Substring.UnicodeScalarView](./unicodescalarview.md)
### Operators
- [static func != <RHS>(Self, RHS) -> Bool](./noteq%28_,_%29-fryj.md)
- [static func == <RHS>(Self, RHS) -> Bool](./eqeq%28_,_%29.md)
- [static func > <RHS>(Self, RHS) -> Bool](./op%28_,_%29-6o7pz.md)
- [static func < <RHS>(Self, RHS) -> Bool](./op%28_,_%29-8d1w2.md)
- [static func <= <RHS>(Self, RHS) -> Bool](./opeq%28_,_%29-5y23r.md)
- [static func >= <RHS>(Self, RHS) -> Bool](./opeq%28_,_%29-nd7a.md)
### Initializers
- [init(cString: UnsafePointer<CChar>)](./init%28cstring%29.md)
  Creates a string from the null-terminated, UTF-8 encoded sequence of bytes at the given pointer.
- [init<C, Encoding>(decoding: C, as: Encoding.Type)](./init%28decoding,as%29.md)
  Creates a string from the given Unicode code units in the specified encoding.
- [init<Encoding>(decodingCString: UnsafePointer<Encoding.CodeUnit>, as: Encoding.Type)](./init%28decodingcstring,as%29.md)
  Creates a string from the null-terminated sequence of bytes at the given pointer.
### Instance Properties
- [var unicodeScalars: Substring.UnicodeScalarView](./unicodescalars.md)
- [var utf16: Substring.UTF16View](./utf16.md)
- [var utf8: Substring.UTF8View](./utf8.md)
### Instance Methods
- [func hasPrefix<Prefix>(Prefix) -> Bool](./hasprefix%28_%29.md)
  Returns a Boolean value indicating whether the string begins with the specified prefix.
- [func hasSuffix<Suffix>(Suffix) -> Bool](./hassuffix%28_%29.md)
  Returns a Boolean value indicating whether the string ends with the specified suffix.
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [func lowercased() -> String](./lowercased%28%29.md)
- [func uppercased() -> String](./uppercased%28%29.md)
- [func withCString<Result, E>((UnsafePointer<CChar>) throws(E) -> Result) throws(E) -> Result](./withcstring%28_%29.md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [func withCString<Result, TargetEncoding, E>(encodedAs: TargetEncoding.Type, (UnsafePointer<TargetEncoding.CodeUnit>) throws(E) -> Result) throws(E) -> Result](./withcstring%28encodedas,_%29.md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/stringprotocol-implementations)*