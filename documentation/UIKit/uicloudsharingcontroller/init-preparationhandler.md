# init(preparationHandler:)

**Framework**: UIKit  
**Kind**: init

Initializes the CloudKit sharing controller with a preparation handler intending to save a new share record.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(preparationHandler: @escaping (UICloudSharingController, @escaping (CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)
```

#### Discussion

Use the [`init(preparationHandler:)`](uicloudsharingcontroller/init(preparationhandler:).md) initializer method to create a new [`UICloudSharingController`](uicloudsharingcontroller.md) instance when the user who owns a [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord) wants to share the record with other people. To determine if the record is shared, check its [`share`](https://developer.apple.com/documentation/CloudKit/CKRecord/share) property. If the property value is `nil`, the record is not shared, and this method is the one to use.

> ❗ **Important**:  You must initialize the controller with the correct initializer method. Do not use [`init(preparationHandler:)`](uicloudsharingcontroller/init(preparationhandler:).md) if the [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord) is already shared. Likewise, do not use [`init(share:container:)`](uicloudsharingcontroller/init(share:container:).md) if the [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord) is not shared. Using the wrong initializer leads to errors when saving the record.

The `preparationHandler:` provided to the initializer method is responsible for saving the new [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) record. The handler has two parameters:

- A reference to the [`UICloudSharingController`](uicloudsharingcontroller.md) instance that called the preparation handler
- A reference to a completion block

After you save the new [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) record and its root record (the [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord) representing the data to share) in the preparation handler, you call the completion block. Calling the completion block tells the [`UICloudSharingController`](uicloudsharingcontroller.md) instance to continue with the invitation workflow.

For more information and sample code, see [`Inviting participants to a new share`](uicloudsharingcontroller#Inviting-participants-to-a-new-share.md).

## Parameters

- `preparationHandler`: The block invoked by   when it is time for your application to save a newly created   record.

## See Also

- [init(share: CKShare, container: CKContainer)](uicloudsharingcontroller/init(share:container:).md)
  Initializes the CloudKit sharing view controller with a CloudKit share record and container to manage participants and restrictions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/init(preparationhandler:))*