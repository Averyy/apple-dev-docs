# init(topology:setupPayload:showing:)

**Framework**: MatterSupport  
**Kind**: init

Create the request.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload? = nil, showing deviceCriteria: MatterAddDeviceRequest.DeviceCriteria = .allDevices)
```

## Parameters

- `topology`: The topology of the home.
- `setupPayload`: The setup payload.

## See Also

- [init(from: any Decoder) throws](matteradddevicerequest/init(from:).md)
  Create the request from a decoder.
- [init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload?, showing: MatterAddDeviceRequest.DeviceCriteria, shouldScanNetworks: Bool)](matteradddevicerequest/init(topology:setuppayload:showing:shouldscannetworks:).md)
  Create the request with an optional network scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/init(topology:setuppayload:showing:))*