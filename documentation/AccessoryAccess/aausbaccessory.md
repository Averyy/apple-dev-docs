# AAUSBAccessory

**Framework**: Accessory Access  
**Kind**: class

A class that represents a USB accessory.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class AAUSBAccessory
```

#### Discussion

Obtain a USB accessory from the [`usbAccessoryDidConnect(_:)`](aausbaccessorylistener/usbaccessorydidconnect(_:).md) method, or instantiate one from an [`XPC`](https://developer.apple.com/documentation/xpc) representation that describes an existing USB accessory.

A USB accessory may not be in a configured state when your application receives it. To configure a USB accessory, open it with [`open(serviceQueue:completionHandler:)`](aausbaccessory/open(servicequeue:completionhandler:).md) and select a configuration with [`configureWithValue:error:`](https://developer.apple.com/documentation/iousbhost/iousbhostdevice/configurewithvalue:error:).

## Topics

### Creating USB accessories
- [init?(XPCRepresentation: xpc_object_t)](aausbaccessory/init(xpcrepresentation:)-5lxcr.md)
  Creates a USB accessory from an XPC representation.
- [init?(xpcRepresentation: xpc_object_t)](aausbaccessory/init(xpcrepresentation:)-6dmbu.md)
  Creates a USB accessory from an XPC representation.
- [init?(coder: NSCoder)](aausbaccessory/init(coder:).md)
  Creates a new USB accessory with the provided coder.
### Getting information about a USB accessory
- [var configurationDescriptorData: Data?](aausbaccessory/configurationdescriptordata.md)
  Returns the currently selected configuration descriptor data.
- [var deviceDescriptorData: Data](aausbaccessory/devicedescriptordata.md)
  Returns the device descriptor data.
- [var registryID: UInt64](aausbaccessory/registryid.md)
  Returns the IORegistry ID for the USB accessory.
### Managing a USB accessory
- [func open(serviceQueue: dispatch_queue_t?, completionHandler: (IOUSBHostDevice, (any Error)?) -> Void)](aausbaccessory/open(servicequeue:completionhandler:).md)
  Opens a connection to the USB accessory for this process to access it exclusively.
- [func close(completionHandler: ((any Error)?) -> Void)](aausbaccessory/close(completionhandler:).md)
  Closes all connections to the USB accessory for this process.
### Connection and disconnection events
- [AAUSBAccessory.Event](aausbaccessory/event.md)
  Events that represent accessory connection and disconnection.
### Encoding a USB accessory for delivery to an XPC service
- [func createXPCRepresentation() -> xpc_object_t](aausbaccessory/createxpcrepresentation.md)
  Creates an encoded representation of the USB accessory.
### See also
- [protocol AAUSBAccessoryListener](aausbaccessorylistener.md)
  A class that conforms to the framework’s USB accessory listener protocol can listen to the accessory events.
- [class IOUSBHostDevice](../iousbhost/iousbhostdevice.md)
  The class that claims and configures devices, retrieves descriptors, and sends device requests.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AAUSBAccessoryManager](aausbaccessorymanager.md)
  A class your app uses to manage USB accessories and the listener objects for those accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory)*