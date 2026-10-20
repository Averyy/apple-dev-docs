# CKShareTransferRepresentation.ExportedShare

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

An intermediate structure that returns an existing share or prepares a new one if it doesn’t exist.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
struct ExportedShare
```

## Topics

### Accessing share attributes
- [static var transferRepresentation: some TransferRepresentation](./exportedshare/transferrepresentation.md)
  The representation the system uses to import and export the item.
### Preparing an exported share
- [static func existing(CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions) -> CKShareTransferRepresentation<Item>.ExportedShare](./exportedshare/existing%28_,container,allowedsharingoptions%29.md)
  Allows the user to view or make modifications to the share settings.
- [static func prepareShare(container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions, preparationHandler: () async throws -> CKShare) -> CKShareTransferRepresentation<Item>.ExportedShare](./exportedshare/prepareshare%28container,allowedsharingoptions,preparationhandler%29.md)
  Creates a share when the system calls the specified handler.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Transferable](../../CoreTransferable/transferable.md)

## See Also

### Accessing transfer representation attributes
- [var body: some TransferRepresentation](./body.md)
  The transfer representation for the share item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharetransferrepresentation/exportedshare)*