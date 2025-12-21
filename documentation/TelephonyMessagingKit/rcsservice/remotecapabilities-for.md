# remoteCapabilities(for:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Requests remote capability discovery for a given handle

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func remoteCapabilities(for request: RCSService.RemoteCapabilitiesRequest) async throws -> RCSService.RemoteCapabilities?
```

#### Return Value

Remote capabilities for requested handle, if available.

## Parameters

- `request`:   containing the request parameters.

## See Also

- [RCSService.RemoteCapabilitiesRequest](rcsservice/remotecapabilitiesrequest.md)
  A structure representing a request to retrieve the capabilities of a remote handle.
- [RCSService.RemoteCapabilities](rcsservice/remotecapabilities.md)
  Structure representing the capabilities of a remote handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilities(for:))*