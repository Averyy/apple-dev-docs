# init()

**Framework**: CloudKit  
**Kind**: init

Creates an empty fetch zones operation.

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
init()
```

#### Discussion

You must set the [`recordZoneIDs`](ckfetchrecordzonesoperation/recordzoneids.md) property before you execute the operation.

After creating the operation, assign a value to the [`fetchRecordZonesCompletionBlock`](ckfetchrecordzonesoperation/fetchrecordzonescompletionblock.md) property so you can process the results.

## See Also

- [convenience init(recordZoneIDs: [CKRecordZone.ID])](ckfetchrecordzonesoperation/init(recordzoneids:).md)
  Creates an operation for fetching the specified record zones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/init())*