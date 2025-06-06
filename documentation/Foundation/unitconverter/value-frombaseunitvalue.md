# value(fromBaseUnitValue:)

**Framework**: Foundation  
**Kind**: method

For a given unit, returns the specified value of the base unit in terms of that unit.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func value(fromBaseUnitValue baseUnitValue: Double) -> Double
```

#### Return Value

The value in terms of a given unit.

#### Discussion

This method takes a value in the base unit of a unit’s dimension and returns the result of converting it into that unit. For example, a converter for the pounds unit calling this method, passing `2.20462` to the `baseUnitValue` parameter, results in `1.0` ().

## Parameters

- `baseUnitValue`: The value in terms of the base unit.

## See Also

- [func baseUnitValue(fromValue: Double) -> Double](unitconverter/baseunitvalue(fromvalue:).md)
  For a given unit, returns the specified value of that unit in terms of the base unit of its dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitconverter/value(frombaseunitvalue:))*