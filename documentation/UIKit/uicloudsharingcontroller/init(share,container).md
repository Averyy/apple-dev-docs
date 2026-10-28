# init(share:container:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes the CloudKit sharing view controller with a CloudKit share record and container to manage participants and restrictions.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(share: CKShare, container: CKContainer)
```

```objc
- (instancetype) initWithShare:(CKShare *) share container:(CKContainer *) container;
```

## Discussion

Use the [`init(share:container:)`](./init%28share,container%29.md) initializer method to create the [`UICloudSharingController`](../uicloudsharingcontroller.md) instance when the user who owns the [`CKShare`](../../CloudKit/ckshare.md) record wants to manage the participants and restrictions associated with the share. (For more information, see [Adding and removing participants from an existing share](../uicloudsharingcontroller.md#Adding-and-removing-participants-from-an-existing-share).) You also use this initializer method when users are participants who want to remove themselves from a share. (For more information, see [Viewing participants and leaving a share](../uicloudsharingcontroller.md#Viewing-participants-and-leaving-a-share).)

> ❗ **Important**:  You must initialize the controller with the correct initializer method. Do not use [`init(preparationHandler:)`](./init%28preparationhandler%29.md) if the [`CKRecord`](../../CloudKit/ckrecord.md) is already shared. Likewise, do not use [`init(share:container:)`](./init%28share,container%29.md) if the [`CKRecord`](../../CloudKit/ckrecord.md) is not shared. Using the wrong initializer leads to errors when saving the record.

[`init(share:container:)`](./init%28share,container%29.md) requires a reference to the [`CKShare`](../../CloudKit/ckshare.md) instance associated with the [`CKRecord`](../../CloudKit/ckrecord.md) instance that represents the shared data. To retrieve the [`CKShare`](../../CloudKit/ckshare.md) instance, get the [`share`](../../CloudKit/ckrecord/share.md) property value (a [`CKRecord.Reference`](../../CloudKit/ckrecord/reference.md) instance) from the [`CKRecord`](../../CloudKit/ckrecord.md) instance. Then pass the [`recordID`](../../CloudKit/ckrecord/reference/recordid.md) from the [`CKRecord.Reference`](../../CloudKit/ckrecord/reference.md) instance to the [`fetch(withRecordID:completionHandler:)`](../../CloudKit/ckdatabase/fetch%28withrecordid,completionhandler%29.md) method on a [`CKDatabase`](../../CloudKit/ckdatabase.md) instance, as shown in the following code.

```objc
CKRecord *record = [self record];
CKReference *shareReference = [record share];
if (shareReference == nil) {
  return;
}
CKContainer *container = [CKContainer defaultContainer];
[[container privateCloudDatabase] fetchRecordWithID:[shareReference recordID] completionHandler:^(CKRecord * _Nullable record, NSError * _Nullable error) {
  
  if (record == nil) {
    NSLog(@"%@", [error localizedDescription]);
  } else if ([record isKindOfClass:[CKShare class]]) {
    CKShare *shareRecord = (CKShare *)record;
    NSLog(@"%@", [shareRecord URL]);
  }
  
}];
```

## Parameters

- `share`: An instance of [`CKShare`](../../CloudKit/ckshare.md) that was previously saved.
- `container`: An instance of [`CKContainer`](../../CloudKit/ckcontainer.md) that contains the record that is shared.

## See Also

### Creating the cloud sharing controller
- [init(preparationHandler: (UICloudSharingController, (CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)](./init%28preparationhandler%29.md)
  Initializes the CloudKit sharing controller with a preparation handler intending to save a new share record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/init(share:container:))*