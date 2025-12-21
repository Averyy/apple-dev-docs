# init(_:access:label:fallback:)

**Framework**: DeviceDiscoveryUI  
**Kind**: init

Creates a `DevicePairingView` which, when pressed, will display a local device advertiser interface.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ listenerProvider: any ListenerProvider, access: DDDevicePairingAccess = .default, @ViewBuilder label: () -> Label, @ViewBuilder fallback: () -> Fallback)
```

#### Discussion

For example:

```None
DevicePairingView(listenerProvider) {
	Text("Starting advertising to local devices")
} fallback: {
	Text("Advertising not available")
}
```

## Parameters

- `listenerProvider`: A ListenerProvider which provides information about the listener to use to advertise.
- `access`: The level of access the app receives for the endpoint selected by the user.
- `label`: A view that describes the action of requesting device advertising if it is supported.
- `fallback`: A view that describes the alternative action when device advertising is not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/devicepairingview/init(_:access:label:fallback:))*