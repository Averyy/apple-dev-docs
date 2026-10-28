# unitString(fromJoules:usedUnit:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the unit string for the provided value.

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
func unitString(fromJoules numberInJoules: Double, usedUnit unitp: UnsafeMutablePointer<EnergyFormatter.Unit>?) -> String
```

```objc
- (NSString *) unitStringFromJoules:(double) numberInJoules usedUnit:(NSEnergyFormatterUnit *) unitp;
```

## Return Value

A localized string representing the unit.

## Discussion

This method selects the correct unit based on the formatter’s locale, the magnitude of the value, and the [`isForFoodEnergyUse`](./isforfoodenergyuse.md) property.

## Parameters

- `numberInJoules`: The energy value in joules.
- `unitp`: An output parameter. This will hold the [`EnergyFormatter.Unit`](./unit.md) value that corresponds to the returned units.

## See Also

### Formatting Energy Strings
- [var isForFoodEnergyUse: Bool](./isforfoodenergyuse.md)
  A Boolean value that indicates whether the energy value is used to measure food energy.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getobjectvalue%28_,for,errordescription%29.md)
  This method is not supported for the `NSEnergyFormatter` class.
- [var numberFormatter: NumberFormatter!](./numberformatter.md)
  The number formatter used to format the numbers in energy strings.
- [func string(fromJoules: Double) -> String](./string%28fromjoules%29.md)
  Returns an energy string for the provided value.
- [func string(fromValue: Double, unit: EnergyFormatter.Unit) -> String](./string%28fromvalue,unit%29.md)
  Returns a properly formatted energy string for the given value and unit.
- [func unitString(fromValue: Double, unit: EnergyFormatter.Unit) -> String](./unitstring%28fromvalue,unit%29.md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](./unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/energyformatter/unitstring(fromjoules:usedunit:))*