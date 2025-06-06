# recordZoneIDs

**Framework**: CloudKit  
**Kind**: property

The IDs of the record zones to retrieve.

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
var recordZoneIDs: [CKRecordZone.ID]? { get set }
```

#### Discussion

Use this property to view or change the IDs of the record zones you want to retrieve. If you intend to change the value of this property, do so before you execute the operation or submit the operation to a queue.

If you use the operation that [`fetchAllRecordZonesOperation()`](ckfetchrecordzonesoperation/fetchallrecordzonesoperation().md) returns, CloudKit ignores the contents of this property and sets its value to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/recordzoneids)*