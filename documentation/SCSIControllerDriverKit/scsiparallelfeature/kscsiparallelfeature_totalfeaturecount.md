# kSCSIParallelFeature_TotalFeatureCount

**Framework**: SCSIControllerDriverKit  
**Kind**: case  
**Role**: Enumeration Case

The total number of supported features.

**Availability**:
- DriverKit

## Declaration

```c
kSCSIParallelFeature_TotalFeatureCount
```

#### Discussion

This is the last member of the [`SCSIParallelFeature`](../scsiparallelfeature.md) enumeration. Since the enumeration is zero-based, this value always represents the correct total number of features.

## See Also

### Feature selectors
- [kSCSIParallelFeature_WideDataTransfer](./kscsiparallelfeature_widedatatransfer.md)
  The selector for support of wide data transfers.
- [kSCSIParallelFeature_SynchronousDataTransfer](./kscsiparallelfeature_synchronousdatatransfer.md)
  The selector for support of synchronous data transfers.
- [kSCSIParallelFeature_QuickArbitrationAndSelection](./kscsiparallelfeature_quickarbitrationandselection.md)
  The selector for support of quick arbitration and selection (QAS).
- [kSCSIParallelFeature_DoubleTransitionDataTransfers](./kscsiparallelfeature_doubletransitiondatatransfers.md)
  The selector for support of double transition (DT) data transfers.
- [kSCSIParallelFeature_InformationUnitTransfers](./kscsiparallelfeature_informationunittransfers.md)
  The selector for SPI information unit (IU) transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/scsiparallelfeature/kscsiparallelfeature_totalfeaturecount)*