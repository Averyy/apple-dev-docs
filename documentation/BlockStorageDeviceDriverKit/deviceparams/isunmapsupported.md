# isUnmapSupported

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device supports unmapping to reclaim storage.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
bool isUnmapSupported;
```

## See Also

### Accessing Device Parameters
- [numOfBlocks](./numofblocks.md)
  The number of blocks on the device.
- [blockSize](./blocksize.md)
  The size of a block on the device.
- [maxIOSize](./maxiosize.md)
  The maximum amount of data per I/O call.
- [numOfOutstandingIOs](./numofoutstandingios.md)
  The upper limit to the number of requests sent to the device.
- [maxNumOfUnmapRegions](./maxnumofunmapregions.md)
  The maximum number of regions supported by an unmap call.
- [minSegmentAlignment](./minsegmentalignment.md)
  The minimum alignment of the data buffer sent to read-write calls.
- [numOfAddressBits](./numofaddressbits.md)
  The number of bits used to address blocks on the device.
- [isFUASupported](./isfuasupported.md)
  A Boolean value that indicates whether the device supports forced unit access (FUA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/deviceparams/isunmapsupported)*