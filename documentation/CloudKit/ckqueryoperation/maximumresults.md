# maximumResults

**Framework**: CloudKit  
**Kind**: property  
**Role**: Type Property

A constant value that represents the maximum number of results CloudKit retrieves.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class let maximumResults: Int
```

```c
extern const NSUInteger CKQueryOperationMaximumResults;
```

#### Discussion

The value of this constant doesn’t correspond to the actual number of records. CloudKit dynamically determines the actual number according to various conditions at runtime.

This constant is the [`resultsLimit`](./resultslimit.md) property’s default value.

## See Also

### Configuring the Query Operation
- [var query: CKQuery?](./query.md)
  The query for the search.
- [var cursor: CKQueryOperation.Cursor?](./cursor-swift.property.md)
  The cursor for continuing the search.
- [CKQueryOperation.Cursor](./cursor-swift.class.md)
  An object that marks the stopping point for a query and the starting point for retrieving the remaining results.
- [var zoneID: CKRecordZone.ID?](./zoneid.md)
  The ID of the record zone that contains the records to search.
- [var resultsLimit: Int](./resultslimit.md)
  The maximum number of records to return at one time.
- [var desiredKeys: [CKRecord.FieldKey]?](./desiredkeys-7qrse.md)
  The fields of the records to fetch.
- [desiredKeys](./desiredkeys-4a6vy.md)
  The fields of the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/maximumresults)*