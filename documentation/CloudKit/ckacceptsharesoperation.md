# CKAcceptSharesOperation

**Framework**: CloudKit  
**Kind**: class

An operation that confirms a user’s participation in a share.

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
class CKAcceptSharesOperation
```

#### Overview

Use this operation to accept participation in one or more shares. You create the operation with an array of share metadatas, which CloudKit provides to your app when the user taps or clicks a share’s [`url`](ckshare/url.md). The method CloudKit calls varies by platform and app configuration. For more information, see [`CKShare.Metadata`](ckshare/metadata.md). You can also fetch a share’s metadata using [`CKFetchShareMetadataOperation`](ckfetchsharemetadataoperation.md).

If there are several metadatas, group them by their [`containerIdentifier`](ckshare/metadata/containeridentifier.md) and create an operation for each container. Then add the operation to each container’s operation queue to run it. The operation executes its callbacks on a private serial queue.

The operation calls [`perShareCompletionBlock`](ckacceptsharesoperation/persharecompletionblock.md) once for each metadata you provide. CloudKit returns the metadata and its related share, or an error if it can’t accept the share. CloudKit also batches per-metadata errors. If the operation completes with errors, it returns a [`partialFailure`](ckerror/partialfailure.md) error. The error stores individual errors in its [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo) dictionary. Use the [`CKPartialErrorsByItemIDKey`](ckpartialerrorsbyitemidkey.md) key to extract them.

After CloudKit applies all record changes, the operation calls [`acceptSharesCompletionBlock`](ckacceptsharesoperation/acceptsharescompletionblock.md). When the closure executes, the server may continue processing residual tasks of the operation, such as creating the record zone in the user’s private database.

The following example demonstrates how to accept a share that CloudKit provides to your window scene delegate. It shows how to create the operation, configure it, and execute it in the correct container:

```swift
func windowScene(_ windowScene: UIWindowScene, 
    userDidAcceptCloudKitShareWith cloudKitShareMetadata: CKShare.Metadata) {
    
    // Accept the share. If successful, schedule a fetch of the 
    // share's root record.
    acceptShare(metadata: cloudKitShareMetadata) { [weak self] result in
        switch result {
        case .success(let recordID):
            self?.fetchRootRecordAndNotifyObservers(recordID)
        case .failure(let error):
            // Handle the error...
        }
    }
}
    
func acceptShare(metadata: CKShare.Metadata, 
    completion: @escaping (Result<CKRecord.ID, Error>) -> Void) {
    
    // Create a reference to the share's container so the operation
    // executes in the correct context. 
    let container = CKContainer(identifier: metadata.containerIdentifier)
    
    // Create the operation using the metadata the caller provides.
    let operation = CKAcceptSharesOperation(shareMetadatas: [metadata])
        
    var rootRecordID: CKRecord.ID!
    // If CloudKit accepts the share, cache the root record's ID. 
    // The completion closure handles any errors.
    operation.perShareCompletionBlock = { metadata, share, error in
        if let _ = share, error == nil {
            rootRecordID = hierarchicalRootRecordID 
        }
    }

    // If the operation fails, return the error to the caller.
    // Otherwise, return the record ID of the share's root record.
    operation.acceptSharesCompletionBlock = { error in
        if let error = error {
            completion(.failure(error))
        } else {
            completion(.success(rootRecordID))
        }
    }

    // Set an appropriate QoS and add the operation to the
    // container's queue to execute it.
    operation.qualityOfService = .utility
    container.add(operation)
}
```

## Topics

### Creating a Share Accept Operation
- [init()](ckacceptsharesoperation/init.md)
  Creates an operation for accepting shares.
- [convenience init(shareMetadatas: [CKShare.Metadata])](ckacceptsharesoperation/init(sharemetadatas:).md)
  Creates an operation for accepting the specified shares.
### Processing the Share Accept Results
- [var shareMetadatas: [CKShare.Metadata]?](ckacceptsharesoperation/sharemetadatas.md)
  The share metadatas to process.
- [var perShareCompletionBlock: ((CKShare.Metadata, CKShare?, (any Error)?) -> Void)?](ckacceptsharesoperation/persharecompletionblock.md)
  The block to execute as CloudKit processes individual shares.
- [var acceptSharesCompletionBlock: (((any Error)?) -> Void)?](ckacceptsharesoperation/acceptsharescompletionblock.md)
  The closure to execute when the operation finishes.
### Instance Properties
- [var acceptSharesResultBlock: ((Result<Void, any Error>) -> Void)?](ckacceptsharesoperation/acceptsharesresultblock.md)
- [var perShareResultBlock: ((CKShare.Metadata, Result<CKShare, any Error>) -> Void)?](ckacceptsharesoperation/pershareresultblock.md)

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

## See Also

- [class CKFetchShareMetadataOperation](ckfetchsharemetadataoperation.md)
  An operation that fetches metadata for one or more shares.
- [CKShare.Metadata](ckshare/metadata.md)
  An object that describes a shared record’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation)*