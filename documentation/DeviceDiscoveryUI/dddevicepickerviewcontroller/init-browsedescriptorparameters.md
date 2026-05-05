# init(browseDescriptor:parameters:)

**Framework**: DeviceDiscoveryUI  
**Kind**: init

Creates a view controller that displays the available devices on your local network.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init?(browseDescriptor: NWBrowser.Descriptor, parameters: NWParameters? = nil)
```

## Parameters

- `browseDescriptor`: A descriptor for your application service. To create an application service descriptor, call `NWBrowser.Descriptor.applicationService(name:options:)` and provide a name for the service.
- `parameters`: Parameters for your network connection. Use [`applicationService`](https://developer.apple.com/documentation/Network/NWParameters/applicationService) to create a default set of parameters that create an encrypted connection with the other devices. You can also add `a` [`NWProtocolFramer`](https://developer.apple.com/documentation/Network/NWProtocolFramer) to provide an application-level messaging protocol.

## See Also

- [convenience init?(browseDescriptor: NWBrowser.Descriptor, parameters: NWParameters?, access: DDDevicePairingAccess)](dddevicepickerviewcontroller/init(browsedescriptor:parameters:access:).md)
  Creates a view controller with the parameters and access level you specify that displays the available devices on network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepickerviewcontroller/init(browsedescriptor:parameters:))*