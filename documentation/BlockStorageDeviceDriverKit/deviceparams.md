# DeviceParams

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: struct

A structure that represents hardware-specific properties of the block storage device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
struct DeviceParams;
```

#### Discussion

Implement the [`GetDeviceParams`](iouserblockstoragedevice/getdeviceparams.md) method to provide the framework with the device-specific properties indicated by this structure.

## Topics

### Accessing Device Parameters
- [numOfBlocks](deviceparams/numofblocks.md)
  The number of blocks on the device.
- [blockSize](deviceparams/blocksize.md)
  The size of a block on the device.
- [maxIOSize](deviceparams/maxiosize.md)
  The maximum amount of data per I/O call.
- [numOfOutstandingIOs](deviceparams/numofoutstandingios.md)
  The upper limit to the number of requests sent to the device.
- [maxNumOfUnmapRegions](deviceparams/maxnumofunmapregions.md)
  The maximum number of regions supported by an unmap call.
- [minSegmentAlignment](deviceparams/minsegmentalignment.md)
  The minimum alignment of the data buffer sent to read-write calls.
- [numOfAddressBits](deviceparams/numofaddressbits.md)
  The number of bits used to address blocks on the device.
- [isUnmapSupported](deviceparams/isunmapsupported.md)
  A Boolean value that indicates whether the device supports unmapping to reclaim storage.
- [isFUASupported](deviceparams/isfuasupported.md)
  A Boolean value that indicates whether the device supports forced unit access (FUA).

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
- [GetDeviceParams](iouserblockstoragedevice/getdeviceparams.md)
  Gets device parameters in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/deviceparams)*