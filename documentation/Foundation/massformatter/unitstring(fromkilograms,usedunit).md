# unitString(fromKilograms:usedUnit:)

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
func unitString(fromKilograms numberInKilograms: Double, usedUnit unitp: UnsafeMutablePointer<MassFormatter.Unit>?) -> String
```

```objc
- (NSString *) unitStringFromKilograms:(double) numberInKilograms usedUnit:(NSMassFormatterUnit *) unitp;
```

## Return Value

A localized string representing the unit.

## Discussion

This method selects the correct unit based on the formatter’s locale, the magnitude of the value, and the [`isForPersonMassUse`](./isforpersonmassuse.md) property. The value, once converted into the appropriate unit, determines whether the unit string is plural or singular.

## Parameters

- `numberInKilograms`: The mass’s value in kilograms.
- `unitp`: An output parameter. This will hold the [`MassFormatter.Unit`](./unit.md) value that corresponds to the returned units.

## See Also

### Formatting Mass Strings
- [var isForPersonMassUse: Bool](./isforpersonmassuse.md)
  A Boolean value that indicates whether the resulting string represents a person’s mass.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getobjectvalue%28_,for,errordescription%29.md)
  This method is not supported for the `NSMassFormatter` class.
- [var numberFormatter: NumberFormatter!](./numberformatter.md)
  The number formatter used to format the numbers in a mass strings.
- [func string(fromKilograms: Double) -> String](./string%28fromkilograms%29.md)
  Returns a mass string for the provided value.
- [func string(fromValue: Double, unit: MassFormatter.Unit) -> String](./string%28fromvalue,unit%29.md)
  Returns a properly formatted mass string for the given value and unit.
- [func unitString(fromValue: Double, unit: MassFormatter.Unit) -> String](./unitstring%28fromvalue,unit%29.md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](./unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/massformatter/unitstring(fromkilograms:usedunit:))*