# init(base64Encoding:)

**Framework**: Foundation  
**Kind**: init

Initializes a data object initialized with the given Base64 encoded string.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(base64Encoding base64String: String)
```

#### Return Value

A data object built by Base-64 decoding the provided string. Returns `nil` if the data object could not be decoded.

#### Discussion

Although this method was only introduced publicly for iOS 7, it has existed since iOS 4; you can use it if your application needs to target an operating system prior to iOS 7. This method behaves like [`init(base64EncodedString:options:)`](nsdata/init(base64encodedstring:options:).md), but ignores all unknown characters.

## Parameters

- `base64String`: A Base-64 encoded string.

## See Also

- [init?(base64EncodedData: Data, options: NSData.Base64DecodingOptions)](nsdata/init(base64encodeddata:options:).md)
  Initializes a data object with the given Base64 encoded data.
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
- [NSData.Base64DecodingOptions](nsdata/base64decodingoptions.md)
  Options to modify the decoding algorithm used to decode Base64 encoded data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(base64encoding:))*