# NSRulerView.UnitName

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct UnitName
```

```c
typedef NSString * NSRulerViewUnitName;
```

## Topics

### Ruler Units
- [static let centimeters: NSRulerView.UnitName](./unitname/centimeters.md)
- [static let inches: NSRulerView.UnitName](./unitname/inches.md)
- [static let picas: NSRulerView.UnitName](./unitname/picas.md)
- [static let points: NSRulerView.UnitName](./unitname/points.md)
### Initializers
- [init(String)](./unitname/init%28_%29.md)
- [init(rawValue: String)](./unitname/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Altering measurement units
- [class func registerUnit(withName: NSRulerView.UnitName, abbreviation: String, unitToPointsConversionFactor: CGFloat, stepUpCycle: [NSNumber], stepDownCycle: [NSNumber])](./registerunit%28withname,abbreviation,unittopointsconversionfactor,stepupcycle,stepdowncycle%29.md)
  Registers a new unit of measurement with the NSRulerView class, making it available to all instances of NSRulerView.
- [var measurementUnits: NSRulerView.UnitName](./measurementunits.md)
  The measurement units used by the ruler to `unitName`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/unitname)*