# registerCloudKitShare(_:container:)

**Framework**: Foundation  
**Kind**: method

Registers a CloudKit share for the user to modify.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func registerCloudKitShare(_ share: CKShare, container: CKContainer)
```

#### Discussion

Use this method when the CloudKit share already exists on the server and you want to update it. The behavior of the sharing service depends on the role of the current user. An owner can edit the share’s configuration, which includes managing participants and their permissions. A participant can view the share’s configuration and choose to stop participating.

If you’re unsure which container to use, fetch the share’s metadata using [`CKFetchShareMetadataOperation`](https://developer.apple.com/documentation/CloudKit/CKFetchShareMetadataOperation). Then initialize an instance of [`CKContainer`](https://developer.apple.com/documentation/CloudKit/CKContainer) using the metadata’s [`containerIdentifier`](https://developer.apple.com/documentation/CloudKit/CKShare/Metadata/containerIdentifier) property.

Use the [`NSCloudSharingServiceDelegate`](https://developer.apple.com/documentation/AppKit/NSCloudSharingServiceDelegate) protocol to respond to any changes the sharing service makes.

> **Note**:  To create a new share, use the [`registerCloudKitShare(preparationHandler:)`](nsitemprovider/registercloudkitshare(preparationhandler:).md) method instead.

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

- [func registerCloudKitShare(preparationHandler: ((CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)](nsitemprovider/registercloudkitshare(preparationhandler:).md)
  Registers a handler that prepares a new CloudKit share.
- [func registerCKShare(CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions)](nsitemprovider/registerckshare(_:container:allowedsharingoptions:).md)
  Registers an existing collaboration object on a server.
- [func registerCKShare(container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions, preparationHandler: () async throws -> CKShare)](nsitemprovider/registerckshare(container:allowedsharingoptions:preparationhandler:).md)
  Creates and registers a new collaboration object using a collection of records to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registercloudkitshare(_:container:))*