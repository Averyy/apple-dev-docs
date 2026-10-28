# decodeMarkdown(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

Decodes a value from the provided decoder.

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

## Return Value

The decoded value.

## Discussion

This method throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## Default Implementations

### MarkdownDecodableAttributedStringKey Implementations
- [static func decodeMarkdown(from: any Decoder) throws -> Self.Value](./decodemarkdown%28from%29-8vpq6.md)
  Decodes a value from the provided decoder, using a default implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/markdowndecodableattributedstringkey/decodemarkdown(from:))*