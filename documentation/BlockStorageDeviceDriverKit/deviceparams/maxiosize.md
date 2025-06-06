# maxIOSize

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: property

The maximum amount of data per I/O call.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
uint32_t maxIOSize;
```

## See Also

- [numOfBlocks](deviceparams/numofblocks.md)
  The number of blocks on the device.
- [blockSize](deviceparams/blocksize.md)
  The size of a block on the device.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/deviceparams/maxiosize)*