# init(base64EncodedString:options:)

**Framework**: Foundation  
**Kind**: init

Initializes a data object with the given Base64 encoded string.

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
init?(base64Encoded base64String: String, options: NSData.Base64DecodingOptions = [])
```

#### Return Value

A data object built by Base64 decoding the provided string. Returns `nil` if the data object could not be decoded.

#### Discussion

The default implementation of this method will reject non-alphabet characters, including line break characters. To support different encodings and ignore non-alphabet characters, specify an `options` value of [`ignoreUnknownCharacters`](nsdata/base64decodingoptions/ignoreunknowncharacters.md).

## Parameters

- `base64String`: A Base-64 encoded string.
- `options`: A mask that specifies options for Base-64 decoding the data. Possible values are given in  .

## See Also

- [init?(base64EncodedData: Data, options: NSData.Base64DecodingOptions)](nsdata/init(base64encodeddata:options:).md)
  Initializes a data object with the given Base64 encoded data.
- [init?(base64Encoding: String)](nsdata/init(base64encoding:).md)
  Initializes a data object initialized with the given Base64 encoded string.
- [func base64EncodedData(options: NSData.Base64EncodingOptions) -> Data](nsdata/base64encodeddata(options:).md)
  Creates a Base64, UTF-8 encoded data object from the string using the given options.
- [func base64EncodedString(options: NSData.Base64EncodingOptions) -> String](nsdata/base64encodedstring(options:).md)
  Creates a Base64 encoded string from the string using the given options.
- [func base64Encoding() -> String](nsdata/base64encoding.md)
  Initializes a Base64 encoded string from the string.
- [NSData.Base64EncodingOptions](nsdata/base64encodingoptions.md)
  Options for methods used to Base64 encode data.
- [NSData.Base64DecodingOptions](nsdata/base64decodingoptions.md)
  Options to modify the decoding algorithm used to decode Base64 encoded data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(base64encodedstring:options:))*