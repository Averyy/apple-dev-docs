# registerCKShare(container:allowedSharingOptions:preparationHandler:)

**Framework**: Foundation  
**Kind**: method

Creates and registers a new collaboration object using a collection of records to share.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func registerCKShare(container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions = CKAllowedSharingOptions.standard, preparationHandler: @escaping () async throws -> CKShare)
```

#### Discussion

Use this method to share a collection of [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord) objects that don’t have an existing [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) assignment. When the system calls the `preparationHandler`, your app creates a new `CKShare` with the appropriate root `CKRecord` or [`CKRecordZone.ID`](https://developer.apple.com/documentation/CloudKit/CKRecordZone/ID).

After the server successfully saves the share, invoke the [`CKSharePreparationCompletionHandler`](https://developer.apple.com/documentation/CloudKit/CKSharePreparationCompletionHandler) with either the resulting `CKShare`, or an `NSError` if the save fails.

When the system invokes the share sheet with a `CKShare` that you register with this method, it prompts the user to start sharing.

## Parameters

- `container`: A   the system uses to coordinate all the interactions between your app and the server.
- `allowedSharingOptions`: The  . The standard option is the default.
- `preparationHandler`: The handler the system calls in your app to create a new  .

## See Also

- [func registerCloudKitShare(CKShare, container: CKContainer)](nsitemprovider/registercloudkitshare(_:container:).md)
  Registers a CloudKit share for the user to modify.
- [func registerCloudKitShare(preparationHandler: ((CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)](nsitemprovider/registercloudkitshare(preparationhandler:).md)
  Registers a handler that prepares a new CloudKit share.
- [func registerCKShare(CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions)](nsitemprovider/registerckshare(_:container:allowedsharingoptions:).md)
  Registers an existing collaboration object on a server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerckshare(container:allowedsharingoptions:preparationhandler:))*