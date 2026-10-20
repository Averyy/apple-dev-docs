# selectedFunctionalUnit

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The currently selected functional unit on the scanner.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var selectedFunctionalUnit: ICScannerFunctionalUnit { get }
```

```objc
@property (readonly) ICScannerFunctionalUnit * selectedFunctionalUnit;
```

## See Also

### Selecting a Functional Unit
- [var availableFunctionalUnitTypes: [NSNumber]](./availablefunctionalunittypes.md)
  An array of functional unit types available on this scanner.
- [func requestSelect(ICScannerFunctionalUnitType)](./requestselect%28_%29.md)
  Requests to select a functional unit on the scanner.
- [enum ICScannerFunctionalUnitType](../icscannerfunctionalunittype.md)
  The types of scanner functional units.
- [enum ICScannerFunctionalUnitState](../icscannerfunctionalunitstate.md)
  Flags to indicate the state of the scanner functional unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice/selectedfunctionalunit)*