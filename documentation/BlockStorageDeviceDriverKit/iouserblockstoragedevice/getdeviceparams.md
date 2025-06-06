# GetDeviceParams

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method

Gets device parameters in response to a call from the framework.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t GetDeviceParams(struct DeviceParams * deviceParams);
```

#### Return Value

A value that indicates the get-device-params result. Return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) to inidicate success. To indicate a failure, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants) for error definitions.

## Parameters

- `deviceParams`: An in/out   parameter. On output, populate this structure with the device’s parameter data.

## See Also

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
- [DeviceParams](deviceparams.md)
  A structure that represents hardware-specific properties of the block storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/getdeviceparams)*