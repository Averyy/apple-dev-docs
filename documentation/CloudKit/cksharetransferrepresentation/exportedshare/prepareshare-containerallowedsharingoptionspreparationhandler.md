# prepareShare(container:allowedSharingOptions:preparationHandler:)

**Framework**: CloudKit  
**Kind**: method

Creates a share when the system calls the specified handler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
static func prepareShare(container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions = CKAllowedSharingOptions.standard, preparationHandler: @escaping () async throws -> CKShare) -> CKShareTransferRepresentation<Item>.ExportedShare
```

#### Return Value

The [`CKShareTransferRepresentation.ExportedShare`](cksharetransferrepresentation/exportedshare.md) with the new `CKShare`.

#### Discussion

Use this method when you want to share a collection of [`CKRecord`](ckrecord.md) objects, but don’t currently have a [`CKShare`](ckshare.md).

When the system calls the `preparationHandler`, create a new `CKShare` with the appropriate root `CKRecord` or [`CKRecordZone.ID`](ckrecordzone/id.md).

After saving the share and all records to the server, return the resulting `CKShare` or throw an error if saving fails. When your app invokes the share sheet with a `CKShare`, the system prompts the user to start sharing.

## Parameters

- `container`: The   for the share.
- `allowedSharingOptions`: The  . The   option is the default.
- `preparationHandler`: The handler the system calls in your app to create a new  .

## See Also

- [static func existing(CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions) -> CKShareTransferRepresentation<Item>.ExportedShare](cksharetransferrepresentation/exportedshare/existing(_:container:allowedsharingoptions:).md)
  Allows the user to view or make modifications to the share settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharetransferrepresentation/exportedshare/prepareshare(container:allowedsharingoptions:preparationhandler:))*