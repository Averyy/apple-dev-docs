# init(for:contentType:)

**Framework**: Core Transferable  
**Kind**: init

Creates a transfer representation for a given type and type identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(for itemType: Item.Type = Item.self, contentType: UTType) where Encoder == JSONEncoder, Decoder == JSONDecoder
```

#### Discussion

This initializer uses JSON for encoding and decoding.

## Parameters

- `itemType`: The concrete type of the item that’s being transferred.
- `contentType`: A uniform type identifier that best describes the item.

## See Also

- [init(for: Item.Type, contentType: UTType, encoder: Encoder, decoder: Decoder)](codablerepresentation/init(for:contenttype:encoder:decoder:).md)
  Creates a transfer representation for a given type with the encoder and decoder you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/codablerepresentation/init(for:contenttype:))*