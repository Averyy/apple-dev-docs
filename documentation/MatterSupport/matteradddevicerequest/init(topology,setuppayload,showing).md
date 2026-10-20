# init(topology:setupPayload:showing:)

**Framework**: MatterSupport  
**Kind**: init  
**Role**: Initializer

Create the request.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload? = nil, showing deviceCriteria: MatterAddDeviceRequest.DeviceCriteria = .allDevices)
```

## Parameters

- `topology`: The topology of the home.
- `setupPayload`: The setup payload.

## See Also

### Creating the request
- [init(from: any Decoder) throws](./init%28from%29.md)
  Create the request from a decoder.
- [init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload?, showing: MatterAddDeviceRequest.DeviceCriteria, shouldScanNetworks: Bool)](./init%28topology,setuppayload,showing,shouldscannetworks%29.md)
  Create the request with an optional network scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/init(topology:setuppayload:showing:))*