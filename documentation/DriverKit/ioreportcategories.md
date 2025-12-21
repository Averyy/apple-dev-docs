# IOReportCategories

**Framework**: DriverKit  
**Kind**: typealias

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef uint16_t IOReportCategories;
```

#### Discussion

Encapsulate important, multi-purpose “tags” for channels

IOReportCategories is the type for the .categories field of IOReportChanelType.  These categories are inteded to empower a limited number of clients to retrieve a broad range of channels without knowing much about them.  They can be OR’d together as needed.  Groups and subgroups are a more extensible mechanism for aggregating channels produced by different drivers.

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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreportcategories)*