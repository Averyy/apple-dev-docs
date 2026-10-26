# IOUSBHostObject

**Framework**: IOUSBHost  
**Kind**: class  
**Role**: Class

This class provides basic functionality for sending device requests and retrieving descriptors.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostObject
```

```objc
@interface IOUSBHostObject : NSObject
```

## Topics

### Managing the Object Life Cycle
- [struct IOUSBHostObjectInitOptions](./iousbhostobjectinitoptions.md)
  Options for initializing the host object.
- [typealias IOUSBHostInterestHandler](./iousbhostinteresthandler.md)
  The callback that handles underlying service-state changes.
- [var ioService: io_service_t](./iousbhostobject/ioservice.md)
  A reference to the kernel object.
- [var queue: dispatch_queue_t](./iousbhostobject/queue.md)
  The queue for servicing input/output requests.
- [func destroy()](./iousbhostobject/destroy%28%29.md)
  Removes underlying allocations and connections from the USB host object.
- [- initWithIOService:options:queue:error:interestHandler:](./iousbhostobject/initwithioservice_options_queue_error_interesthandler_.md)
  Creates a USB host object and sets up a communication channel to the kernel.
- [- initWithIOService:queue:error:interestHandler:](./iousbhostobject/initwithioservice_queue_error_interesthandler_.md)
  Creates a USB host object and sets up a default communication channel to the kernel.
### Retrieving Base Class Descriptors
- [Parsing USB Descriptors](./parsing-usb-descriptors.md)
  Extract information from various USB descriptors using helper methods.
- [- descriptorWithType:length:index:languageID:requestType:requestRecipient:error:](./iousbhostobject/descriptorwithtype_length_index_languageid_requesttype_requestrecipient_error_.md)
  Retrieves a descriptor from the cache or the device.
- [- descriptorWithType:length:error:](./iousbhostobject/descriptorwithtype_length_error_.md)
  Retrieves a descriptor with default arguments from the cache or the device.
- [- descriptorWithType:length:index:languageID:error:](./iousbhostobject/descriptorwithtype_length_index_languageid_error_.md)
  Retrieves a string descriptor from the cache or the device.
- [- stringWithIndex:languageID:error:](./iousbhostobject/stringwithindex_languageid_error_.md)
  Retrieves a string from a string descriptor.
- [- stringWithIndex:error:](./iousbhostobject/stringwithindex_error_.md)
  Retrieves an English-language string from a string descriptor.
### Creating I/O Buffers
- [func ioData(withCapacity: Int) throws -> NSMutableData](./iousbhostobject/iodata%28withcapacity%29.md)
  Allocates a buffer for input/output requests.
### Sending Device Requests
- [func IOUSBHostDeviceRequestType(tIOUSBDeviceRequestDirectionValue, tIOUSBDeviceRequestTypeValue, tIOUSBDeviceRequestRecipientValue) -> UInt8](./iousbhostdevicerequesttype%28_,_,_%29.md)
  Creates the request type field of a device request.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](./iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [- sendDeviceRequest:data:bytesTransferred:completionTimeout:error:](./iousbhostobject/senddevicerequest_data_bytestransferred_completiontimeout_error_.md)
  Sends a request on the default control endpoint.
- [- sendDeviceRequest:data:bytesTransferred:error:](./iousbhostobject/senddevicerequest_data_bytestransferred_error_.md)
  Sends a request on the default control endpoint with a default completion timeout.
- [- sendDeviceRequest:error:](./iousbhostobject/senddevicerequest_error_.md)
  Sends a request on the default control endpoint without a data phase and default completion timeout.
### Enqueueing Device Requests
- [typealias IOUSBHostCompletionHandler](./iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [- enqueueDeviceRequest:data:completionTimeout:error:completionHandler:](./iousbhostobject/enqueuedevicerequest_data_completiontimeout_error_completionhandler_.md)
  Enqueues a request on the default control endpoint.
- [- enqueueDeviceRequest:data:error:completionHandler:](./iousbhostobject/enqueuedevicerequest_data_error_completionhandler_.md)
  Enqueues a request on the default control endpoint with a default completion timeout.
- [- enqueueDeviceRequest:error:completionHandler:](./iousbhostobject/enqueuedevicerequest_error_completionhandler_.md)
  Enqueues a request on the default control endpoint without a data phase and a default timeout.
### Aborting Device Requests
- [enum IOUSBHostAbortOption](./iousbhostabortoption.md)
  Options for aborting pending input/output requests.
- [- abortDeviceRequestsWithOption:error:](./iousbhostobject/abortdevicerequestswithoption_error_.md)
  Aborts device requests.
- [- abortDeviceRequestsWithError:](./iousbhostobject/abortdevicerequestswitherror_.md)
  Aborts device requests synchronously.
### Getting Host Information
- [var deviceAddress: Int](./iousbhostobject/deviceaddress.md)
  The device’s bus address.
- [- frameNumberWithTime:](./iousbhostobject/framenumberwithtime_.md)
  Returns the current frame number of the USB controller.
### Instance Properties
- [var capabilityDescriptors: UnsafePointer<IOUSBBOSDescriptor>?](./iousbhostobject/capabilitydescriptors.md)
- [var deviceDescriptor: UnsafePointer<IOUSBDeviceDescriptor>?](./iousbhostobject/devicedescriptor.md)
### Instance Methods
- [func configurationDescriptor(with: Int) throws -> UnsafePointer<IOUSBConfigurationDescriptor>](./iousbhostobject/configurationdescriptor%28with%29.md)
- [func configurationDescriptor(withConfigurationValue: Int) throws -> UnsafePointer<IOUSBConfigurationDescriptor>](./iousbhostobject/configurationdescriptor%28withconfigurationvalue%29.md)
- [func data(withCapacity: Int, options: IOUSBHostObjectDataOptions) throws -> NSMutableData](./iousbhostobject/data%28withcapacity,options%29.md)
- [func destroy(options: IOUSBHostObjectDestroyOptions)](./iousbhostobject/destroy%28options%29.md)
- [- currentMicroframeWithTime:error:](./iousbhostobject/currentmicroframewithtime_error_.md)
- [- referenceMicroframeWithTime:error:](./iousbhostobject/referencemicroframewithtime_error_.md)
### Related Documentation
- [class IOUSBHostDevice](./iousbhostdevice.md)
  The class that claims and configures devices, retrieves descriptors, and sends device requests.
- [class IOUSBHostInterface](./iousbhostinterface.md)
  The class for accessing USB-related services.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [IOUSBHostDevice](./iousbhostdevice.md)
- [IOUSBHostInterface](./iousbhostinterface.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Base Classes
- [class IOUSBHostIOSource](./iousbhostiosource.md)
  This class provides basic functionality for deriving pipe and stream classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject)*