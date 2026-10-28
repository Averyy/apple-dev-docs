# decodeMarkdown(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Decodes a value from the provided decoder, using a default implementation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func decodeMarkdown(from decoder: any Decoder) throws -> Self.Value
```

Available when `Self` conforms to `DecodableAttributedStringKey`.

## Return Value

The decoded value.

## Discussion

The default implementation calls [`decode(from:)`](../decodableattributedstringkey/decode%28from%29.md), inherited from [`DecodableAttributedStringKey`](../decodableattributedstringkey.md), meaning it uses the same decoding as non-Markdown encoding.

This method throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/markdowndecodableattributedstringkey/decodemarkdown(from:)-8vpq6)*