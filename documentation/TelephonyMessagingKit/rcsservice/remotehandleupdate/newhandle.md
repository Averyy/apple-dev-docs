# newHandle

**Framework**: TelephonyMessagingKit  
**Kind**: property

The new value for the updated handle.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
let newHandle: RCSHandle?
```

#### Discussion

This value is `nil` if the handle didn’t change.

## See Also

- [let cellularServiceID: CellularServiceID](rcsservice/remotehandleupdate/cellularserviceid.md)
  The cellular service ID associated with message.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let handle: RCSHandle](rcsservice/remotehandleupdate/handle.md)
  The old value of the handle that updated.
- [enum RCSHandle](rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [let isBusinessHandle: Bool](rcsservice/remotehandleupdate/isbusinesshandle.md)
  A Boolean value that indicates whether the handle is a business handle.
- [let capabilities: RCSService.RemoteCapabilities?](rcsservice/remotehandleupdate/capabilities.md)
  The updated capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotehandleupdate/newhandle)*