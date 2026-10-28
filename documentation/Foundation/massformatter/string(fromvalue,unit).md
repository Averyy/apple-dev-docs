# string(fromValue:unit:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a properly formatted mass string for the given value and unit.

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
func string(fromValue value: Double, unit: MassFormatter.Unit) -> String
```

```objc
- (NSString *) stringFromValue:(double) value unit:(NSMassFormatterUnit) unit;
```

## Return Value

A localized string that combines the provided value and unit.

## Parameters

- `value`: The mass’s value in the given unit.
- `unit`: The unit used in the resulting mass string.

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
- [func unitString(fromKilograms: Double, usedUnit: UnsafeMutablePointer<MassFormatter.Unit>?) -> String](./unitstring%28fromkilograms,usedunit%29.md)
  Returns the unit string for the provided value.
- [func unitString(fromValue: Double, unit: MassFormatter.Unit) -> String](./unitstring%28fromvalue,unit%29.md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](./unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/massformatter/string(fromvalue:unit:))*