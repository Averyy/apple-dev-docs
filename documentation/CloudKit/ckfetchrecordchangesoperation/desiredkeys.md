# desiredKeys

**Framework**: CloudKit  
**Kind**: property

The fields to fetch for the requested records.

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
var desiredKeys: [String]? { get set }
```

#### Discussion

Use this property to limit the amount of data that the system retrieves for each record during the fetch operation. This property contains an array of strings, each of which contains the name of a field from the target records. When you retrieve a record, the returned records only include fields with names that match one of the keys in this property. The default value is `nil`, which causes the system to fetch all keys of the record.

Because the records you fetch can be of different types, configure the array to include the merged set of all field names for the requested records and at least one field name from each record type.

If you intend to specify the desired set of keys, set the value of this property before executing the operation or submitting it to a queue.

## See Also

- [var recordZoneID: CKRecordZone.ID?](ckfetchrecordchangesoperation/recordzoneid.md)
  The ID of the record zone with the records you want to fetch.
- [var previousServerChangeToken: CKServerChangeToken?](ckfetchrecordchangesoperation/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var resultsLimit: Int](ckfetchrecordchangesoperation/resultslimit.md)
  The maximum number of changed records to report with this operation object.
- [var moreComing: Bool](ckfetchrecordchangesoperation/morecoming.md)
  A Boolean value that indicates whether more results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/desiredkeys)*