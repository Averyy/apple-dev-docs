# cachePolicy

**Framework**: TelephonyMessagingKit  
**Kind**: property

Cache policy to use for request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var cachePolicy: RCSService.RemoteCapabilitiesRequest.CachePolicy
```

#### Discussion

Always use cache first and then if it fails, prefer cacheOrRemote, remote is something that should be avoided (reserved for cases where the client feels that the cache is invalid, or incorrect)

## See Also

- [var cellularServiceID: CellularServiceID](rcsservice/remotecapabilitiesrequest/cellularserviceid.md)
  Service identifier to use for this request.
- [var handle: RCSHandle](rcsservice/remotecapabilitiesrequest/handle.md)
  The RCS handle, typically a phone number.
- [RCSService.RemoteCapabilitiesRequest.CachePolicy](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum.md)
  Enumeration representing the cache policy to use in requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilitiesrequest/cachepolicy-swift.property)*