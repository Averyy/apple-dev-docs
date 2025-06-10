# NSData.Base64EncodingOptions

**Framework**: Foundation  
**Kind**: struct

Options for methods used to Base64 encode data.

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
struct Base64EncodingOptions
```

## Topics

### Initializers
- [init(rawValue: UInt)](nsdata/base64encodingoptions/init(rawvalue:).md)
### Constants
- [static var lineLength64Characters: NSData.Base64EncodingOptions](nsdata/base64encodingoptions/linelength64characters.md)
  Set the maximum line length to 64 characters, after which a line ending is inserted.
- [static var lineLength76Characters: NSData.Base64EncodingOptions](nsdata/base64encodingoptions/linelength76characters.md)
  Set the maximum line length to 76 characters, after which a line ending is inserted.
- [static var endLineWithCarriageReturn: NSData.Base64EncodingOptions](nsdata/base64encodingoptions/endlinewithcarriagereturn.md)
  When a maximum line length is set, specify that the line ending to insert should include a carriage return.
- [static var endLineWithLineFeed: NSData.Base64EncodingOptions](nsdata/base64encodingoptions/endlinewithlinefeed.md)
  When a maximum line length is set, specify that the line ending to insert should include a line feed.
- [static var lineLength64Characters: NSData.Base64EncodingOptions](nsdata/base64encodingoptions/linelength64characters.md)
  Set the maximum line length to 64 characters, after which a line ending is inserted.
- [static var lineLength76Characters: NSData.Base64EncodingOptions](nsdata/base64encodingoptions/linelength76characters.md)
  Set the maximum line length to 76 characters, after which a line ending is inserted.
- [static var endLineWithCarriageReturn: NSData.Base64EncodingOptions](nsdata/base64encodingoptions/endlinewithcarriagereturn.md)
  When a maximum line length is set, specify that the line ending to insert should include a carriage return.
- [static var endLineWithLineFeed: NSData.Base64EncodingOptions](nsdata/base64encodingoptions/endlinewithlinefeed.md)
  When a maximum line length is set, specify that the line ending to insert should include a line feed.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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
- [NSData.Base64DecodingOptions](nsdata/base64decodingoptions.md)
  Options to modify the decoding algorithm used to decode Base64 encoded data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/base64encodingoptions)*