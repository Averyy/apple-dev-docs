# recordZonesToSave

**Framework**: CloudKit  
**Kind**: property

The record zones to save to the database.

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
var recordZonesToSave: [CKRecordZone]? { get set }
```

#### Discussion

The initial value of the property is the array that you provide to the [`initWithRecordZonesToSave:recordZoneIDsToDelete:`](ckmodifyrecordzonesoperation/initwithrecordzonestosave:recordzoneidstodelete:.md) method. You can modify this array as necessary before you execute the operation. The record zones must all target the same database. You can specify `nil`, or an empty array, for this property.

If you intend to change the value of this property, do so before you execute the operation or submit the operation to a queue.

## See Also

- [var recordZoneIDsToDelete: [CKRecordZone.ID]?](ckmodifyrecordzonesoperation/recordzoneidstodelete.md)
  The IDs of the record zones to delete permanently from the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/recordzonestosave)*