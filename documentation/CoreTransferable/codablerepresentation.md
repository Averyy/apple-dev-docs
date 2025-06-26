# CodableRepresentation

**Framework**: Core Transferable  
**Kind**: struct

A transfer representation for types that participate in Swift’s protocols for encoding and decoding.

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
@preconcurrency
struct CodableRepresentation<Item, Encoder, Decoder> where Item : Transferable, Item : Decodable, Item : Encodable, Encoder : TopLevelEncoder, Encoder : Sendable, Decoder : TopLevelDecoder, Decoder : Sendable, Encoder.Output == Data, Decoder.Input == Data
```

## Mentions

- [Choosing a transfer representation for a model type](choosing-a-transfer-representation-for-a-model-type.md)

#### Overview

```swift
struct Todo: Codable, Transferable {
    var text: String
    var isDone = false

    static var transferRepresentation: some TransferRepresentation {
        CodableRepresentation(contentType: .todo)
    }
}

 extension UTType {
     static var todo: UTType { UTType(exportedAs: "com.example.todo") }
}
```

> ❗ **Important**: If your app declares custom uniform type identifiers, include corresponding entries in the app’s `Info.plist`. For more information, see [`Defining file and data types for your app`](https://developer.apple.com/documentation/UniformTypeIdentifiers/defining-file-and-data-types-for-your-app).

## Topics

### Creating a transfer representation
- [init(for: Item.Type, contentType: UTType)](codablerepresentation/init(for:contenttype:).md)
  Creates a transfer representation for a given type and type identifier.
- [init(for: Item.Type, contentType: UTType, encoder: Encoder, decoder: Decoder)](codablerepresentation/init(for:contenttype:encoder:decoder:).md)
  Creates a transfer representation for a given type with the encoder and decoder you supply.
### Type Aliases
- [CodableRepresentation.Body](codablerepresentation/body.md)
  The transfer representation for the item.
### Default Implementations
- [TransferRepresentation Implementations](codablerepresentation/transferrepresentation-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TransferRepresentation](transferrepresentation.md)

## See Also

- [struct DataRepresentation](datarepresentation.md)
  A transfer representation for types that provide their own binary data conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/codablerepresentation)*