# init(preparationHandler:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes the CloudKit sharing controller with a preparation handler intending to save a new share record.

**Availability**:
- iOS 10.0+ - Deprecated in 17.0
- iPadOS 10.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`init(activityItemsConfiguration:)`](../uiactivityviewcontroller/init%28activityitemsconfiguration%29.md) instead.

## Declaration

```swift
init(preparationHandler: @escaping (UICloudSharingController, @escaping (CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)
```

```objc
- (instancetype) initWithPreparationHandler:(void (^)(UICloudSharingController *controller, void (^preparationCompletionHandler)(CKShare *, CKContainer *, NSError *))) preparationHandler;
```

## Discussion

Use the [`init(preparationHandler:)`](./init%28preparationhandler%29.md) initializer method to create a new [`UICloudSharingController`](../uicloudsharingcontroller.md) instance when the user who owns a [`CKRecord`](../../CloudKit/ckrecord.md) wants to share the record with other people. To determine if the record is shared, check its [`share`](../../CloudKit/ckrecord/share.md) property. If the property value is `nil`, the record is not shared, and this method is the one to use.

> ❗ **Important**:  You must initialize the controller with the correct initializer method. Do not use [`init(preparationHandler:)`](./init%28preparationhandler%29.md) if the [`CKRecord`](../../CloudKit/ckrecord.md) is already shared. Likewise, do not use [`init(share:container:)`](./init%28share,container%29.md) if the [`CKRecord`](../../CloudKit/ckrecord.md) is not shared. Using the wrong initializer leads to errors when saving the record.

The `preparationHandler:` provided to the initializer method is responsible for saving the new [`CKShare`](../../CloudKit/ckshare.md) record. The handler has two parameters:

- A reference to the [`UICloudSharingController`](../uicloudsharingcontroller.md) instance that called the preparation handler
- A reference to a completion block

After you save the new [`CKShare`](../../CloudKit/ckshare.md) record and its root record (the [`CKRecord`](../../CloudKit/ckrecord.md) representing the data to share) in the preparation handler, you call the completion block. Calling the completion block tells the [`UICloudSharingController`](../uicloudsharingcontroller.md) instance to continue with the invitation workflow.

For more information and sample code, see [Inviting participants to a new share](../uicloudsharingcontroller.md#Inviting-participants-to-a-new-share).

## Parameters

- `preparationHandler`: The block invoked by [`UICloudSharingController`](../uicloudsharingcontroller.md) when it is time for your application to save a newly created [`CKShare`](../../CloudKit/ckshare.md) record.

## See Also

### Creating the cloud sharing controller
- [init(share: CKShare, container: CKContainer)](./init%28share,container%29.md)
  Initializes the CloudKit sharing view controller with a CloudKit share record and container to manage participants and restrictions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/init(preparationhandler:))*