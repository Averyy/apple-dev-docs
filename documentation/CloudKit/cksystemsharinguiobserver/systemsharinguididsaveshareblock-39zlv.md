# systemSharingUIDidSaveShareBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A callback block the system invokes after the success or failure of a share save by the system sharing UI.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
@property (copy, nullable) void (^)(CKRecordID *, CKShare *, NSError *) systemSharingUIDidSaveShareBlock;
```

#### Discussion

Following a successful share save by the system sharing UI in the provided [`CKContainer`](../ckcontainer.md), the system invokes this callback with a `nonnull` [`CKRecord.ID`](../ckrecord/id.md), a `nonnull` share, and a `nil` error.

If a save failure occurs due to a per-item error like [`CKError.Code.serverRecordChanged`](../ckerror/code/serverrecordchanged.md), the system invokes this callback with a `nonnull` [`CKRecord.ID`](../ckrecord/id.md), a `nil` share, and a `nonnull` error.

Each [`CKSystemSharingUIObserver`](../cksystemsharinguiobserver.md) instance has a private serial queue. The system uses this queue for all callback block invocations.

## See Also

### Accessing sharing blocks
- [systemSharingUIDidStopSharingBlock](./systemsharinguididstopsharingblock-4g5bn.md)
  A callback block the system invokes after the success or failure of a share delete by the system sharing UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksystemsharinguiobserver/systemsharinguididsaveshareblock-39zlv)*