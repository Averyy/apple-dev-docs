# failedRecordSaves

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The records that CloudKit is unable to modify.

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
@property (nonatomic, copy, readonly) NSArray<CKSyncEngineFailedRecordSave *> * failedRecordSaves;
```

## See Also

### Accessing failed changes
- [failedRecordDeletes](./failedrecorddeletes.md)
  The unique identifiers of the records CloudKit is unable to delete, and the reasons why.
- [CKSyncEngineFailedRecordSave](../cksyncenginefailedrecordsave.md)
  A type that describes an unsuccessful attempt to modify an individual record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginesentrecordzonechangesevent/failedrecordsaves)*