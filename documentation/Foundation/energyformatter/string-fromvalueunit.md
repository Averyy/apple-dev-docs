# string(fromValue:unit:)

**Framework**: Foundation  
**Kind**: method

Returns a properly formatted energy string for the given value and unit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func string(fromValue value: Double, unit: EnergyFormatter.Unit) -> String
```

#### Return Value

A localized string that combines the provided value and unit.

## Parameters

- `value`: The energy value in the given unit.
- `unit`: The unit used in the resulting energy string.

## See Also

- [var isForFoodEnergyUse: Bool](energyformatter/isforfoodenergyuse.md)
  A Boolean value that indicates whether the energy value is used to measure food energy.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](energyformatter/getobjectvalue(_:for:errordescription:).md)
  This method is not supported for the `NSEnergyFormatter` class.
- [var numberFormatter: NumberFormatter!](energyformatter/numberformatter.md)
  The number formatter used to format the numbers in energy strings.
- [func string(fromJoules: Double) -> String](energyformatter/string(fromjoules:).md)
  Returns an energy string for the provided value.
- [func unitString(fromJoules: Double, usedUnit: UnsafeMutablePointer<EnergyFormatter.Unit>?) -> String](energyformatter/unitstring(fromjoules:usedunit:).md)
  Returns the unit string for the provided value.
- [func unitString(fromValue: Double, unit: EnergyFormatter.Unit) -> String](energyformatter/unitstring(fromvalue:unit:).md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](energyformatter/unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/energyformatter/string(fromvalue:unit:))*