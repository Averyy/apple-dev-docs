# init(browseDescriptor:parameters:)

**Framework**: DeviceDiscoveryUI  
**Kind**: init

Creates a view controller that displays the other, available devices on your local network.

**Availability**:
- tvOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init?(browseDescriptor: NWBrowser.Descriptor, parameters: NWParameters? = nil)
```

## Parameters

- `browseDescriptor`: A descriptor for your application service. To create an application service descriptor, call   and provide a name for the service.
- `parameters`: Parameters for your network connection. Use   to create a default set of parameters that create an encrypted connection with the other devices. You can also add     to provide an application-level messaging protocol.

## See Also

- [static func isSupported(NWBrowser.Descriptor, using: NWParameters?) -> Bool](dddevicepickerviewcontroller/issupported(_:using:).md)
  Returns a Boolean value that indicates whether the current device supports device discovery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepickerviewcontroller/init(browsedescriptor:parameters:))*