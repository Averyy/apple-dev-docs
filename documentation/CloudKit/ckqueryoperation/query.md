# query

**Framework**: CloudKit  
**Kind**: property

The query for the search.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var query: CKQuery? { get set }
```

#### Discussion

The initial value of this property is the query that you provide to the [`init(query:)`](ckqueryoperation/init(query:).md) method. When the value in the [`cursor`](ckqueryoperation/cursor-swift.property.md) property is `nil`, the operation uses this property’s value to execute a new search and return its results to your completion handler. If [`cursor`](ckqueryoperation/cursor-swift.property.md) isn’t `nil`, the operation uses the cursor instead.

If you intend to specify or change the value of this property, do so before you execute the operation or submit it to a queue.

## See Also

- [var cursor: CKQueryOperation.Cursor?](ckqueryoperation/cursor-swift.property.md)
  The  cursor for continuing the search.
- [CKQueryOperation.Cursor](ckqueryoperation/cursor-swift.class.md)
  An object that marks the stopping point for a query and the starting point for retrieving the remaining results.
- [var zoneID: CKRecordZone.ID?](ckqueryoperation/zoneid.md)
  The ID of the record zone that contains the records to search.
- [var resultsLimit: Int](ckqueryoperation/resultslimit.md)
  The maximum number of records to return at one time.
- [class let maximumResults: Int](ckqueryoperation/maximumresults.md)
  A constant value that represents the maximum number of results CloudKit retrieves.
- [var desiredKeys: [CKRecord.FieldKey]?](ckqueryoperation/desiredkeys-7qrse.md)
  The fields of the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/query)*