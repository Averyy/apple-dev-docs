# init(_:access:onSelect:label:fallback:parameters:)

**Framework**: DeviceDiscoveryUI  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init<Provider>(_ browserProvider: Provider, access: DDDevicePairingAccess = .default, onSelect: @escaping (Provider.Endpoint) -> Void, @ViewBuilder label: () -> Label, @ViewBuilder fallback: () -> Fallback, parameters: (() -> NWParameters)? = nil) where Provider : BrowserProvider
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/devicepicker/init(_:access:onselect:label:fallback:parameters:))*