# registerCloudKitShare(_:container:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Registers a CloudKit share for the user to modify.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func registerCloudKitShare(_ share: CKShare, container: CKContainer)
```

```objc
- (void) registerCloudKitShare:(CKShare *) share container:(CKContainer *) container;
```

#### Discussion

Use this method when the CloudKit share already exists on the server and you want to update it. The behavior of the sharing service depends on the role of the current user. An owner can edit the share’s configuration, which includes managing participants and their permissions. A participant can view the share’s configuration and choose to stop participating.

If you’re unsure which container to use, fetch the share’s metadata using [`CKFetchShareMetadataOperation`](../../CloudKit/ckfetchsharemetadataoperation.md). Then initialize an instance of [`CKContainer`](../../CloudKit/ckcontainer.md) using the metadata’s [`containerIdentifier`](../../CloudKit/ckshare/metadata/containeridentifier.md) property.

Use the [`NSCloudSharingServiceDelegate`](../../AppKit/nscloudsharingservicedelegate.md) protocol to respond to any changes the sharing service makes.

> **Note**:  To create a new share, use the [`registerCloudKitShare(preparationHandler:)`](./registercloudkitshare%28preparationhandler%29.md) method instead.

The following example shows how to create an item provider with an existing share. It then invokes the cloud-sharing service with the provider and presents the share’s configuration to the user.

```swift
func modifyShare(_ share: CKShare, in container: CKContainer) {

    // Create an item provider and register a share that
    // already exists on the server.
    let itemProvider = NSItemProvider()
    itemProvider.registerCloudKitShare(share, container: container)
        
    // Create and invoke the cloud-sharing service to
    // present the share configuration to the user.
    if let service = NSSharingService(named: .cloudSharing),
       service.canPerform(withItems: [itemProvider]) {
        service.perform(withItems: [itemProvider])
    }
}
```

## Parameters

- `share`: The CloudKit share to modify.
- `container`: The CloudKit container that stores the shared records.

## See Also

### Registering CloudKit shares
- [func registerCloudKitShare(preparationHandler: ((CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)](./registercloudkitshare%28preparationhandler%29.md)
  Registers a handler that prepares a new CloudKit share.
- [func registerCKShare(CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions)](./registerckshare%28_,container,allowedsharingoptions%29.md)
  Registers an existing collaboration object on a server.
- [func registerCKShare(container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions, preparationHandler: () async throws -> CKShare)](./registerckshare%28container,allowedsharingoptions,preparationhandler%29.md)
  Creates and registers a new collaboration object using a collection of records to share.
- [- registerCKShare:container:allowedSharingOptions:](./registerckshare_container_allowedsharingoptions_.md)
  Registers an existing collaboration object on a server.
- [- registerCKShareWithContainer:allowedSharingOptions:preparationHandler:](./registercksharewithcontainer_allowedsharingoptions_preparationhandler_.md)
  Creates and registers a new collaboration object using a collection of records to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registercloudkitshare(_:container:))*