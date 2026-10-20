# base64Encoding()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes a Base64 encoded string from the string.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 4.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: You should transition to either [`base64EncodedString(options:)`](./base64encodedstring%28options%29.md) or [`base64EncodedData(options:)`](./base64encodeddata%28options%29.md)

## Declaration

```swift
func base64Encoding() -> String
```

```objc
- (NSString *) base64Encoding;
```

#### Return Value

A Base-64 encoded string.

#### Discussion

This method is equivalent to calling [`base64EncodedString(options:)`](./base64encodedstring%28options%29.md) with no options specified.

##### Special Considerations

Although this method was only introduced publicly for iOS 7, it has existed since iOS 4; you can use it if your application needs to target an operating system prior to iOS 7.

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
- [NSData.Base64EncodingOptions](./base64encodingoptions.md)
  Options for methods used to Base64 encode data.
- [NSData.Base64DecodingOptions](./base64decodingoptions.md)
  Options to modify the decoding algorithm used to decode Base64 encoded data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/base64encoding())*