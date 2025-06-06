# base64Encoding()

**Framework**: Foundation  
**Kind**: method

Initializes a Base64 encoded string from the string.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func base64Encoding() -> String
```

#### Return Value

A Base-64 encoded string.

#### Discussion

This method is equivalent to calling [`base64EncodedString(options:)`](nsdata/base64encodedstring(options:).md) with no options specified.

##### Special Considerations

Although this method was only introduced publicly for iOS 7, it has existed since iOS 4; you can use it if your application needs to target an operating system prior to iOS 7.

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
- [NSData.Base64EncodingOptions](nsdata/base64encodingoptions.md)
  Options for methods used to Base64 encode data.
- [NSData.Base64DecodingOptions](nsdata/base64decodingoptions.md)
  Options to modify the decoding algorithm used to decode Base64 encoded data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/base64encoding())*