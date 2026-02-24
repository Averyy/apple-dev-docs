# legendWith

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSSharedPtr<IOReportLegendEntry> legendWith(OSArray *channelIDs, OSArray *channelNames, IOReportChannelType channelType, IOReportUnit unit);
```

#### Return Value

An IOReportLegendEntry object or NULL on failure

#### Discussion

Internal method to help create legend entries

This static method is the main legend creation function. It is called by IOReporter sub-classes and is responsible for building an IOReportLegendEntry corresponding to this reporter object. This legend entry may be extended by the sub-class of IOReporter if required.

Locking: SAFE to call concurrently (no static globals), MAY BLOCK

## Parameters

- `channelIDs`: - OSArray of OSNumber(uint64_t) channels IDs.
- `channelNames`: - parrallel OSArray of OSSymbol(rich names)
- `channelType`: - the type of all channels in this legend
- `unit`: - The unit for the quantity recorded by this reporter object


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter_ivars/legendwith)*