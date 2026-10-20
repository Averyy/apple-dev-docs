# measurementUnits

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The measurement units used by the ruler to `unitName`.

**Availability**:
- macOS

## Declaration

```swift
var measurementUnits: NSRulerView.UnitName { get set }
```

```objc
@property (copy) NSRulerViewUnitName measurementUnits;
```

#### Discussion

`unitName` must have been registered with the NSRulerView class object prior to invoking this method. See the description of the class method [`registerUnit(withName:abbreviation:unitToPointsConversionFactor:stepUpCycle:stepDownCycle:)`](./registerunit%28withname,abbreviation,unittopointsconversionfactor,stepupcycle,stepdowncycle%29.md) for a list of predefined units.

## See Also

### Altering measurement units
- [class func registerUnit(withName: NSRulerView.UnitName, abbreviation: String, unitToPointsConversionFactor: CGFloat, stepUpCycle: [NSNumber], stepDownCycle: [NSNumber])](./registerunit%28withname,abbreviation,unittopointsconversionfactor,stepupcycle,stepdowncycle%29.md)
  Registers a new unit of measurement with the NSRulerView class, making it available to all instances of NSRulerView.
- [NSRulerView.UnitName](./unitname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/measurementunits)*