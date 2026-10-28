# init(exporter:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates and initializes a transfer representation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
init(exporter: @escaping @Sendable (Item) throws -> CKShareTransferRepresentation<Item>.ExportedShare)
```

## Return Value

A [`CKShareTransferRepresentation.ExportedShare`](./exportedshare.md).

## Parameters

- `exporter`: A closure that provides a [`CKShareTransferRepresentation.ExportedShare`](./exportedshare.md) representation of the specified `Item`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharetransferrepresentation/init(exporter:))*