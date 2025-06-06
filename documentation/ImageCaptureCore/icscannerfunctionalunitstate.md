# ICScannerFunctionalUnitState

**Framework**: ImageCaptureCore  
**Kind**: enum

Flags to indicate the state of the scanner functional unit.

**Availability**:
- macOS 10.4+

## Declaration

```swift
enum ICScannerFunctionalUnitState
```

## Topics

### Constants
- [ICScannerFunctionalUnitState.ready](icscannerfunctionalunitstate/ready.md)
  A flag indicating that the functional unit is ready for operation.
- [ICScannerFunctionalUnitState.overviewScanInProgress](icscannerfunctionalunitstate/overviewscaninprogress.md)
  A flag indicating that the functional unit is performing an overview scan.
- [ICScannerFunctionalUnitState.scanInProgress](icscannerfunctionalunitstate/scaninprogress.md)
  A flag indicating that the functional unit is performing a scan.
### Initializers
- [init?(rawValue: UInt)](icscannerfunctionalunitstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var availableFunctionalUnitTypes: [NSNumber]](icscannerdevice/availablefunctionalunittypes.md)
  An array of functional unit types available on this scanner.
- [var selectedFunctionalUnit: ICScannerFunctionalUnit](icscannerdevice/selectedfunctionalunit.md)
  The currently selected functional unit on the scanner.
- [func requestSelect(ICScannerFunctionalUnitType)](icscannerdevice/requestselect(_:).md)
  Requests to select a functional unit on the scanner.
- [enum ICScannerFunctionalUnitType](icscannerfunctionalunittype.md)
  The types of scanner functional units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerfunctionalunitstate)*