# AAUSBAccessory

**Framework**: Accessory Access  
**Kind**: class

A class that represents a USB accessory.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class AAUSBAccessory
```

#### Discussion

A USB accessory can either be obtained from the [`usbAccessoryDidConnect(_:)`](aausbaccessorylistener/usbaccessorydidconnect(_:).md) method, or instantiated from an [`XPC`](https://developer.apple.com/documentation/XPC) representation that describes an existing USB accessory.

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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AAUSBAccessoryManager](aausbaccessorymanager.md)
  A class your app uses to manage USB accessories and the listener objects for those accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory)*