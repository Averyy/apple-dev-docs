# IOUSBHostObject

**Framework**: IOUSBHost  
**Kind**: class

This class provides basic functionality for sending device requests and retrieving descriptors.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostObject
```

## Topics

### Managing the Object Life Cycle
- [struct IOUSBHostObjectInitOptions](iousbhostobjectinitoptions.md)
  Options for initializing the host object.
- [typealias IOUSBHostInterestHandler](iousbhostinteresthandler.md)
  The callback that handles underlying service-state changes.
- [var ioService: io_service_t](iousbhostobject/ioservice.md)
  A reference to the kernel object.
- [var queue: dispatch_queue_t](iousbhostobject/queue.md)
  The queue for servicing input/output requests.
- [func destroy()](iousbhostobject/destroy.md)
  Removes underlying allocations and connections from the USB host object.
### Retrieving Base Class Descriptors
- [Parsing USB Descriptors](parsing-usb-descriptors.md)
  Extract information from various USB descriptors using helper methods.
### Creating I/O Buffers
- [func ioData(withCapacity: Int) throws -> NSMutableData](iousbhostobject/iodata(withcapacity:).md)
  Allocates a buffer for input/output requests.
### Sending Device Requests
- [func IOUSBHostDeviceRequestType(tIOUSBDeviceRequestDirectionValue, tIOUSBDeviceRequestTypeValue, tIOUSBDeviceRequestRecipientValue) -> UInt8](iousbhostdevicerequesttype(_:_:_:).md)
  Creates the request type field of a device request.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
### Enqueueing Device Requests
- [typealias IOUSBHostCompletionHandler](iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
### Aborting Device Requests
- [enum IOUSBHostAbortOption](iousbhostabortoption.md)
  Options for aborting pending input/output requests.
### Getting Host Information
- [var deviceAddress: Int](iousbhostobject/deviceaddress.md)
  The device’s bus address.
### Instance Properties
- [var capabilityDescriptors: UnsafePointer<IOUSBBOSDescriptor>?](iousbhostobject/capabilitydescriptors.md)
- [var deviceDescriptor: UnsafePointer<IOUSBDeviceDescriptor>?](iousbhostobject/devicedescriptor.md)
### Instance Methods
- [func configurationDescriptor(with: Int) throws -> UnsafePointer<IOUSBConfigurationDescriptor>](iousbhostobject/configurationdescriptor(with:).md)
- [func configurationDescriptor(withConfigurationValue: Int) throws -> UnsafePointer<IOUSBConfigurationDescriptor>](iousbhostobject/configurationdescriptor(withconfigurationvalue:).md)
- [func destroy(options: IOUSBHostObjectDestroyOptions)](iousbhostobject/destroy(options:).md)
### Related Documentation
- [class IOUSBHostDevice](iousbhostdevice.md)
  The class that claims and configures devices, retrieves descriptors, and sends device requests.
- [class IOUSBHostInterface](iousbhostinterface.md)
  The class for accessing USB-related services.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [IOUSBHostDevice](iousbhostdevice.md)
- [IOUSBHostInterface](iousbhostinterface.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class IOUSBHostIOSource](iousbhostiosource.md)
  This class provides basic functionality for deriving pipe and stream classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject)*