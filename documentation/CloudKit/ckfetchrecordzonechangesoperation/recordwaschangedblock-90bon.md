# recordWasChangedBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute with the results of retrieving a record change.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) void (^)(CKRecordID *, CKRecord *, NSError *) recordWasChangedBlock;
```

#### Discussion

The closure returns no value and takes the following parameters:

- The ID of the changed record to retrieve.
- The changed record, or `nil` if CloudKit can’t retrieve the record. If you specify a value for the [`desiredKeys`](../ckfetchrecordzonechangesconfiguration/desiredkeys.md) property, the record contains only the corresponding fields.
- An error that contains information about a problem, or `nil` if CloudKit retrieves the record successfully.

The operation executes this closure once for each record in the record zone with changes since the previous fetch request. Each time the closure executes, it executes serially with respect to the other closures of the operation. If there aren’t any record changes, this closure doesn’t execute.

Set this property before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/recordwaschangedblock-90bon)*