# GetVendorString

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets a string that identifies the vendor in response to a call from the framework.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t GetVendorString(struct DeviceString *vendor);
```

## Return Value

A value that indicates the get-vendor-string result. Return [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) to inidicate success. To indicate a failure, see [IOKit Constants](../../iokit/iokit_constants.md) for error definitions.

## Parameters

- `vendor`: An in/out [`DeviceString`](../devicestring.md) parameter. On output, populate this structure with the vendor string.

## See Also

### Reporting Device Metadata
- [GetProductString](./getproductstring.md)
  Gets a string that identifies the product in response to a call from the framework.
- [GetRevisionString](./getrevisionstring.md)
  Gets a string that identifies the current revision in response to a call from the framework.
- [GetAdditionalInfoString](./getadditionalinfostring.md)
  Gets a string that provides additional information in response to a call from the framework.
- [DeviceString](../devicestring.md)
  A type that represents a string of character data from the device.
- [GetDeviceParams](./getdeviceparams.md)
  Gets device parameters in response to a call from the framework.
- [DeviceParams](../deviceparams.md)
  A structure that represents hardware-specific properties of the block storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/getvendorstring)*