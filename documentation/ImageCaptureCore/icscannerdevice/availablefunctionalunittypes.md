# availableFunctionalUnitTypes

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

An array of functional unit types available on this scanner.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var availableFunctionalUnitTypes: [NSNumber] { get }
```

```objc
@property (readonly) NSArray<NSNumber *> * availableFunctionalUnitTypes;
```

#### Discussion

This array contains [`NSNumber`](../../Foundation/nsnumber.md) objects whose values are of type [`ICScannerFunctionalUnitType`](../icscannerfunctionalunittype.md).

## See Also

### Selecting a Functional Unit
- [var selectedFunctionalUnit: ICScannerFunctionalUnit](./selectedfunctionalunit.md)
  The currently selected functional unit on the scanner.
- [func requestSelect(ICScannerFunctionalUnitType)](./requestselect%28_%29.md)
  Requests to select a functional unit on the scanner.
- [enum ICScannerFunctionalUnitType](../icscannerfunctionalunittype.md)
  The types of scanner functional units.
- [enum ICScannerFunctionalUnitState](../icscannerfunctionalunitstate.md)
  Flags to indicate the state of the scanner functional unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice/availablefunctionalunittypes)*