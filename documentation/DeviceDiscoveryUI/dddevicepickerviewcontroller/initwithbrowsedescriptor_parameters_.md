# initWithBrowseDescriptor:parameters:

**Framework**: DeviceDiscoveryUI  
**Kind**: method  
**Role**: Instance Method

Creates a view controller that displays the other, available devices on your local network.

**Availability**:
- tvOS 16.0+

## Declaration

```objc
- (instancetype) initWithBrowseDescriptor:(nw_browse_descriptor_t) browseDescriptor parameters:(nw_parameters_t) parameters;
```

## Parameters

- `browseDescriptor`: A descriptor for your application service. To create an application service descriptor, call `NWBrowser.Descriptor.applicationService(name:options:)` and provide a name for the service.
- `parameters`: Parameters for your network connection. Use [`applicationService`](../../Network/nwparameters/applicationservice.md) to create a default set of parameters that create an encrypted connection with the other devices. You can also add `a` [`NWProtocolFramer`](../../Network/nwprotocolframer.md) to provide an application-level messaging protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepickerviewcontroller/initwithbrowsedescriptor:parameters:)*