# base64EncodedData(options:)

**Framework**: Foundation  
**Kind**: method

Returns Base-64 encoded data.

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
func base64EncodedData(options: Data.Base64EncodingOptions = []) -> Data
```

#### Return Value

The Base-64 encoded data.

## Parameters

- `options`: The options to use for the encoding. Default value is  .

## See Also

- [func base64EncodedString(options: Data.Base64EncodingOptions) -> String](data/base64encodedstring(options:).md)
  Returns a Base-64 encoded string.
- [typealias Base64DecodingOptions](data/base64decodingoptions.md)
  Options to use when decoding data.
- [typealias Base64EncodingOptions](data/base64encodingoptions.md)
  Options to use when encoding data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/base64encodeddata(options:))*