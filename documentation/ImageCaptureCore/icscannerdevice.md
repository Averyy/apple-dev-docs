# ICScannerDevice

**Framework**: ImageCaptureCore  
**Kind**: class

An object that represents a scanner.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class ICScannerDevice
```

#### Overview

An instance of ICScannerDevice class is intended to be used by the ICScannerDeviceView object. The ICScannerDeviceView class encapsulates the complexities of setting scan parameters, performing scans and saving the result. The developer should consider using ICScannerDeviceView instead of building their own views using the ICScannerDevice object.

## Topics

### Selecting a Functional Unit
- [var availableFunctionalUnitTypes: [NSNumber]](icscannerdevice/availablefunctionalunittypes.md)
  An array of functional unit types available on this scanner.
- [var selectedFunctionalUnit: ICScannerFunctionalUnit](icscannerdevice/selectedfunctionalunit.md)
  The currently selected functional unit on the scanner.
- [func requestSelect(ICScannerFunctionalUnitType)](icscannerdevice/requestselect(_:).md)
  Requests to select a functional unit on the scanner.
- [enum ICScannerFunctionalUnitType](icscannerfunctionalunittype.md)
  The types of scanner functional units.
- [enum ICScannerFunctionalUnitState](icscannerfunctionalunitstate.md)
  Flags to indicate the state of the scanner functional unit.
### Performing a Scan
- [func requestOpenSession(withCredentials: String, password: String)](icscannerdevice/requestopensession(withcredentials:password:).md)
  Opens a session on the protected device with the authorized username and passcode.
- [func requestOverviewScan()](icscannerdevice/requestoverviewscan.md)
  Starts an overview scan on the selected functional unit.
- [func requestScan()](icscannerdevice/requestscan.md)
  Starts a scan on the selected functional unit.
- [func cancelScan()](icscannerdevice/cancelscan.md)
  Cancels the current scan.
- [var documentName: String](icscannerdevice/documentname.md)
  The document’s name.
- [var documentUTI: String](icscannerdevice/documentuti.md)
  The document’s uniform type identifier.
- [var downloadsDirectory: URL](icscannerdevice/downloadsdirectory.md)
  The downloads directory.
- [var transferMode: ICScannerTransferMode](icscannerdevice/transfermode.md)
  The transfer mode for the scanned document.
- [var maxMemoryBandSize: UInt32](icscannerdevice/maxmemorybandsize.md)
  The total maximum band size requested when performing a memory-based transfer.
### Logging into a Protected Device
- [var defaultUsername: String](icscannerdevice/defaultusername.md)
  A default username on protected scanners.

## Relationships

### Inherits From
- [ICDevice](icdevice.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol ICScannerDeviceDelegate](icscannerdevicedelegate.md)
  Methods for determining availability, selecting a functional unit, and performing scans on connected scanners.
- [Scanner Configuration](scanner-configuration.md)
  Examine a scanner’s functional units and features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice)*