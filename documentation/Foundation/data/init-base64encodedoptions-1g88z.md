# init(base64Encoded:options:)

**Framework**: Foundation  
**Kind**: init

Initialize a `Data` from a Base-64, UTF-8 encoded `Data`.

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
init?(base64Encoded base64Data: Data, options: Data.Base64DecodingOptions = [])
```

#### Discussion

Returns nil when the input is not recognized as valid Base-64.

## Parameters

- `base64Data`: Base-64, UTF-8 encoded input data.
- `options`: Decoding options. Default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/init(base64encoded:options:)-1g88z)*