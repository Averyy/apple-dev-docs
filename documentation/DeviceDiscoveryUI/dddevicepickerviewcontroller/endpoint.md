# endpoint

**Framework**: DeviceDiscoveryUI  
**Kind**: property

A network connection endpoint for the device selected by the user.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency var endpoint: NWEndpoint { get async throws }
```

#### Discussion

Your app can asynchronously read from this property. The system populates this property when the user selects a device from the endpoint picker. If the user cancels the picker, the system throws an error.

```swift
let endpoint: NWEndpoint
do {
    endpoint = try await myEndpointPickerHandler.endpoint
} catch {
    // The user canceled the endpoint picker view.
    return
}

// Use the endpoint here.
myDeviceConnectionManager.connectTo(endpoint: endpoint)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepickerviewcontroller/endpoint)*