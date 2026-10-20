# UserGetDMASpecification

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the controller-specific direct memory access (DMA) specification in response to a call from the framework.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserGetDMASpecification(uint64_t *maxTransferSize, uint32_t *alignment, uint8_t *numAddressBits, DMAOutputSegmentType *segmentType);
```

#### Return Value

A value that indicates the result of getting the DMA specification. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

## Parameters

- `maxTransferSize`: The maximum allowable transfer size for the controller.
- `alignment`: The required alignment for the controller.
- `numAddressBits`: The number of bits that the hardware uses on its internal address bus.
- `segmentType`: On return, set this output segment type according to the endianness of the hardware.

## See Also

### Managing direct memory access
- [DMAOutputSegmentType](../dmaoutputsegmenttype.md)
  The size and endianness that the system uses for direct memory access (DMA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usergetdmaspecification)*