# maximumResults

**Framework**: CloudKit  
**Kind**: property

A constant value that represents the maximum number of results CloudKit retrieves.

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
class let maximumResults: Int
```

#### Discussion

The value of this constant doesn’t correspond to the actual number of records. CloudKit dynamically determines the actual number according to various conditions at runtime.

This constant is the [`resultsLimit`](ckqueryoperation/resultslimit.md) property’s default value.

## See Also

- [var query: CKQuery?](ckqueryoperation/query.md)
  The query for the search.
- [var cursor: CKQueryOperation.Cursor?](ckqueryoperation/cursor-swift.property.md)
  The  cursor for continuing the search.
- [CKQueryOperation.Cursor](ckqueryoperation/cursor-swift.class.md)
  An object that marks the stopping point for a query and the starting point for retrieving the remaining results.
- [var zoneID: CKRecordZone.ID?](ckqueryoperation/zoneid.md)
  The ID of the record zone that contains the records to search.
- [var resultsLimit: Int](ckqueryoperation/resultslimit.md)
  The maximum number of records to return at one time.
- [var desiredKeys: [CKRecord.FieldKey]?](ckqueryoperation/desiredkeys-7qrse.md)
  The fields of the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/maximumresults)*