# requestSelect(_:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Requests to select a functional unit on the scanner.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func requestSelect(_ type: ICScannerFunctionalUnitType)
```

```objc
- (void) requestSelectFunctionalUnit:(ICScannerFunctionalUnitType) type;
```

#### Discussion

When the request has completed, [`scannerDevice(_:didSelect:error:)`](../icscannerdevicedelegate/scannerdevice%28_,didselect,error%29.md) is called on the delegate.

## See Also

### Selecting a Functional Unit
- [var availableFunctionalUnitTypes: [NSNumber]](./availablefunctionalunittypes.md)
  An array of functional unit types available on this scanner.
- [var selectedFunctionalUnit: ICScannerFunctionalUnit](./selectedfunctionalunit.md)
  The currently selected functional unit on the scanner.
- [enum ICScannerFunctionalUnitType](../icscannerfunctionalunittype.md)
  The types of scanner functional units.
- [enum ICScannerFunctionalUnitState](../icscannerfunctionalunitstate.md)
  Flags to indicate the state of the scanner functional unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice/requestselect(_:))*