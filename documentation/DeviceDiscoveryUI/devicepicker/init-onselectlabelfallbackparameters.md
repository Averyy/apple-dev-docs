# init(_:onSelect:label:fallback:parameters:)

**Framework**: DeviceDiscoveryUI  
**Kind**: init

Creates a view that displays available devices.

**Availability**:
- tvOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ browseDescriptor: NWBrowser.Descriptor, onSelect: @escaping (NWEndpoint) -> Void, @ViewBuilder label: () -> Label, @ViewBuilder fallback: () -> Fallback, parameters: (() -> NWParameters)? = nil)
```

## Parameters

- `browseDescriptor`: A descriptor for your application service. To create an application service descriptor, call `NWBrowser.Descriptor.applicationService(name:options:)` and provide a name for the service.
- `onSelect`: A closure that the framework calls when someone selects a device in the picker view, or cancels the view.
- `label`: A label the network device picker displays.
- `fallback`: A view that the framework displays if the current device doesn’t support device discovery.
- `parameters`: Parameters for your network connection. Use [`applicationService`](https://developer.apple.com/documentation/Network/NWParameters/applicationService) to create a default set of parameters that create an encrypted connection with the other devices. You can also add a [`NWProtocolFramer`](https://developer.apple.com/documentation/Network/NWProtocolFramer) to provide an application-level messaging protocol.

## See Also

- [init<Provider>(Provider, access: DDDevicePairingAccess, onSelect: (Provider.Endpoint) -> Void, label: () -> Label, fallback: () -> Fallback, parameters: (() -> NWParameters)?)](devicepicker/init(_:access:onselect:label:fallback:parameters:).md)
  Creates a view that displays the available devices with the access level, section handler, and other parameters you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/devicepicker/init(_:onselect:label:fallback:parameters:))*