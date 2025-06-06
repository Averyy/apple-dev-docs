# CMIOExtensionProvider

**Framework**: Core Media I/O  
**Kind**: class

An object that manages device connections for a provider.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionProvider
```

## Mentions

- [Creating a camera extension with Core Media I/O](creating-a-camera-extension-with-core-media-i-o.md)

#### Overview

An extension provider manages device connections and provides the [`startService(provider:)`](cmioextensionprovider/startservice(provider:).md) class method that you call to bootstrap the service.

## Topics

### Creating a Provider
- [init(source: any CMIOExtensionProviderSource, clientQueue: dispatch_queue_t?)](cmioextensionprovider/init(source:clientqueue:).md)
  Creates an extension provider with the specified source and dispatch queue.
### Inspecting a Provider
- [var clientQueue: dispatch_queue_t](cmioextensionprovider/clientqueue.md)
  The dispatch queue on which the system performs client operations.
- [var source: (any CMIOExtensionProviderSource)?](cmioextensionprovider/source.md)
  The source for the provider.
### Starting a Provider
- [class func startService(provider: CMIOExtensionProvider)](cmioextensionprovider/startservice(provider:).md)
  Starts the system extension.
### Managing Devices
- [var devices: [CMIOExtensionDevice]](cmioextensionprovider/devices.md)
  An array of connected devices.
- [func addDevice(CMIOExtensionDevice) throws](cmioextensionprovider/adddevice(_:).md)
  Adds a device to a provider.
- [func removeDevice(CMIOExtensionDevice) throws](cmioextensionprovider/removedevice(_:).md)
  Removes a device from a provider.
### Managing Clients
- [var connectedClients: [CMIOExtensionClient]](cmioextensionprovider/connectedclients.md)
  An array of connected clients.
- [func notifyPropertiesChanged([CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](cmioextensionprovider/notifypropertieschanged(_:).md)
  Notifies connected clients of device property changes.
### Type Methods
- [class func ignoreSIGTERM()](cmioextensionprovider/ignoresigterm.md)
- [class func stopService(provider: CMIOExtensionProvider)](cmioextensionprovider/stopservice(provider:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating a camera extension with Core Media I/O](creating-a-camera-extension-with-core-media-i-o.md)
  Build high-performance camera drivers that are secure and simple to deploy.
- [Overriding the default USB video class extension](overriding-the-default-usb-video-class-extension.md)
  Create a simple DriverKit extension to override the default driver-matching behavior for USB devices.
- [protocol CMIOExtensionProviderSource](cmioextensionprovidersource.md)
  A protocol for objects that act as provider sources.
- [class CMIOExtensionProviderProperties](cmioextensionproviderproperties.md)
  An object that manages the properties of an extension provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider)*