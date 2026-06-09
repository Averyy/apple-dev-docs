# init(base64Encoded:options:)

**Framework**: Foundation  
**Kind**: init

Initializes a data object with the given Base64 encoded data.

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
init?(base64Encoded base64Data: Data, options: NSData.Base64DecodingOptions = [])
```

#### Return Value

A data object containing the Base64 decoded data. Returns `nil` if the data object could not be decoded.

#### Discussion

The default implementation of this method will reject non-alphabet characters, including line break characters. To support different encodings and ignore non-alphabet characters, specify an `options` value of [`ignoreUnknownCharacters`](nsdata/base64decodingoptions/ignoreunknowncharacters.md).

## Parameters

- `base64Data`: A Base64, UTF-8 encoded data object.
- `options`: A mask that specifies options for Base64 decoding the data. Possible values are given in [`NSData.Base64DecodingOptions`](nsdata/base64decodingoptions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(base64encoded:options:)-4t5yq)*