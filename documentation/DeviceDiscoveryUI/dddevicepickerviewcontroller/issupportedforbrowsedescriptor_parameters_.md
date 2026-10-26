# isSupportedForBrowseDescriptor:parameters:

**Framework**: DeviceDiscoveryUI  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the current device supports device discovery.

**Availability**:
- tvOS 16.0+

## Declaration

```objc
+ (BOOL) isSupportedForBrowseDescriptor:(nw_browse_descriptor_t) browseDescriptor parameters:(nw_parameters_t) parameters;
```

## Parameters

- `browseDescriptor`: A descriptor for your application service. To create an application service descriptor, call `NWBrowser.Descriptor.applicationService(name:options:)` and provide a name for the service.
- `parameters`: Parameters for your network connection. Use [`applicationService`](../../Network/nwparameters/applicationservice.md) to create a default set of parameters that create an encrypted connection with the other devices. You can also add `a` [`NWProtocolFramer`](../../Network/nwprotocolframer.md) to provide an application-level messaging protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepickerviewcontroller/issupportedforbrowsedescriptor:parameters:)*