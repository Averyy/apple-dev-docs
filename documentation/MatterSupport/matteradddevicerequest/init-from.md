# init(from:)

**Framework**: MatterSupport  
**Kind**: init

Create the request from a decoder.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder`: The decoder to use.

## See Also

- [init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload?, showing: MatterAddDeviceRequest.DeviceCriteria)](matteradddevicerequest/init(topology:setuppayload:showing:).md)
  Create the request.
- [init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload?, showing: MatterAddDeviceRequest.DeviceCriteria, shouldScanNetworks: Bool)](matteradddevicerequest/init(topology:setuppayload:showing:shouldscannetworks:).md)
  Create the request with an optional network scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/init(from:))*