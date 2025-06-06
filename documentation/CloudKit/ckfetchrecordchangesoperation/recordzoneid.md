# recordZoneID

**Framework**: CloudKit  
**Kind**: property

The ID of the record zone with the records you want to fetch.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var recordZoneID: CKRecordZone.ID? { get set }
```

#### Discussion

Typically, you set the value of this property when you initialize the operation object. If you intend to change the record zone, update the value before executing the operation or submitting it to a queue.

## See Also

- [var previousServerChangeToken: CKServerChangeToken?](ckfetchrecordchangesoperation/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var desiredKeys: [String]?](ckfetchrecordchangesoperation/desiredkeys.md)
  The fields to fetch for the requested records.
- [var resultsLimit: Int](ckfetchrecordchangesoperation/resultslimit.md)
  The maximum number of changed records to report with this operation object.
- [var moreComing: Bool](ckfetchrecordchangesoperation/morecoming.md)
  A Boolean value that indicates whether more results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/recordzoneid)*