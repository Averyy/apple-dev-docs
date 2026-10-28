# perRecordZoneSaveBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when CloudKit saves a record zone.

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
@property (nonatomic, copy, nullable) void (^)(CKRecordZoneID *, CKRecordZone *, NSError *) perRecordZoneSaveBlock;
```

## Discussion

This property is a closure that returns no value and has the following parameters:

- The ID of the record zone that CloudKit saves.
- The record zone that CloudKit saves, or `nil` if CloudKit can’t save the record zone.
- If CloudKit can’t save the record zone, an error that provides information about the failure; otherwise, `nil`.

The closure executes once for each record zone in the [`recordZonesToSave`](./recordzonestosave.md) property. Each time the closure executes, it executes serially with respect to the other record zone completion blocks of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/perrecordzonesaveblock-3txst)*