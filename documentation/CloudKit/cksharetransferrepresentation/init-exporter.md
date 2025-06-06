# init(exporter:)

**Framework**: CloudKit  
**Kind**: init

Creates and initializes a transfer representation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
init(exporter: @escaping (Item) throws -> CKShareTransferRepresentation<Item>.ExportedShare)
```

#### Return Value

A [`CKShareTransferRepresentation.ExportedShare`](cksharetransferrepresentation/exportedshare.md).

## Parameters

- `exporter`: A closure that provides a   representation of the specified  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharetransferrepresentation/init(exporter:))*