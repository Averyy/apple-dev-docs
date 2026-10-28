# AAUSBAccessory

**Framework**: Accessory Access  
**Kind**: class  
**Role**: Class

A class that represents a USB accessory.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class AAUSBAccessory
```

```objc
@interface AAUSBAccessory : NSObject
```

## Discussion

Obtain a USB accessory from the [`usbAccessoryDidConnect(_:)`](./aausbaccessorylistener/usbaccessorydidconnect%28_%29.md) method, or instantiate one from an [XPC](../XPC/XPC.md) representation that describes an existing USB accessory.

A USB accessory may not be in a configured state when your application receives it. To configure a USB accessory, open it with [`open(serviceQueue:completionHandler:)`](./aausbaccessory/open%28servicequeue,completionhandler%29.md) and select a configuration with [`configureWithValue:error:`](../IOUSBHost/iousbhostdevice/configurewithvalue_error_.md).

## Topics

### Creating USB accessories
- [init?(XPCRepresentation: xpc_object_t)](./aausbaccessory/init%28xpcrepresentation%29-5lxcr.md)
  Creates a USB accessory from an XPC representation.
- [init?(xpcRepresentation: xpc_object_t)](./aausbaccessory/init%28xpcrepresentation%29-6dmbu.md)
  Creates a USB accessory from an XPC representation.
- [init?(coder: NSCoder)](./aausbaccessory/init%28coder%29.md)
  Creates a new USB accessory with the provided coder.
### Getting information about a USB accessory
- [var configurationDescriptorData: Data?](./aausbaccessory/configurationdescriptordata.md)
  Returns the currently selected configuration descriptor data.
- [var deviceDescriptorData: Data](./aausbaccessory/devicedescriptordata.md)
  Returns the device descriptor data.
- [var registryID: UInt64](./aausbaccessory/registryid.md)
  Returns the IORegistry ID for the USB accessory.
### Managing a USB accessory
- [func open(serviceQueue: dispatch_queue_t?, completionHandler: (IOUSBHostDevice, (any Error)?) -> Void)](./aausbaccessory/open%28servicequeue,completionhandler%29.md)
  Opens a connection to the USB accessory for this process to access it exclusively.
- [func close(completionHandler: ((any Error)?) -> Void)](./aausbaccessory/close%28completionhandler%29.md)
  Closes all connections to the USB accessory for this process.
### Connection and disconnection events
- [AAUSBAccessory.Event](./aausbaccessory/event.md)
  Events that represent accessory connection and disconnection.
### Encoding a USB accessory for delivery to an XPC service
- [func createXPCRepresentation() -> xpc_object_t](./aausbaccessory/createxpcrepresentation%28%29.md)
  Creates an encoded representation of the USB accessory.
### See also
- [protocol AAUSBAccessoryListener](./aausbaccessorylistener.md)
  A class that conforms to the framework’s USB accessory listener protocol can listen to the accessory events.
- [class IOUSBHostDevice](../IOUSBHost/iousbhostdevice.md)
  The class that claims and configures devices, retrieves descriptors, and sends device requests.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing accessories
- [class AAUSBAccessoryManager](./aausbaccessorymanager.md)
  A class your app uses to manage USB accessories and the listener objects for those accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory)*