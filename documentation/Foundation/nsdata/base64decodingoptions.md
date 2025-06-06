# NSData.Base64DecodingOptions

**Framework**: Foundation  
**Kind**: struct

Options to modify the decoding algorithm used to decode Base64 encoded data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Base64DecodingOptions
```

## Topics

### Initializers
- [init(rawValue: UInt)](nsdata/base64decodingoptions/init(rawvalue:).md)
### Constants
- [static var ignoreUnknownCharacters: NSData.Base64DecodingOptions](nsdata/base64decodingoptions/ignoreunknowncharacters.md)
  Modify the decoding algorithm so that it ignores unknown non-Base-64 bytes, including line ending characters.
- [static var ignoreUnknownCharacters: NSData.Base64DecodingOptions](nsdata/base64decodingoptions/ignoreunknowncharacters.md)
  Modify the decoding algorithm so that it ignores unknown non-Base-64 bytes, including line ending characters.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [init?(base64EncodedData: Data, options: NSData.Base64DecodingOptions)](nsdata/init(base64encodeddata:options:).md)
  Initializes a data object with the given Base64 encoded data.
- [init?(base64Encoding: String)](nsdata/init(base64encoding:).md)
  Initializes a data object initialized with the given Base64 encoded string.
- [init?(base64EncodedString: String, options: NSData.Base64DecodingOptions)](nsdata/init(base64encodedstring:options:).md)
  Initializes a data object with the given Base64 encoded string.
- [func base64EncodedData(options: NSData.Base64EncodingOptions) -> Data](nsdata/base64encodeddata(options:).md)
  Creates a Base64, UTF-8 encoded data object from the string using the given options.
- [func base64EncodedString(options: NSData.Base64EncodingOptions) -> String](nsdata/base64encodedstring(options:).md)
  Creates a Base64 encoded string from the string using the given options.
- [func base64Encoding() -> String](nsdata/base64encoding.md)
  Initializes a Base64 encoded string from the string.
- [NSData.Base64EncodingOptions](nsdata/base64encodingoptions.md)
  Options for methods used to Base64 encode data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/base64decodingoptions)*