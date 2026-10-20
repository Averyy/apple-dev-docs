# base64EncodedString(options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a Base64 encoded string from the string using the given options.

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
func base64EncodedString(options: NSData.Base64EncodingOptions = []) -> String
```

```objc
- (NSString *) base64EncodedStringWithOptions:(NSDataBase64EncodingOptions) options;
```

#### Return Value

A Base64 encoded string.

#### Discussion

By default, no line endings are inserted.

If you specify one of the line length options ([`lineLength64Characters`](./base64encodingoptions/linelength64characters.md) or [`lineLength76Characters`](./base64encodingoptions/linelength76characters.md)) but don’t specify the kind of line ending to insert, the default line ending is Carriage Return + Line Feed.

## Parameters

- `options`: A mask that specifies options for Base-64 encoding the data. Possible values are given in [`NSData.Base64EncodingOptions`](./base64encodingoptions.md).

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
- [func base64Encoding() -> String](./base64encoding%28%29.md)
  Initializes a Base64 encoded string from the string.
- [NSData.Base64EncodingOptions](./base64encodingoptions.md)
  Options for methods used to Base64 encode data.
- [NSData.Base64DecodingOptions](./base64decodingoptions.md)
  Options to modify the decoding algorithm used to decode Base64 encoded data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/base64encodedstring(options:))*