# recordZonesToSave

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The record zones to save to the database.

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
var recordZonesToSave: [CKRecordZone]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<CKRecordZone *> * recordZonesToSave;
```

#### Discussion

The initial value of the property is the array that you provide to the [`init(recordZonesToSave:recordZoneIDsToDelete:)`](./init%28recordzonestosave,recordzoneidstodelete%29.md) method. You can modify this array as necessary before you execute the operation. The record zones must all target the same database. You can specify `nil`, or an empty array, for this property.

If you intend to change the value of this property, do so before you execute the operation or submit the operation to a queue.

## See Also

### Configuring the Modify Zones Operation
- [var recordZoneIDsToDelete: [CKRecordZone.ID]?](./recordzoneidstodelete.md)
  The IDs of the record zones to delete permanently from the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/recordzonestosave)*