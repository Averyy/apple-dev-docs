# measurementUnits

**Framework**: AppKit  
**Kind**: property

The measurement units used by the ruler to `unitName`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var measurementUnits: NSRulerView.UnitName { get set }
```

#### Discussion

`unitName` must have been registered with the NSRulerView class object prior to invoking this method. See the description of the class method [`registerUnit(withName:abbreviation:unitToPointsConversionFactor:stepUpCycle:stepDownCycle:)`](nsrulerview/registerunit(withname:abbreviation:unittopointsconversionfactor:stepupcycle:stepdowncycle:).md) for a list of predefined units.

## See Also

- [class func registerUnit(withName: NSRulerView.UnitName, abbreviation: String, unitToPointsConversionFactor: CGFloat, stepUpCycle: [NSNumber], stepDownCycle: [NSNumber])](nsrulerview/registerunit(withname:abbreviation:unittopointsconversionfactor:stepupcycle:stepdowncycle:).md)
  Registers a new unit of measurement with the NSRulerView class, making it available to all instances of NSRulerView.
- [NSRulerView.UnitName](nsrulerview/unitname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/measurementunits)*