# recordZoneFetchResultBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when a record zone’s fetch finishes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
var recordZoneFetchResultBlock: ((CKRecordZone.ID, Result<(serverChangeToken: CKServerChangeToken, clientChangeTokenData: Data?, moreComing: Bool), any Error>) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameters:

- **`recordZoneID`**: The record zone’s ID.
- **`fetchChangesResult`**: A [`Result`](https://developer.apple.com/documentation/swift/result) that contains either: - A successful `Result` of - The change token to store and use in subsequent instances of [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md).
- The more recent client change token from the device. If the change token isn’t the more recent change token you provided, the server might not have received the associated changes.
- A Boolean that indicates whether this is the final record zone change. If [`fetchAllChanges`](ckfetchrecordzonechangesoperation/fetchallchanges.md) is [`false`](https://developer.apple.com/documentation/swift/false), it’s the app’s responsibility to create additional instances of [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md) to fetch further changes.
- An error object that contains information about a problem encountered retrieving the record zone changes.

The app is responsible for saving the change token at the end of the operation and providing it to future uses of [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md). Each time the closure executes, it executes serially with respect to the other closures of the operation.

Set this property before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/recordzonefetchresultblock)*