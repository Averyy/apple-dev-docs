# string(fromKilograms:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a mass string for the provided value.

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
func string(fromKilograms numberInKilograms: Double) -> String
```

```objc
- (NSString *) stringFromKilograms:(double) numberInKilograms;
```

## Return Value

A string that combines a value and a unit string appropriate for the formatter’s locale.

## Discussion

This method converts the provided mass in kilograms into units appropriate for the formatter’s locale.

## Parameters

- `numberInKilograms`: The mass’s value in kilograms.

## See Also

### Formatting Mass Strings
- [var isForPersonMassUse: Bool](./isforpersonmassuse.md)
  A Boolean value that indicates whether the resulting string represents a person’s mass.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getobjectvalue%28_,for,errordescription%29.md)
  This method is not supported for the `NSMassFormatter` class.
- [var numberFormatter: NumberFormatter!](./numberformatter.md)
  The number formatter used to format the numbers in a mass strings.
- [func string(fromValue: Double, unit: MassFormatter.Unit) -> String](./string%28fromvalue,unit%29.md)
  Returns a properly formatted mass string for the given value and unit.
- [func unitString(fromKilograms: Double, usedUnit: UnsafeMutablePointer<MassFormatter.Unit>?) -> String](./unitstring%28fromkilograms,usedunit%29.md)
  Returns the unit string for the provided value.
- [func unitString(fromValue: Double, unit: MassFormatter.Unit) -> String](./unitstring%28fromvalue,unit%29.md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](./unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/massformatter/string(fromkilograms:))*