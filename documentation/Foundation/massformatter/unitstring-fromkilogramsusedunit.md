# unitString(fromKilograms:usedUnit:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

A localized string representing the unit.

#### Discussion

This method selects the correct unit based on the formatter’s locale, the magnitude of the value, and the [`isForPersonMassUse`](massformatter/isforpersonmassuse.md) property. The value, once converted into the appropriate unit, determines whether the unit string is plural or singular.

## Parameters

- `numberInKilograms`: The mass’s value in kilograms.
- `unitp`: An output parameter. This will hold the   value that corresponds to the returned units.

## See Also

- [var isForPersonMassUse: Bool](massformatter/isforpersonmassuse.md)
  A Boolean value that indicates whether the resulting string represents a person’s mass.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](massformatter/getobjectvalue(_:for:errordescription:).md)
  This method is not supported for the `NSMassFormatter` class.
- [var numberFormatter: NumberFormatter!](massformatter/numberformatter.md)
  The number formatter used to format the numbers in a mass strings.
- [func string(fromKilograms: Double) -> String](massformatter/string(fromkilograms:).md)
  Returns a mass string for the provided value.
- [func string(fromValue: Double, unit: MassFormatter.Unit) -> String](massformatter/string(fromvalue:unit:).md)
  Returns a properly formatted mass string for the given value and unit.
- [func unitString(fromValue: Double, unit: MassFormatter.Unit) -> String](massformatter/unitstring(fromvalue:unit:).md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](massformatter/unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/massformatter/unitstring(fromkilograms:usedunit:))*