# recordIDs

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The record IDs of the records to fetch.

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
var recordIDs: [CKRecord.ID]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<CKRecordID *> * recordIDs;
```

## Discussion

Use this property to view or change the IDs of the records you want to retrieve. If you use the operation that [`fetchCurrentUserRecordOperation()`](./fetchcurrentuserrecordoperation%28%29.md) returns, CloudKit ignores the contents of this property and sets its value to `nil`.

If you intend to specify a value other than `nil`, do so before you execute the operation or add the operation to a queue. The records you fetch don’t need to be in the same record zone. The record ID for each record provides the zone information that CloudKit needs to fetch the corresponding record.

## See Also

### Configuring a Record Fetch Operation
- [var desiredKeys: [CKRecord.FieldKey]?](./desiredkeys-31bbq.md)
  The fields of the records to fetch.
- [desiredKeys](./desiredkeys-34l1l.md)
  The fields of the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/recordids)*