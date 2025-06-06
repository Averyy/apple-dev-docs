# base64EncodedData(options:)

**Framework**: Foundation  
**Kind**: method

Creates a Base64, UTF-8 encoded data object from the string using the given options.

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
func base64EncodedData(options: NSData.Base64EncodingOptions = []) -> Data
```

#### Return Value

A Base64, UTF-8 encoded data object.

#### Discussion

By default, no line endings are inserted.

If you specify one of the line length options ([`lineLength64Characters`](nsdata/base64encodingoptions/linelength64characters.md) or [`lineLength76Characters`](nsdata/base64encodingoptions/linelength76characters.md)) but don’t specify the kind of line ending to insert, the default line ending is Carriage Return + Line Feed.

## Parameters

- `options`: A mask that specifies options for Base64 encoding the data. Possible values are given in  .

## See Also

- [init?(base64EncodedData: Data, options: NSData.Base64DecodingOptions)](nsdata/init(base64encodeddata:options:).md)
  Initializes a data object with the given Base64 encoded data.
- [init?(base64Encoding: String)](nsdata/init(base64encoding:).md)
  Initializes a data object initialized with the given Base64 encoded string.
- [init?(base64EncodedString: String, options: NSData.Base64DecodingOptions)](nsdata/init(base64encodedstring:options:).md)
  Initializes a data object with the given Base64 encoded string.
- [func base64EncodedString(options: NSData.Base64EncodingOptions) -> String](nsdata/base64encodedstring(options:).md)
  Creates a Base64 encoded string from the string using the given options.
- [func base64Encoding() -> String](nsdata/base64encoding.md)
  Initializes a Base64 encoded string from the string.
- [NSData.Base64EncodingOptions](nsdata/base64encodingoptions.md)
  Options for methods used to Base64 encode data.
- [NSData.Base64DecodingOptions](nsdata/base64decodingoptions.md)
  Options to modify the decoding algorithm used to decode Base64 encoded data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/base64encodeddata(options:))*