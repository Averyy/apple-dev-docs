# CKSyncEngineFailedRecordSave

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

A type that describes an unsuccessful attempt to modify an individual record.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface CKSyncEngineFailedRecordSave : NSObject
```

## Topics

### Accessing the record
- [record](./cksyncenginefailedrecordsave/record.md)
  The record that CloudKit is unable to modify.
### Accessing the error
- [error](./cksyncenginefailedrecordsave/error.md)
  An error that describes the reason for the unsuccessful attempt to modify the associated record.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Accessing failed changes
- [failedRecordDeletes](./cksyncenginesentrecordzonechangesevent/failedrecorddeletes.md)
  The unique identifiers of the records CloudKit is unable to delete, and the reasons why.
- [failedRecordSaves](./cksyncenginesentrecordzonechangesevent/failedrecordsaves.md)
  The records that CloudKit is unable to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginefailedrecordsave)*