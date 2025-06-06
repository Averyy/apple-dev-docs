# NSRulerView.UnitName

**Framework**: AppKit  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct UnitName
```

## Topics

### Ruler Units
- [static let centimeters: NSRulerView.UnitName](nsrulerview/unitname/centimeters.md)
- [static let inches: NSRulerView.UnitName](nsrulerview/unitname/inches.md)
- [static let picas: NSRulerView.UnitName](nsrulerview/unitname/picas.md)
- [static let points: NSRulerView.UnitName](nsrulerview/unitname/points.md)
### Initializers
- [init(String)](nsrulerview/unitname/init(_:).md)
- [init(rawValue: String)](nsrulerview/unitname/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func registerUnit(withName: NSRulerView.UnitName, abbreviation: String, unitToPointsConversionFactor: CGFloat, stepUpCycle: [NSNumber], stepDownCycle: [NSNumber])](nsrulerview/registerunit(withname:abbreviation:unittopointsconversionfactor:stepupcycle:stepdowncycle:).md)
  Registers a new unit of measurement with the NSRulerView class, making it available to all instances of NSRulerView.
- [var measurementUnits: NSRulerView.UnitName](nsrulerview/measurementunits.md)
  The measurement units used by the ruler to `unitName`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/unitname)*