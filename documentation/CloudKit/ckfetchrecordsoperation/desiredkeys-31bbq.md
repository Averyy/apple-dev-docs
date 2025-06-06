# desiredKeys

**Framework**: CloudKit  
**Kind**: property

The fields of the records to fetch.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
var desiredKeys: [CKRecord.FieldKey]? { get set }
```

#### Discussion

Use this property to limit the amount of data that CloudKit returns for each record during the fetch operation. When CloudKit returns a record, it only includes fields with names that match one of the keys in this property. The property’s default value is `nil`, which instructs CloudKit to return all of a record’s keys.

If you’re retrieving records of different types, make sure the array includes the fields you want from all of the various record types that the operation can return.

If you intend to specify a value other than `nil`, do so before you execute the operation or add the operation to a queue.

## See Also

- [var recordIDs: [CKRecord.ID]?](ckfetchrecordsoperation/recordids.md)
  The record IDs of the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/desiredkeys-31bbq)*