# shareManagedObjects:toShare:completion:

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Associates the specified managed objects with a new or existing share record.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
- (void) shareManagedObjects:(NSArray<NSManagedObject *> *) managedObjects toShare:(CKShare *) share completion:(void (^)(NSSet<NSManagedObjectID *> *sharedObjectIDs, CKShare *share, CKContainer *cloudKitContainer, NSError *sharingError)) completion;
```

## Discussion

The `completion` closure returns no value and takes the following parameters:

- The IDs of the shared objects.
- The share record. For more information, see [`CKShare`](../../CloudKit/ckshare.md).
- The CloudKit container of the database that stores the shared record zone. For more information, see [`CKContainer`](../../CloudKit/ckcontainer.md).
- An error object that contains information about a problem, or `nil` if the managed objects share successfully.

When you invoke this method, Core Data performs a deep traversal among the specified managed objects and adds any related objects to the share.

Sharing fails if any of the following conditions apply:

- Any objects in `managedObjects`, or those the traversal finds, belong to an existing share record.
- Any objects in `managedObjects` belong to a persistent store that doesn’t support sharing, such as those you configure with the [`CKDatabase.Scope.public`](../../CloudKit/ckdatabase/scope/public.md) database scope.
- The current device state doesn’t support sharing, such as when there isn’t an active iCloud account.

You can use `completion` directly with the [`init(preparationHandler:)`](../../UIKit/uicloudsharingcontroller/init%28preparationhandler%29.md) method of [`UICloudSharingController`](../../UIKit/uicloudsharingcontroller.md), as the following example shows.

**Swift**:

```swift
func share(_ objects: [NSManagedObjects], in container: NSPersistentCloudKitContainer) {
  // Create an instance of UICloudSharingController.
  let cloudSharingController = UICloudSharingController {
    (controller, completion: @escaping (CKShare?, CKContainer?, Error?) -> Void) in
    
    // Call the container's share method, passing the managed objects to share.
    container.share(objects, to: nil) { _, share, container, error in
      // Invoke the cloud-sharing controller's completion handler,
      // passing the share, container, and error parameters that
      // NSPersistentCloudKitContainer provides.
      completion(share, container, error)
    }
  }

  // Present the cloud-sharing controller to the user.
  present(cloudSharingController, animated: true)
}
```

**Objective-C**:

```objc
- (void)shareObjects:(NSArray *)objects
         inContainer:(NSPersistentCloudKitContainer *)container {
    
    // Create an instance of UICloudSharingController.
    UICloudSharingController *cloudSharingController =
        [[UICloudSharingController alloc]
         initWithPreparationHandler:^(UICloudSharingController * _Nonnull controller,
                                      void (^ _Nonnull preparationCompletionHandler)(
                                       CKShare * _Nullable,
                                       CKContainer * _Nullable,
                                       NSError * _Nullable)) {
        
        // Call the container's share method, passing the managed objects
        // to share.
        [container shareManagedObjects:objects
                               toShare:NULL
                            completion:^(NSSet<NSManagedObjectID *>
                                         * _Nullable sharedObjectIDs,
                                         CKShare * _Nullable share,
                                         CKContainer * _Nullable cloudKitContainer,
                                         NSError * _Nullable sharingError) {
            
            // Invoke the cloud-sharing controller's completion handler,
            // passing the share, container, and error parameters that
            // NSPersistentCloudKitContainer provides.
            preparationCompletionHandler(share, cloudKitContainer, sharingError);
        }];
    }];
    
    // Present the cloud-sharing controller to the user.
    [self presentViewController:cloudSharingController
                       animated:true
                     completion:NULL];
}
```

## Parameters

- `managedObjects`: The managed objects to share.
- `share`: A share record that identifies an existing shared record zone to associate the managed objects with. Use `nil` to create a new shared record zone that contains only the specified managed objects and doesn’t have any participants.
- `completion`: The handler to invoke after Core Data shares the managed objects.

## See Also

### Sharing Objects
- [Accepting Share Invitations in a SwiftUI App](../accepting-share-invitations-in-a-swiftui-app.md)
  Adapt your app to use UIKit’s application and scene delegates so it can process CloudKit share invitations.
- [- acceptShareInvitationsFromMetadata:intoPersistentStore:completion:](./acceptshareinvitationsfrommetadata_intopersistentstore_completion_.md)
  Accepts one or more invitations to participate in sharing using the specified metadata.
- [- fetchParticipantsMatchingLookupInfos:intoPersistentStore:completion:](./fetchparticipantsmatchinglookupinfos_intopersistentstore_completion_.md)
  Fetches all participants that match the specified critieria.
- [- fetchSharesInPersistentStore:error:](./fetchsharesinpersistentstore_error_.md)
  Returns an array that contains all share records in the specified persistent store.
- [- fetchSharesMatchingObjectIDs:error:](./fetchsharesmatchingobjectids_error_.md)
  Returns a dictionary that contains the share records that CloudKit associates with specified managed object IDs.
- [- persistUpdatedShare:inPersistentStore:completion:](./persistupdatedshare_inpersistentstore_completion_.md)
  Saves the share record and schedules it for export to iCloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/sharemanagedobjects:toshare:completion:)*