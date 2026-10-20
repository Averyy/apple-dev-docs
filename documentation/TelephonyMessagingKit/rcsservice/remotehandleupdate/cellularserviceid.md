# cellularServiceID

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The cellular service ID associated with message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
let cellularServiceID: CellularServiceID
```

## See Also

### Accessing handle update properties
- [struct CellularServiceID](../../cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let handle: RCSHandle](./handle.md)
  The old value of the handle that updated.
- [let newHandle: RCSHandle?](./newhandle.md)
  The new value for the updated handle.
- [enum RCSHandle](../../rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [let isBusinessHandle: Bool](./isbusinesshandle.md)
  A Boolean value that indicates whether the handle is a business handle.
- [let capabilities: RCSService.RemoteCapabilities?](./capabilities.md)
  The updated capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotehandleupdate/cellularserviceid)*