# registerCKShare(container:allowedSharingOptions:preparationHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates and registers a new collaboration object using a collection of records to share.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func registerCKShare(container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions = CKAllowedSharingOptions.standard, preparationHandler: @escaping @Sendable () async throws -> CKShare)
```

## Discussion

Use this method to share a collection of [`CKRecord`](../../CloudKit/ckrecord.md) objects that don’t have an existing [`CKShare`](../../CloudKit/ckshare.md) assignment. When the system calls the `preparationHandler`, your app creates a new `CKShare` with the appropriate root `CKRecord` or [`CKRecordZone.ID`](../../CloudKit/ckrecordzone/id.md).

After the server successfully saves the share, invoke the [`CKSharePreparationCompletionHandler`](../../CloudKit/cksharepreparationcompletionhandler.md) with either the resulting `CKShare`, or an `NSError` if the save fails.

When the system invokes the share sheet with a `CKShare` that you register with this method, it prompts the user to start sharing.

## Parameters

- `container`: A [`CKContainer`](../../CloudKit/ckcontainer.md) the system uses to coordinate all the interactions between your app and the server.
- `allowedSharingOptions`: The [`CKAllowedSharingOptions`](../../CloudKit/ckallowedsharingoptions.md). The standard option is the default.
- `preparationHandler`: The handler the system calls in your app to create a new [`CKShare`](../../CloudKit/ckshare.md).

## See Also

### Registering CloudKit shares
- [func registerCloudKitShare(CKShare, container: CKContainer)](./registercloudkitshare%28_,container%29.md)
  Registers a CloudKit share for the user to modify.
- [func registerCloudKitShare(preparationHandler: ((CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)](./registercloudkitshare%28preparationhandler%29.md)
  Registers a handler that prepares a new CloudKit share.
- [func registerCKShare(CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions)](./registerckshare%28_,container,allowedsharingoptions%29.md)
  Registers an existing collaboration object on a server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerckshare(container:allowedsharingoptions:preparationhandler:))*