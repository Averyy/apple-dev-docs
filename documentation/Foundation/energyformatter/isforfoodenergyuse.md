# isForFoodEnergyUse

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the energy value is used to measure food energy.

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
var isForFoodEnergyUse: Bool { get set }
```

```objc
@property (getter=isForFoodEnergyUse) BOOL forFoodEnergyUse;
```

## Discussion

Returns [`true`](../../Swift/true.md) if the energy is used to measure food energy; otherwise, [`false`](../../Swift/false.md). If set to [`true`](../../Swift/true.md), [`EnergyFormatter.Unit.kilocalorie`](./unit/kilocalorie.md) may be represented using “C” instead of “kcal”. By default, this property returns [`false`](../../Swift/false.md).

## See Also

### Formatting Energy Strings
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getobjectvalue%28_,for,errordescription%29.md)
  This method is not supported for the `NSEnergyFormatter` class.
- [var numberFormatter: NumberFormatter!](./numberformatter.md)
  The number formatter used to format the numbers in energy strings.
- [func string(fromJoules: Double) -> String](./string%28fromjoules%29.md)
  Returns an energy string for the provided value.
- [func string(fromValue: Double, unit: EnergyFormatter.Unit) -> String](./string%28fromvalue,unit%29.md)
  Returns a properly formatted energy string for the given value and unit.
- [func unitString(fromJoules: Double, usedUnit: UnsafeMutablePointer<EnergyFormatter.Unit>?) -> String](./unitstring%28fromjoules,usedunit%29.md)
  Returns the unit string for the provided value.
- [func unitString(fromValue: Double, unit: EnergyFormatter.Unit) -> String](./unitstring%28fromvalue,unit%29.md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](./unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/energyformatter/isforfoodenergyuse)*