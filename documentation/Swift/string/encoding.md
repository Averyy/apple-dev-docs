# String.Encoding

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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
struct Encoding
```

## Topics

### Initializers
- [init?(ianaName: String)](./encoding/init%28iananame%29.md)
  Creates an instance from the name of the IANA registry “charset”.
### Instance Properties
- [var ianaName: String?](./encoding/iananame.md)
  The name of this encoding that is compatible with the one of the IANA registry “charset”.
### Type Properties
- [static let ascii: String.Encoding](./encoding/ascii.md)
- [static let iso2022JP: String.Encoding](./encoding/iso2022jp.md)
- [static let isoLatin1: String.Encoding](./encoding/isolatin1.md)
- [static let isoLatin2: String.Encoding](./encoding/isolatin2.md)
- [static let japaneseEUC: String.Encoding](./encoding/japaneseeuc.md)
- [static let macOSRoman: String.Encoding](./encoding/macosroman.md)
- [static let nextstep: String.Encoding](./encoding/nextstep.md)
- [static let nonLossyASCII: String.Encoding](./encoding/nonlossyascii.md)
- [static let shiftJIS: String.Encoding](./encoding/shiftjis.md)
- [static let symbol: String.Encoding](./encoding/symbol.md)
- [static let unicode: String.Encoding](./encoding/unicode.md)
- [static let utf16: String.Encoding](./encoding/utf16.md)
- [static let utf16BigEndian: String.Encoding](./encoding/utf16bigendian.md)
- [static let utf16LittleEndian: String.Encoding](./encoding/utf16littleendian.md)
- [static let utf32: String.Encoding](./encoding/utf32.md)
- [static let utf32BigEndian: String.Encoding](./encoding/utf32bigendian.md)
- [static let utf32LittleEndian: String.Encoding](./encoding/utf32littleendian.md)
- [static let utf8: String.Encoding](./encoding/utf8.md)
- [static let windowsCP1250: String.Encoding](./encoding/windowscp1250.md)
- [static let windowsCP1251: String.Encoding](./encoding/windowscp1251.md)
- [static let windowsCP1252: String.Encoding](./encoding/windowscp1252.md)
- [static let windowsCP1253: String.Encoding](./encoding/windowscp1253.md)
- [static let windowsCP1254: String.Encoding](./encoding/windowscp1254.md)

## Relationships

### Conforms To
- [Copyable](../copyable.md)
- [CustomStringConvertible](../customstringconvertible.md)
- [Equatable](../equatable.md)
- [Escapable](../escapable.md)
- [Hashable](../hashable.md)
- [RawRepresentable](../rawrepresentable.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)

## See Also

### Related String Types
- [struct Substring](../substring.md)
  A slice of a string.
- [protocol StringProtocol](../stringprotocol.md)
  A type that can represent a string as a collection of characters.
- [String.Index](./index.md)
  A position of a character or code unit in a string.
- [String.UnicodeScalarView](./unicodescalarview.md)
  A view of a string’s contents as a collection of Unicode scalar values.
- [String.UTF16View](./utf16view.md)
  A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](./utf8view.md)
  A view of a string’s contents as a collection of UTF-8 code units.
- [String.Iterator](./iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/encoding)*