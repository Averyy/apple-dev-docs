# IOUserBlockStorageDevice

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: class

A DriverKit provider object that manages communications with a block storage device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserBlockStorageDevice;
```

#### Overview

Implement your driver by subclassing this class and overriding all C++ pure virtual methods.

##### Specifying the Drivers Personality Information

When you subclass `IOUserBlockStorageDevice`, update the [`IOKitPersonalities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/IOKitPersonalities) key of your driver extension’s `Info.plist` file with information to match your driver to the correct hardware. For this class, always include the keys and values in the following table:

| Key | Value |
| --- | --- |
| IOClass | `IOUserBlockStorageDevice` |
| IOUserClass | The name of your custom dext class |
| CFBundleIdentifierKernel | `com.apple.iokit.IOStorageFamily` |

## Topics

### Running the Service
- [init](iouserblockstoragedevice/init.md)
  Handles the basic initialization of the service.
- [Start](iouserblockstoragedevice/start.md)
  Starts the current service and associates it with the specified provider.
- [Stop](iouserblockstoragedevice/stop.md)
  Stops the service associated with the specified provider.
- [free](iouserblockstoragedevice/free.md)
  Performs any final cleanup for the service.
### Reporting Device Metadata
- [GetVendorString](iouserblockstoragedevice/getvendorstring.md)
  Gets a string that identifies the vendor in response to a call from the framework.
- [GetProductString](iouserblockstoragedevice/getproductstring.md)
  Gets a string that identifies the product in response to a call from the framework.
- [GetRevisionString](iouserblockstoragedevice/getrevisionstring.md)
  Gets a string that identifies the current revision in response to a call from the framework.
- [GetAdditionalInfoString](iouserblockstoragedevice/getadditionalinfostring.md)
  Gets a string that provides additional information in response to a call from the framework.
- [DeviceString](devicestring.md)
  A type that represents a string of character data from the device.
- [GetDeviceParams](iouserblockstoragedevice/getdeviceparams.md)
  Gets device parameters in response to a call from the framework.
- [DeviceParams](deviceparams.md)
  A structure that represents hardware-specific properties of the block storage device.
### Reporting Device Capabilities
- [ReportEjectability](iouserblockstoragedevice/reportejectability.md)
  Returns a Boolean value that indicates whether the media is ejectable, in response to a call from the framework.
- [ReportRemovability](iouserblockstoragedevice/reportremovability.md)
  Returns a Boolean value that indicates whether the media is removable, in response to a call from the framework.
- [ReportWriteProtection](iouserblockstoragedevice/reportwriteprotection.md)
  Returns a Boolean value that indicates whether the media is write protected, in response to a call from the framework.
### Accessing the Device
- [DoAsyncUnmap](iouserblockstoragedevice/doasyncunmap.md)
  Sends an asynchronous request to the dext to reclaim storage by unmapping.
- [BlockRange](blockrange.md)
  A structure that represents a range of blocks.
- [DoAsyncSynchronize](iouserblockstoragedevice/doasyncsynchronize.md)
  Forces the hardware buffer to flush data blocks to the media.
- [DoAsyncEjectMedia](iouserblockstoragedevice/doasyncejectmedia.md)
  Ejects the media.
- [Complete](iouserblockstoragedevice/complete.md)
  Indicates that the dext completed an asynchronous call.
- [DoAsyncReadWrite](iouserblockstoragedevice/doasyncreadwrite.md)
  Starts an asynchronous read or write operation.
- [IOUserStorageOptions](iouserstorageoptions.md)
  Options that affect the performance of read-write operations.
- [CompleteIO](iouserblockstoragedevice/completeio.md)
  Indicates that the dext completed an asynchronous read-write call.
### Instance Methods
- [DoAsyncUnmapPriv](iouserblockstoragedevice/doasyncunmappriv.md)
- [RegisterDext](iouserblockstoragedevice/registerdext.md)

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice)*