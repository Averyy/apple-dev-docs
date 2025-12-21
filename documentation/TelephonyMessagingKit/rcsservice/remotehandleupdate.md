# RCSService.RemoteHandleUpdate

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains information about an update to a remote handle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct RemoteHandleUpdate
```

## Topics

### Accessing handle update properties
- [let cellularServiceID: CellularServiceID](rcsservice/remotehandleupdate/cellularserviceid.md)
  The cellular service ID associated with message.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let handle: RCSHandle](rcsservice/remotehandleupdate/handle.md)
  The old value of the handle that updated.
- [let newHandle: RCSHandle?](rcsservice/remotehandleupdate/newhandle.md)
  The new value for the updated handle.
- [enum RCSHandle](rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [let isBusinessHandle: Bool](rcsservice/remotehandleupdate/isbusinesshandle.md)
  A Boolean value that indicates whether the handle is a business handle.
- [let capabilities: RCSService.RemoteCapabilities?](rcsservice/remotehandleupdate/capabilities.md)
  The updated capabilities.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var remoteHandleUpdates: some AsyncSequence<RCSService.RemoteHandleUpdate, Never>](rcsservice/remotehandleupdates.md)
  An asynchronous sequence of remote handle updates produced by this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotehandleupdate)*