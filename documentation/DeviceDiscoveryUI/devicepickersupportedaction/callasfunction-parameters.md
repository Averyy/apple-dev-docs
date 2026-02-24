# callAsFunction(_:parameters:)

**Framework**: DeviceDiscoveryUI  
**Kind**: method

Returns a Boolean value that indicates whether the current device supports device discovery.

**Availability**:
- tvOS 16.0+

## Declaration

```swift
func callAsFunction(_ browseDescriptor: NWBrowser.Descriptor, parameters: (() -> NWParameters)? = nil) -> Bool
```

## Parameters

- `browseDescriptor`: A descriptor for your application service. To create an application service descriptor, call `NWBrowser.Descriptor.applicationService(name:options:)` and provide a name for the service.
- `parameters`: Parameters for your network connection. Use [`applicationService`](https://developer.apple.com/documentation/Network/NWParameters/applicationService) to create a default set of parameters that create an encrypted connection with the other devices. You can also add `a` [`NWProtocolFramer`](https://developer.apple.com/documentation/Network/NWProtocolFramer) to provide an application-level messaging protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/devicepickersupportedaction/callasfunction(_:parameters:))*