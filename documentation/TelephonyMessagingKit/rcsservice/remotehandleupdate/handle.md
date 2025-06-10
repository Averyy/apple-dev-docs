# handle

**Framework**: TelephonyMessagingKit  
**Kind**: property

The old value of the handle that updated.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
let handle: RCSHandle
```

## See Also

- [let cellularServiceID: CellularServiceID](rcsservice/remotehandleupdate/cellularserviceid.md)
  The cellular service ID associated with message.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let newHandle: RCSHandle?](rcsservice/remotehandleupdate/newhandle.md)
  The new value for the updated handle.
- [enum RCSHandle](rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [let isBusinessHandle: Bool](rcsservice/remotehandleupdate/isbusinesshandle.md)
  A Boolean value that indicates whether the handle is a business handle.
- [let capabilities: RCSService.RemoteCapabilities?](rcsservice/remotehandleupdate/capabilities.md)
  The updated capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotehandleupdate/handle)*