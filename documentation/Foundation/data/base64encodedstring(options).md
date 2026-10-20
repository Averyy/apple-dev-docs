# base64EncodedString(options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Base-64 encoded string.

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
func base64EncodedString(options: Data.Base64EncodingOptions = []) -> String
```

#### Return Value

The Base-64 encoded string.

## Parameters

- `options`: The options to use for the encoding. Default value is `[]`.

## See Also

### Base-64 Encoding
- [func base64EncodedData(options: Data.Base64EncodingOptions) -> Data](./base64encodeddata%28options%29.md)
  Returns Base-64 encoded data.
- [typealias Base64DecodingOptions](./base64decodingoptions.md)
  Options to use when decoding data.
- [typealias Base64EncodingOptions](./base64encodingoptions.md)
  Options to use when encoding data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/base64encodedstring(options:))*