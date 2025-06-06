# init(recordZoneIDs:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for fetching the specified record zones.

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
convenience init(recordZoneIDs zoneIDs: [CKRecordZone.ID])
```

#### Discussion

After creating the operation, assign a value to the [`fetchRecordZonesCompletionBlock`](ckfetchrecordzonesoperation/fetchrecordzonescompletionblock.md) property so you can process the results.

## Parameters

- `zoneIDs`: An array of  objects that represents the zones you want to retrieve. If you provide an empty array, you must set the   property before you execute the operation.

## See Also

- [init()](ckfetchrecordzonesoperation/init.md)
  Creates an empty fetch zones operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/init(recordzoneids:))*