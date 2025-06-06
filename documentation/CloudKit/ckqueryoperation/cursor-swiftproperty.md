# cursor

**Framework**: CloudKit  
**Kind**: property

The  cursor for continuing the search.

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
var cursor: CKQueryOperation.Cursor? { get set }
```

#### Discussion

The initial value of this property is the cursor that you provide to the [`init(cursor:)`](ckqueryoperation/init(cursor:).md) method. When you use a cursor, the operation ignores the contents of the [`query`](ckqueryoperation/query.md) property. This property’s value is an opaque value that CloudKit provides. For more information, see the [`queryCompletionBlock`](ckqueryoperation/querycompletionblock.md) property.

If you intend to specify or change the value in this property, do so before you execute the operation or submit it to a queue.

## See Also

- [var query: CKQuery?](ckqueryoperation/query.md)
  The query for the search.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/cursor-swift.property)*