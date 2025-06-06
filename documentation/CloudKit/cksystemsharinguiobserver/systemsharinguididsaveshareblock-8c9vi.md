# systemSharingUIDidSaveShareBlock

**Framework**: CloudKit  
**Kind**: property

A callback block the system invokes after the success or failure of a system sharing UI save.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
@preconcurrency
var systemSharingUIDidSaveShareBlock: ((CKRecord.ID, Result<CKShare, any Error>) -> Void)? { get set }
```

#### Discussion

Following a successful share save by the system sharing UI in the provided [`CKContainer`](ckcontainer.md), the system invokes this callback with a `nonnull` [`CKRecord.ID`](ckrecord/id.md), a `nonnull` share, and a `nil` error.

If a save failure occurs due to a per-item error like [`CKError.Code.serverRecordChanged`](ckerror/code/serverrecordchanged.md), the system invokes this callback with a `nonnull` `CKRecord.ID`, a `nil` share, and a `nonnull` error.

Each [`CKSystemSharingUIObserver`](cksystemsharinguiobserver.md) instance has a private serial queue. The system uses this queue for all callback block invocations.

## See Also

- [var systemSharingUIDidStopSharingBlock: ((CKRecord.ID, Result<Void, any Error>) -> Void)?](cksystemsharinguiobserver/systemsharinguididstopsharingblock-7nmiw.md)
  A callback block the system invokes after the success or failure of a system sharing UI delete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksystemsharinguiobserver/systemsharinguididsaveshareblock-8c9vi)*