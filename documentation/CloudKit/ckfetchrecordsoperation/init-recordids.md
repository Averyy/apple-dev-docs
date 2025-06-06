# init(recordIDs:)

**Framework**: CloudKit  
**Kind**: init

Creates a fetch operation for retrieving the records with the specified IDs.

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
convenience init(recordIDs: [CKRecord.ID])
```

#### Discussion

A fetch operation retrieves all of a record’s fields, including any assets that those fields reference. If you want to minimize the amount of data that the operation returns, configure the [`desiredKeys`](ckfetchrecordsoperation/desiredkeys-34l1l.md) property with only the keys that contain the values that you have an interest in.

After initializing the operation, you must associate at least one progress handler with the operation (excluding the completion handler) to process the results.

## Parameters

- `recordIDs`: An array of   objects that represents the records you want to retrieve. If you provide an empty array, you must set the   property before you execute the operation.

## See Also

- [init()](ckfetchrecordsoperation/init.md)
  Creates an empty fetch operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/init(recordids:))*