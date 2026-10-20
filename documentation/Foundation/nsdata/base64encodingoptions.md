# NSData.Base64EncodingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSDataBase64EncodingOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./base64encodingoptions/init%28rawvalue%29.md)
### Constants
- [static var lineLength64Characters: NSData.Base64EncodingOptions](./base64encodingoptions/linelength64characters.md)
  Set the maximum line length to 64 characters, after which a line ending is inserted.
- [static var lineLength76Characters: NSData.Base64EncodingOptions](./base64encodingoptions/linelength76characters.md)
  Set the maximum line length to 76 characters, after which a line ending is inserted.
- [static var endLineWithCarriageReturn: NSData.Base64EncodingOptions](./base64encodingoptions/endlinewithcarriagereturn.md)
  When a maximum line length is set, specify that the line ending to insert should include a carriage return.
- [static var endLineWithLineFeed: NSData.Base64EncodingOptions](./base64encodingoptions/endlinewithlinefeed.md)
  When a maximum line length is set, specify that the line ending to insert should include a line feed.
### Type Properties
- [static let base64URLAlphabet: NSData.Base64EncodingOptions](./base64encodingoptions/base64urlalphabet.md)
  Use the base64url alphabet to encode the data
- [static let omitPaddingCharacter: NSData.Base64EncodingOptions](./base64encodingoptions/omitpaddingcharacter.md)
  Omit the `=` padding characters in the end of the base64 encoded result

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Encoding and Decoding Base64 Representations
- [init?(base64EncodedData: Data, options: NSData.Base64DecodingOptions)](./init%28base64encodeddata,options%29.md)
  Initializes a data object with the given Base64 encoded data.
- [init?(base64Encoding: String)](./init%28base64encoding%29.md)
  Initializes a data object initialized with the given Base64 encoded string.
- [init?(base64EncodedString: String, options: NSData.Base64DecodingOptions)](./init%28base64encodedstring,options%29.md)
  Initializes a data object with the given Base64 encoded string.
- [func base64EncodedData(options: NSData.Base64EncodingOptions) -> Data](./base64encodeddata%28options%29.md)
  Creates a Base64, UTF-8 encoded data object from the string using the given options.
- [func base64EncodedString(options: NSData.Base64EncodingOptions) -> String](./base64encodedstring%28options%29.md)
  Creates a Base64 encoded string from the string using the given options.
- [func base64Encoding() -> String](./base64encoding%28%29.md)
  Initializes a Base64 encoded string from the string.
- [NSData.Base64DecodingOptions](./base64decodingoptions.md)
  Options to modify the decoding algorithm used to decode Base64 encoded data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/base64encodingoptions)*