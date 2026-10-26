# init()

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates an empty modify record zones operation.

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
init()
```

```objc
- (instancetype) init;
```

#### Discussion

You must set at least one of the [`recordZonesToSave`](./recordzonestosave.md) or [`recordZoneIDsToDelete`](./recordzoneidstodelete.md) properties before you execute the operation.

## See Also

### Creating a Modify Zones Operation
- [convenience init(recordZonesToSave: [CKRecordZone]?, recordZoneIDsToDelete: [CKRecordZone.ID]?)](./init%28recordzonestosave,recordzoneidstodelete%29.md)
  Creates an operation for modifying the specified record zones.
- [- initWithRecordZonesToSave:recordZoneIDsToDelete:](./initwithrecordzonestosave_recordzoneidstodelete_.md)
  Creates an operation for modifying the specified record zones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/init())*