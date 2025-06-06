# registerCloudKitShare(preparationHandler:)

**Framework**: Foundation  
**Kind**: method

Registers a handler that prepares a new CloudKit share.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func registerCloudKitShare(preparationHandler: @escaping (@escaping (CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)
```

#### Discussion

Use this method to share a hierarchy of CloudKit records with other iCloud users. When the service invokes the handler, create an instance of [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) with a root record. Save the share to the server using [`CKModifyRecordsOperation`](https://developer.apple.com/documentation/CloudKit/CKModifyRecordsOperation). The root record (and its hierarchy) must already exist on the server or be part of the same save operation. After the share saves, call `preparationCompletionHandler` with the saved share and its container. If the save fails, pass the error to the completion handler instead. Invoking the sharing service with a share you register using this method prompts the user to begin sharing.

Use the [`NSCloudSharingServiceDelegate`](https://developer.apple.com/documentation/AppKit/NSCloudSharingServiceDelegate) protocol to respond to any changes the sharing service makes.

> **Note**:  To modify an existing share, use the [`registerCloudKitShare(_:container:)`](nsitemprovider/registercloudkitshare(_:container:).md) method instead.

 To modify an existing share, use the [`registerCloudKitShare(_:container:)`](nsitemprovider/registercloudkitshare(_:container:).md) method instead.

The following example shows how to create an item provider with a handler that saves a share. It then invokes the cloud-sharing service with that provider.

```swift
func beginSharing(_ record: CKRecord) {
    let itemProvider = NSItemProvider()
        
    // Register a handler that creates a CloudKit share using
    // the provided record, and saves them both to the server
    // before passing them to the sharing service.
    itemProvider.registerCloudKitShare(preparationHandler: { completion in
        let container = CKContainer.default()
            
        // Create a share and use the record the caller provides as 
        // its root record. 
        let share = CKShare(rootRecord: record)

        // Create an operation that saves both the record and the 
        // share to CloudKit.
        let records = [record, share]
        let operation = CKModifyRecordsOperation(recordsToSave: records, 
                                                 recordIDsToDelete: nil)
            
        // If the save fails, pass the error to the completion handler.
        // Otherwise, pass the new share and its container.
        operation.modifyRecordsCompletionBlock = { _, _, error in
            if let error = error {
                completion(nil, nil, error)
            } else {
                completion(share, container, nil)
            }
        }
            
        // Set an appropriate QoS and add the operation to the
        // container's queue to execute it.
        operation.qualityOfService = .userInitiated
        container.privateCloudDatabase.add(operation)
    })
        
    let items = [itemProvider]
        
    // Create a cloud-sharing service and invoke it to begin sharing.
    if let service = NSSharingService(named: .cloudSharing), 
       service.canPerform(withItems: items) {
        service.perform(withItems: items)
    }
}
```

## Parameters

- `preparationHandler`: The handler the service invokes when it requires the CloudKit share.

## See Also

- [func registerCloudKitShare(CKShare, container: CKContainer)](nsitemprovider/registercloudkitshare(_:container:).md)
  Registers a CloudKit share for the user to modify.
- [func registerCKShare(CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions)](nsitemprovider/registerckshare(_:container:allowedsharingoptions:).md)
  Registers an existing collaboration object on a server.
- [func registerCKShare(container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions, preparationHandler: () async throws -> CKShare)](nsitemprovider/registerckshare(container:allowedsharingoptions:preparationhandler:).md)
  Creates and registers a new collaboration object using a collection of records to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registercloudkitshare(preparationhandler:))*