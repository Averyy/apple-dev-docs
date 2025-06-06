# SCSITaggedTaskIdentifier

**Framework**: DriverKit  
**Kind**: typealias

64-bit number to represent a unique task identifier.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef UInt64 SCSITaggedTaskIdentifier;
```

#### Discussion

The Tagged Task Identifier is used when a Task has a Task Attribute other than SIMPLE. The SCSI Application Layer client that controls the Logical Unit for which a Task is intended is required to guarantee that the Task Tag Identifier is unique. Zero cannot be used a a Tag value as this is used to when a Tagged Task Identifier value is needed for a Task with a SIMPLE attribute.

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsitaggedtaskidentifier)*