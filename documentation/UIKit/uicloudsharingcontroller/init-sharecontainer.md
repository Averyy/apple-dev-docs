# init(share:container:)

**Framework**: UIKit  
**Kind**: init

Initializes the CloudKit sharing view controller with a CloudKit share record and container to manage participants and restrictions.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(share: CKShare, container: CKContainer)
```

#### Discussion

Use the [`init(share:container:)`](uicloudsharingcontroller/init(share:container:).md) initializer method to create the [`UICloudSharingController`](uicloudsharingcontroller.md) instance when the user who owns the [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) record wants to manage the participants and restrictions associated with the share. (For more information, see [`Adding and removing participants from an existing share`](uicloudsharingcontroller#Adding-and-removing-participants-from-an-existing-share.md).) You also use this initializer method when users are participants who want to remove themselves from a share. (For more information, see [`Viewing participants and leaving a share`](uicloudsharingcontroller#Viewing-participants-and-leaving-a-share.md).)

> ❗ **Important**:  You must initialize the controller with the correct initializer method. Do not use [`init(preparationHandler:)`](uicloudsharingcontroller/init(preparationhandler:).md) if the [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord) is already shared. Likewise, do not use [`init(share:container:)`](uicloudsharingcontroller/init(share:container:).md) if the [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord) is not shared. Using the wrong initializer leads to errors when saving the record.

[`init(share:container:)`](uicloudsharingcontroller/init(share:container:).md) requires a reference to the [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) instance associated with the [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord) instance that represents the shared data. To retrieve the [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) instance, get the [`share`](https://developer.apple.com/documentation/CloudKit/CKRecord/share) property value (a [`CKRecord.Reference`](https://developer.apple.com/documentation/CloudKit/CKRecord/Reference) instance) from the [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord) instance. Then pass the [`recordID`](https://developer.apple.com/documentation/CloudKit/CKRecord/Reference/recordID) from the [`CKRecord.Reference`](https://developer.apple.com/documentation/CloudKit/CKRecord/Reference) instance to the [`fetch(withRecordID:completionHandler:)`](https://developer.apple.com/documentation/CloudKit/CKDatabase/fetch(withRecordID:completionHandler:)) method on a [`CKDatabase`](https://developer.apple.com/documentation/CloudKit/CKDatabase) instance, as shown in the following code.

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

- `share`: An instance of   that was previously saved.
- `container`: An instance of   that contains the record that is shared.

## See Also

- [init(preparationHandler: (UICloudSharingController, (CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)](uicloudsharingcontroller/init(preparationhandler:).md)
  Initializes the CloudKit sharing controller with a preparation handler intending to save a new share record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/init(share:container:))*