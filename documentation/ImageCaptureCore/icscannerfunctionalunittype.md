# ICScannerFunctionalUnitType

**Framework**: ImageCaptureCore  
**Kind**: enum  
**Role**: Enumeration

The types of scanner functional units.

**Availability**:
- macOS 10.4+

## Declaration

```swift
enum ICScannerFunctionalUnitType
```

```c
enum ICScannerFunctionalUnitType : NSUInteger;
```

## Topics

### Constants
- [ICScannerFunctionalUnitType.documentFeeder](./icscannerfunctionalunittype/documentfeeder.md)
  A document feeder functional unit.
- [ICScannerFunctionalUnitType.flatbed](./icscannerfunctionalunittype/flatbed.md)
  A flatbed functional unit.
- [ICScannerFunctionalUnitType.negativeTransparency](./icscannerfunctionalunittype/negativetransparency.md)
  A transparency functional unit for scanning negatives.
- [ICScannerFunctionalUnitType.positiveTransparency](./icscannerfunctionalunittype/positivetransparency.md)
  A transparency functional unit for scanning positives.
### Initializers
- [init?(rawValue: UInt)](./icscannerfunctionalunittype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Selecting a Functional Unit
- [var availableFunctionalUnitTypes: [NSNumber]](./icscannerdevice/availablefunctionalunittypes.md)
  An array of functional unit types available on this scanner.
- [var selectedFunctionalUnit: ICScannerFunctionalUnit](./icscannerdevice/selectedfunctionalunit.md)
  The currently selected functional unit on the scanner.
- [func requestSelect(ICScannerFunctionalUnitType)](./icscannerdevice/requestselect%28_%29.md)
  Requests to select a functional unit on the scanner.
- [enum ICScannerFunctionalUnitState](./icscannerfunctionalunitstate.md)
  Flags to indicate the state of the scanner functional unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerfunctionalunittype)*