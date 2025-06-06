# init(for:contentType:encoder:decoder:)

**Framework**: Core Transferable  
**Kind**: init

Creates a transfer representation for a given type with the encoder and decoder you supply.

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
init(for itemType: Item.Type = Item.self, contentType: UTType, encoder: Encoder, decoder: Decoder)
```

## Parameters

- `itemType`: The concrete type of the item that’s being transported.
- `contentType`: A uniform type identifier that best describes the item.
- `encoder`: An instance of a type that can convert the item being transferred   into binary data with a specific structure.
- `decoder`: An instance of a type that can convert specifically structured   binary data into the item being transferred.

## See Also

- [init(for: Item.Type, contentType: UTType)](codablerepresentation/init(for:contenttype:).md)
  Creates a transfer representation for a given type and type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/codablerepresentation/init(for:contenttype:encoder:decoder:))*