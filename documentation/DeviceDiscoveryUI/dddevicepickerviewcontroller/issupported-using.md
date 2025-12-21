# isSupported(_:using:)

**Framework**: DeviceDiscoveryUI  
**Kind**: method

Returns a Boolean value that indicates whether the current device supports device discovery.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency static func isSupported(_ browseDescriptor: NWBrowser.Descriptor, using: NWParameters? = nil) -> Bool
```

## Parameters

- `browseDescriptor`: A descriptor for your application service. To create an application service descriptor, call   and provide a name for the service.

## See Also

- [convenience init?(browseDescriptor: NWBrowser.Descriptor, parameters: NWParameters?)](dddevicepickerviewcontroller/init(browsedescriptor:parameters:).md)
  Creates a view controller that displays the other, available devices on your local network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepickerviewcontroller/issupported(_:using:))*