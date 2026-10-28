# init()

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates an empty modify records operation.

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

## Discussion

You must set at least one of the [`recordsToSave`](./recordstosave.md) or [`recordIDsToDelete`](./recordidstodelete.md) properties before you execute the operation.

## See Also

### Creating a Modify Record Operation
- [convenience init(recordsToSave: [CKRecord]?, recordIDsToDelete: [CKRecord.ID]?)](./init%28recordstosave,recordidstodelete%29.md)
  Creates an operation for modifying the specified records.
- [- initWithRecordsToSave:recordIDsToDelete:](./initwithrecordstosave_recordidstodelete_.md)
  Creates an operation for modifying the specified records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/init())*