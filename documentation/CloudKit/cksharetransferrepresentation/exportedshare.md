# CKShareTransferRepresentation.ExportedShare

**Framework**: CloudKit  
**Kind**: struct

An intermediate structure that returns an existing share or prepares a new one if it doesn’t exist.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
struct ExportedShare
```

## Topics

### Preparing an exported share
- [static func existing(CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions) -> CKShareTransferRepresentation<Item>.ExportedShare](cksharetransferrepresentation/exportedshare/existing(_:container:allowedsharingoptions:).md)
  Allows the user to view or make modifications to the share settings.
- [static func prepareShare(container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions, preparationHandler: () async throws -> CKShare) -> CKShareTransferRepresentation<Item>.ExportedShare](cksharetransferrepresentation/exportedshare/prepareshare(container:allowedsharingoptions:preparationhandler:).md)
  Creates a share when the system calls the specified handler.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transferable](../CoreTransferable/Transferable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharetransferrepresentation/exportedshare)*