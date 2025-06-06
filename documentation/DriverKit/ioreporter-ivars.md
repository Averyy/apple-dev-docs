# IOReporter_IVars

**Framework**: DriverKit  
**Kind**: struct

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
struct IOReporter_IVars;
```

## Topics

### Instance Properties
- [channelDimension](ioreporter_ivars/channeldimension.md)
- [channelNames](ioreporter_ivars/channelnames.md)
- [channelType](ioreporter_ivars/channeltype.md)
- [configLock](ioreporter_ivars/configlock.md)
- [driver_id](ioreporter_ivars/driver_id.md)
- [elements](ioreporter_ivars/elements.md)
- [enableCounts](ioreporter_ivars/enablecounts.md)
- [enabled](ioreporter_ivars/enabled.md)
- [nChannels](ioreporter_ivars/nchannels.md)
- [nElements](ioreporter_ivars/nelements.md)
- [reporterConfigIsLocked](ioreporter_ivars/reporterconfigislocked.md)
- [reporterIsLocked](ioreporter_ivars/reporterislocked.md)
- [reporterLock](ioreporter_ivars/reporterlock.md)
- [swapElements](ioreporter_ivars/swapelements.md)
- [swapEnableCounts](ioreporter_ivars/swapenablecounts.md)
- [unit](ioreporter_ivars/unit.md)
### Instance Methods
- [IOReporter_IVars](ioreporter_ivars/ioreporter_ivars.md)
  Establishes the parameters of all channels for this reporter instance
- [copyChannelIDs](ioreporter_ivars/copychannelids.md)
- [copyElementValues](ioreporter_ivars/copyelementvalues.md)
- [getChannelIndex](ioreporter_ivars/getchannelindex.md)
- [getChannelIndices](ioreporter_ivars/getchannelindices.md)
- [getElementValues](ioreporter_ivars/getelementvalues.md)
- [getFirstElementIndex](ioreporter_ivars/getfirstelementindex.md)
- [handleAddChannelSwap](ioreporter_ivars/handleaddchannelswap.md)
- [handleConfigureReport](ioreporter_ivars/handleconfigurereport.md)
- [handleCreateLegend](ioreporter_ivars/handlecreatelegend.md)
- [handleSwapCleanup](ioreporter_ivars/handleswapcleanup.md)
- [handleSwapPrepare](ioreporter_ivars/handleswapprepare.md)
- [handleUpdateReport](ioreporter_ivars/handleupdatereport.md)
- [lockReporter](ioreporter_ivars/lockreporter.md)
- [lockReporterConfig](ioreporter_ivars/lockreporterconfig.md)
- [setElementValues](ioreporter_ivars/setelementvalues.md)
- [unlockReporter](ioreporter_ivars/unlockreporter.md)
- [unlockReporterConfig](ioreporter_ivars/unlockreporterconfig.md)
- [updateChannelValues](ioreporter_ivars/updatechannelvalues.md)
- [updateReportChannel](ioreporter_ivars/updatereportchannel.md)
  Internal method to extract channel data to a destination.
- [valid](ioreporter_ivars/valid.md)
- [~IOReporter_IVars](ioreporter_ivars/~ioreporter_ivars.md)
### Type Methods
- [legendWith](ioreporter_ivars/legendwith.md)

## Relationships

### Inherited By
- [IOHistogramReporter_IVars](iohistogramreporter_ivars.md)
- [IOSimpleReporter_IVars](iosimplereporter_ivars.md)
- [IOStateReporter_IVars](iostatereporter_ivars.md)

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
- [IOSimpleReporter_IVars](iosimplereporter_ivars.md)
- [IOStateReporter_IVars](iostatereporter_ivars.md)
- [IOStateReporter_valueSelector](iostatereporter_valueselector.md)
- [IVarsInvalidator](ivarsinvalidator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter_ivars)*