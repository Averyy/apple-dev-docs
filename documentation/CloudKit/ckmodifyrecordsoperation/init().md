# init()

**Framework**: CloudKit  
**Kind**: init

Creates an empty modify records operation.

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

You must set at least one of the [`recordsToSave`](ckmodifyrecordsoperation/recordstosave.md) or [`recordIDsToDelete`](ckmodifyrecordsoperation/recordidstodelete.md) properties before you execute the operation.

## See Also

- [convenience init(recordsToSave: [CKRecord]?, recordIDsToDelete: [CKRecord.ID]?)](ckmodifyrecordsoperation/init(recordstosave:recordidstodelete:).md)
  Creates an operation for modifying the specified records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/init())*