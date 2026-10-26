# perRecordZoneDeleteBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when CloudKit deletes a record zone.

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
@property (nonatomic, copy, nullable) void (^)(CKRecordZoneID *, NSError *) perRecordZoneDeleteBlock;
```

#### Discussion

This property is a closure that returns no value and has the following parameters:

- The ID of the record zone that CloudKit deletes.
- If CloudKit can’t delete the record zone, an error that provides information about the failure; otherwise, `nil`.

The closure executes once for each record zone in the [`recordZoneIDsToDelete`](./recordzoneidstodelete.md) property. Each time the closure executes, it executes serially with respect to the other record zone completion blocks of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/perrecordzonedeleteblock-27i5g)*