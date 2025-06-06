# baseUnitValue(fromValue:)

**Framework**: Foundation  
**Kind**: method

For a given unit, returns the specified value of that unit in terms of the base unit of its dimension.

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
func baseUnitValue(fromValue value: Double) -> Double
```

#### Return Value

The value in terms of the base unit.

#### Discussion

This method takes a value in a particular unit and returns the result of converting it into the base unit of that unit’s dimension. For example, a converter for the miles unit calling this method, passing `1.0` to the `value` parameter, results in `1609.34` ().

## Parameters

- `value`: The value in terms of a given unit.

## See Also

- [func value(fromBaseUnitValue: Double) -> Double](unitconverter/value(frombaseunitvalue:).md)
  For a given unit, returns the specified value of the base unit in terms of that unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitconverter/baseunitvalue(fromvalue:))*