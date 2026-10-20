# init(topology:setupPayload:showing:shouldScanNetworks:)

**Framework**: MatterSupport  
**Kind**: init  
**Role**: Initializer

Create the request with an optional network scan.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 14.0+
- visionOS

## Declaration

```swift
init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload? = nil, showing deviceCriteria: MatterAddDeviceRequest.DeviceCriteria = .allDevices, shouldScanNetworks: Bool = true)
```

## Parameters

- `topology`: The topology of the home.
- `setupPayload`: The setup payload.
- `shouldScanNetworks`: A flag that determines whether to request a network scan.

## See Also

### Creating the request
- [init(from: any Decoder) throws](./init%28from%29.md)
  Create the request from a decoder.
- [init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload?, showing: MatterAddDeviceRequest.DeviceCriteria)](./init%28topology,setuppayload,showing%29.md)
  Create the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/init(topology:setuppayload:showing:shouldscannetworks:))*