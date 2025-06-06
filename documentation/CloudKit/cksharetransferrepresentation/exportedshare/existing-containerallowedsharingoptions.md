# existing(_:container:allowedSharingOptions:)

**Framework**: CloudKit  
**Kind**: method

Allows the user to view or make modifications to the share settings.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
static func existing(_ share: CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions = CKAllowedSharingOptions.standard) -> CKShareTransferRepresentation<Item>.ExportedShare
```

#### Return Value

The [`CKShareTransferRepresentation.ExportedShare`](cksharetransferrepresentation/exportedshare.md) with updated share settings.

#### Discussion

Use this method when you have a share that’s already saved to the server.

When the system invokes the share sheet with a [`CKShare`](ckshare.md) registered with this method, the system allows the owner to make modifications to the share settings, or allows a participant to view the share settings.

## Parameters

- `share`: The existing   object.
- `container`: The   for the share.
- `allowedSharingOptions`: The  . The   option is the default.

## See Also

- [static func prepareShare(container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions, preparationHandler: () async throws -> CKShare) -> CKShareTransferRepresentation<Item>.ExportedShare](cksharetransferrepresentation/exportedshare/prepareshare(container:allowedsharingoptions:preparationhandler:).md)
  Creates a share when the system calls the specified handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharetransferrepresentation/exportedshare/existing(_:container:allowedsharingoptions:))*