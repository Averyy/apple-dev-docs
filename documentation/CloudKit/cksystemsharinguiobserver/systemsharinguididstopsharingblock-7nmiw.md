# systemSharingUIDidStopSharingBlock

**Framework**: CloudKit  
**Kind**: property

A callback block the system invokes after the success or failure of a system sharing UI delete.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
@preconcurrency
var systemSharingUIDidStopSharingBlock: ((CKRecord.ID, Result<Void, any Error>) -> Void)? { get set }
```

#### Discussion

The system invokes this block on the success or failure of a [`CKShare`](ckshare.md) delete when the user decides to stop sharing through the system sharing UI.

Each [`CKSystemSharingUIObserver`](cksystemsharinguiobserver.md) instance has a private serial queue. The system uses this queue for all callback block invocations.

## See Also

- [var systemSharingUIDidSaveShareBlock: ((CKRecord.ID, Result<CKShare, any Error>) -> Void)?](cksystemsharinguiobserver/systemsharinguididsaveshareblock-8c9vi.md)
  A callback block the system invokes after the success or failure of a system sharing UI save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksystemsharinguiobserver/systemsharinguididstopsharingblock-7nmiw)*