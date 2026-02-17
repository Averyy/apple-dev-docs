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

The app is responsible for saving the change token at the end of the operation and providing it to future uses of [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md). Each time the closure executes, it executes serially with respect to the other closures of the operation.

Set this property before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/recordzonefetchresultblock)*