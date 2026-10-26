# systemSharingUIDidStopSharingBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A callback block the system invokes after the success or failure of a share delete by the system sharing UI.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
@property (copy, nullable) void (^)(CKRecordID *, NSError *) systemSharingUIDidStopSharingBlock;
```

#### Discussion

The system invokes this block on the success or failure of a [`CKShare`](../ckshare.md) delete when the user decides to stop sharing through the system sharing UI.

Each [`CKSystemSharingUIObserver`](../cksystemsharinguiobserver.md) instance has a private serial queue. The system uses this queue for all callback block invocations.

## See Also

### Accessing sharing blocks
- [systemSharingUIDidSaveShareBlock](./systemsharinguididsaveshareblock-39zlv.md)
  A callback block the system invokes after the success or failure of a share save by the system sharing UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksystemsharinguiobserver/systemsharinguididstopsharingblock-4g5bn)*