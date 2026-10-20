# remoteCapabilities(for:)

**Framework**: TelephonyMessagingKit  
**Kind**: method  
**Role**: Instance Method

Requests remote capability discovery for a given handle

**Availability**:
- iOS 26.0+

## Declaration

```swift
final func remoteCapabilities(for request: RCSService.RemoteCapabilitiesRequest) async throws -> RCSService.RemoteCapabilities?
```

#### Return Value

Remote capabilities for requested handle, if available.

## Parameters

- `request`: `RemoteCapabilitiesRequest` containing the request parameters.

## See Also

### Discovering remote capabilities
- [RCSService.RemoteCapabilitiesRequest](./remotecapabilitiesrequest.md)
  A structure representing a request to retrieve the capabilities of a remote handle.
- [RCSService.RemoteCapabilities](./remotecapabilities.md)
  Structure representing the capabilities of a remote handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilities(for:))*