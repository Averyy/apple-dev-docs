# init(from:)

**Framework**: MatterSupport  
**Kind**: init  
**Role**: Initializer

Create the request from a decoder.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder`: The decoder to use.

## See Also

### Creating the request
- [init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload?, showing: MatterAddDeviceRequest.DeviceCriteria)](./init%28topology,setuppayload,showing%29.md)
  Create the request.
- [init(topology: MatterAddDeviceRequest.Topology, setupPayload: MTRSetupPayload?, showing: MatterAddDeviceRequest.DeviceCriteria, shouldScanNetworks: Bool)](./init%28topology,setuppayload,showing,shouldscannetworks%29.md)
  Create the request with an optional network scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/init(from:))*