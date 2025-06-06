# init()

**Framework**: CloudKit  
**Kind**: init

Creates an empty modify record zones operation.

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

You must set at least one of the [`recordZonesToSave`](ckmodifyrecordzonesoperation/recordzonestosave.md) or [`recordZoneIDsToDelete`](ckmodifyrecordzonesoperation/recordzoneidstodelete.md) properties before you execute the operation.

## See Also

- [convenience init(recordZonesToSave: [CKRecordZone]?, recordZoneIDsToDelete: [CKRecordZone.ID]?)](ckmodifyrecordzonesoperation/init(recordzonestosave:recordzoneidstodelete:).md)
  Creates an operation for modifying the specified record zones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/init())*