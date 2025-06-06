# SCSIDeviceIdentifier

**Framework**: DriverKit  
**Kind**: typealias

64-bit number to represent a SCSI Device.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef UInt64 SCSIDeviceIdentifier;
```

#### Discussion

If the identifier can either be that of an initiator or a target, SCSIDeviceIdentifier should be used.

## See Also

- [IOCallOnceBlock](iocallonceblock.md)
- [IOCallOnceFlag](iocallonceflag.md)
- [IOCommand](iocommand.md)
- [IOCommandPool](iocommandpool.md)
- [IOCommandPoolPtr](iocommandpoolptr.md)
- [IOCommandPtr](iocommandptr.md)
- [IODMACommand](iodmacommand.md)
  An object that converts memory references to I/O bus addresses.
- [IODMACommandSpecification](iodmacommandspecification.md)
- [IODispatchAction](iodispatchaction.md)
- [IOHistogramReporter_IVars](iohistogramreporter_ivars.md)
- [IOReportLegendEntry](ioreportlegendentry.md)
- [IOReporter_IVars](ioreporter_ivars.md)
- [IOSimpleReporter_IVars](iosimplereporter_ivars.md)
- [IOStateReporter_IVars](iostatereporter_ivars.md)
- [IOStateReporter_valueSelector](iostatereporter_valueselector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsideviceidentifier)*