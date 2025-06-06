# init(allowedUnits:width:maximumUnitCount:zeroValueUnits:valueLengthLimits:fractionalPart:)

**Framework**: Swift  
**Kind**: init

Creates a units format style using the given parameters.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init<ValueRange>(allowedUnits: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int? = nil, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy = .hide, valueLengthLimits: ValueRange, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy = .hide) where ValueRange : RangeExpression, ValueRange.Bound == Int
```

#### Discussion

Use this convenience function in situations that expect a [`Duration.UnitsFormatStyle`](duration/unitsformatstyle.md), such as [`formatted(_:)`](duration/formatted(_:).md), as an alternative to using the full initializer.

## Parameters

- `allowedUnits`: The units that the formatted string may include.
- `width`: The width of the unit and the spacing between the value and the unit.
- `maximumUnitCount`: The maximum number of duration units to include in the output string.
- `zeroValueUnits`: The strategy for handling leading units with zero values.
- `valueLengthLimits`: The padding or truncating behavior of the unit value, as a bounded range of   values.
- `fractionalPart`: The strategy for displaying a duration if a formatted string can’t represent it exactly with the allowed units.

## See Also

- [init(allowedUnits: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int?, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy, valueLength: Int?, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy)](duration/unitsformatstyle/init(allowedunits:width:maximumunitcount:zerovalueunits:valuelength:fractionalpart:).md)
  Creates a units format style using the given parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/init(allowedunits:width:maximumunitcount:zerovalueunits:valuelengthlimits:fractionalpart:))*