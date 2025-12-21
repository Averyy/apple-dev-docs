# init(_:onSelect:label:fallback:parameters:)

**Framework**: DeviceDiscoveryUI  
**Kind**: init

Creates a view that displays the other, available devices on your local network.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ browseDescriptor: NWBrowser.Descriptor, onSelect: @escaping (NWEndpoint) -> Void, @ViewBuilder label: () -> Label, @ViewBuilder fallback: () -> Fallback, parameters: (() -> NWParameters)? = nil)
```

## Parameters

- `browseDescriptor`: A descriptor for your application service. To create an application service descriptor, call   and provide a name for the service.
- `onSelect`: A closure that the system calls when the user selects a device in the picker view, or cancels the view.
- `label`: A label displayed by the network device picker.
- `fallback`: A view that the system displays if the current device doesn’t support device discovery.
- `parameters`: Parameters for your network connection. Use   to create a default set of parameters that create an encrypted connection with the other devices. You can also add     to provide an application-level messaging protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/devicepicker/init(_:onselect:label:fallback:parameters:))*