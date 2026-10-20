# resultsLimit

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of records to return at one time.

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
var resultsLimit: Int { get set }
```

```objc
@property (nonatomic, assign) NSUInteger resultsLimit;
```

#### Discussion

For most queries, leave the value of this property as the default value, which is the [`maximumResults`](./maximumresults.md) constant. When using that value, CloudKit returns as many records as possible while minimizing delays in receiving those records. If you want to process a fixed number of results, change the value of this property accordingly.

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
- [class let maximumResults: Int](./maximumresults.md)
  A constant value that represents the maximum number of results CloudKit retrieves.
- [var desiredKeys: [CKRecord.FieldKey]?](./desiredkeys-7qrse.md)
  The fields of the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/resultslimit)*