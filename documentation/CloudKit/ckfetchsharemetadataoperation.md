# CKFetchShareMetadataOperation

**Framework**: CloudKit  
**Kind**: class

An operation that fetches metadata for one or more shares.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CKFetchShareMetadataOperation
```

#### Overview

Use this operation to fetch the metadata for one or more shares. A share’s metadata contains the share and details about the user’s participation. Fetch metadata when you want to manually accept participation in a share using [`CKAcceptSharesOperation`](ckacceptsharesoperation.md).

For a shared record hierarchy, the fetched metadata includes the record ID of the share’s root record. Set [`shouldFetchRootRecord`](ckfetchsharemetadataoperation/shouldfetchrootrecord.md) to [`true`](https://developer.apple.com/documentation/swift/true) to fetch the entire root record. You can further customize this behavior using [`rootRecordDesiredKeys`](ckfetchsharemetadataoperation/rootrecorddesiredkeys-3xrex.md) to specify which fields you want to include in your fetch. This functionality isn’t applicable for a shared record zone because, unlike a shared record hierarchy, it doesn’t have a nominated root record.

To run the operation, add it to any container’s operation queue. Returned metadata includes the ID of the container that stores the share. The operation executes its callbacks on a private serial queue.

The operation calls [`perShareMetadataBlock`](ckfetchsharemetadataoperation/persharemetadatablock.md) once for each URL you provide, and CloudKit returns the metadata, or an error if the fetch fails. CloudKit also batches per-URL errors. If the operation completes with errors, it returns a [`partialFailure`](ckerror/partialfailure.md) error. The error stores individual errors in its [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary. Use the [`CKPartialErrorsByItemIDKey`](ckpartialerrorsbyitemidkey.md) key to extract them.

When all of the following conditions are true, CloudKit returns a [`participantMayNeedVerification`](ckerror/participantmayneedverification.md) error:

- There are pending participants that don’t have matched iCloud accounts.
- The current user has an active iCloud account and isn’t an existing participant (pending or otherwise).

On receipt of this error, call [`open(_:options:completionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplication/open(_:options:completionHandler:)) with the share’s URL to allow CloudKit to verify the user.

The following example demonstrates how to create the operation, configure it, and then execute it using the default container’s operation queue:

```swift
func fetchShareMetadata(for shareURLs: [URL],
    completion: @escaping (Result<[URL: CKShare.Metadata], Error>) -> Void) {
        
    var cache = [URL: CKShare.Metadata]()
        
    // Create the fetch operation using the share URLs that
    // the caller provides to the method.
    let operation = CKFetchShareMetadataOperation(shareURLs: shareURLs)
        
    // To reduce network requests, request that CloudKit 
    // includes the root record in the metadata it returns.
    operation.shouldFetchRootRecord = true
        
    // Cache the metadata that CloudKit returns using the
    // share URL. This implementation ignores per-metadata
    // fetch errors and handles any errors in the completion
    // closure instead.
    operation.perShareMetadataBlock = { url, metadata, _ in
        guard let metadata = metadata else { return }
        cache[url] = metadata
    }
        
    // If the operation fails, return the error to the caller.
    // Otherwise, return the array of participants.
    operation.fetchShareMetadataCompletionBlock = { error in
        if let error = error {
            completion(.failure(error))
        } else {
            completion(.success(cache))
        }
    }
        
    // Set an appropriate QoS and add the operation to the
    // container's queue to execute it.
    operation.qualityOfService = .userInitiated
    CKContainer.default().add(operation)
}
```

## Topics

### Creating an Operation
- [init()](ckfetchsharemetadataoperation/init.md)
  Creates an empty fetch share metadata operation.
- [convenience init(shareURLs: [URL])](ckfetchsharemetadataoperation/init(shareurls:).md)
  Creates an operation for fetching the metadata for the specified shares.
### Configuring the Operation
- [var shareURLs: [URL]?](ckfetchsharemetadataoperation/shareurls.md)
  The URLs of the shares to fetch.
- [var shouldFetchRootRecord: Bool](ckfetchsharemetadataoperation/shouldfetchrootrecord.md)
  A Boolean value that indicates whether to retrieve the root record.
### Processing the Operation’s Results
- [var perShareMetadataBlock: ((URL, CKShare.Metadata?, (any Error)?) -> Void)?](ckfetchsharemetadataoperation/persharemetadatablock.md)
  The closure to execute as the operation fetches individual shares.
- [var fetchShareMetadataCompletionBlock: (((any Error)?) -> Void)?](ckfetchsharemetadataoperation/fetchsharemetadatacompletionblock.md)
  The closure to execute when the operation finishes.
### Instance Properties
- [var fetchShareMetadataResultBlock: ((Result<Void, any Error>) -> Void)?](ckfetchsharemetadataoperation/fetchsharemetadataresultblock.md)
- [var perShareMetadataResultBlock: ((URL, Result<CKShare.Metadata, any Error>) -> Void)?](ckfetchsharemetadataoperation/persharemetadataresultblock.md)
- [var rootRecordDesiredKeys: [CKRecord.FieldKey]?](ckfetchsharemetadataoperation/rootrecorddesiredkeys-3xrex.md)
  The fields to return when fetching the root record.

## Relationships

### Inherits From
- [CKOperation](ckoperation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CKShare.Metadata](ckshare/metadata.md)
  An object that describes a shared record’s metadata.
- [class CKAcceptSharesOperation](ckacceptsharesoperation.md)
  An operation that confirms a user’s participation in a share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation)*