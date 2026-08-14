# init(_:access:onSelect:label:fallback:parameters:)

**Framework**: DeviceDiscoveryUI  
**Kind**: init

Creates a view that displays the available devices with the access level, section handler, and other parameters you supply.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init<Provider>(_ browserProvider: Provider, access: DDDevicePairingAccess = .default, onSelect: @escaping (Provider.Endpoint) -> Void, @ViewBuilder label: () -> Label, @ViewBuilder fallback: () -> Fallback, parameters: (() -> NWParameters)? = nil) where Provider : BrowserProvider
```

## Parameters

- `browserProvider`: An object that conforms to the [`BrowserProvider`](https://developer.apple.com/documentation/network/browserprovider) protocol and implements a specific network browser type.
- `access`: The [`DDDevicePairingAccess`](dddevicepairingaccess.md) access level. The default is `DDDevicePairingAccess.default`.
- `onSelect`: A closure that the framework calls when someone selects a device in the picker view, or cancels the view.
- `label`: A label the network device picker displays.
- `fallback`: A view that the framework displays if the current device doesn’t support device discovery.
- `parameters`: Parameters for your network connection. Use [`applicationService`](https://developer.apple.com/documentation/network/nwparameters/applicationservice) to create a default set of parameters that create an encrypted connection with the other devices. You can also add a [`NWProtocolFramer`](https://developer.apple.com/documentation/network/nwprotocolframer) to provide an application-level messaging protocol.

## See Also

- [init(NWBrowser.Descriptor, onSelect: (NWEndpoint) -> Void, label: () -> Label, fallback: () -> Fallback, parameters: (() -> NWParameters)?)](devicepicker/init(_:onselect:label:fallback:parameters:).md)
  Creates a view that displays available devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/devicepicker/init(_:access:onselect:label:fallback:parameters:))*