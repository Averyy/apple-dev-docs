# unitStyle

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The unit style used by this formatter.

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
var unitStyle: Formatter.UnitStyle { get set }
```

```objc
@property NSFormattingUnitStyle unitStyle;
```

#### Discussion

This property defaults to [`Formatter.UnitStyle.medium`](../formatter/unitstyle/medium.md). For a complete list of unit styles, see [`Formatter.UnitStyle`](../formatter/unitstyle.md).

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
- [func unitString(fromKilograms: Double, usedUnit: UnsafeMutablePointer<MassFormatter.Unit>?) -> String](./unitstring%28fromkilograms,usedunit%29.md)
  Returns the unit string for the provided value.
- [func unitString(fromValue: Double, unit: MassFormatter.Unit) -> String](./unitstring%28fromvalue,unit%29.md)
  Returns the unit string based on the provided value and unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/massformatter/unitstyle)*