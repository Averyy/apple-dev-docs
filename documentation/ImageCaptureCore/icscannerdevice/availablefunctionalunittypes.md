# availableFunctionalUnitTypes

**Framework**: ImageCaptureCore  
**Kind**: property

An array of functional unit types available on this scanner.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var availableFunctionalUnitTypes: [NSNumber] { get }
```

#### Discussion

This array contains [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects whose values are of type [`ICScannerFunctionalUnitType`](icscannerfunctionalunittype.md).

## See Also

- [var selectedFunctionalUnit: ICScannerFunctionalUnit](icscannerdevice/selectedfunctionalunit.md)
  The currently selected functional unit on the scanner.
- [func requestSelect(ICScannerFunctionalUnitType)](icscannerdevice/requestselect(_:).md)
  Requests to select a functional unit on the scanner.
- [enum ICScannerFunctionalUnitType](icscannerfunctionalunittype.md)
  The types of scanner functional units.
- [enum ICScannerFunctionalUnitState](icscannerfunctionalunitstate.md)
  Flags to indicate the state of the scanner functional unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice/availablefunctionalunittypes)*