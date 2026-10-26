# perRecordSaveBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when CloudKit saves a record.

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
@property (nonatomic, copy, nullable) void (^)(CKRecordID *, CKRecord *, NSError *) perRecordSaveBlock;
```

#### Discussion

This property is a closure that returns no value and has the following parameters:

- The ID of the record that CloudKit saves.
- The saved record (as it appears on the server), or `nil` if there’s an error.
- If CloudKit can’t save the record, an error that provides information about the failure; otherwise, `nil`.

The closure executes once for each record in the [`recordsToSave`](./recordstosave.md) property. Each time the closure executes, it executes serially with respect to the other record completion blocks of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/perrecordsaveblock-80dn4)*