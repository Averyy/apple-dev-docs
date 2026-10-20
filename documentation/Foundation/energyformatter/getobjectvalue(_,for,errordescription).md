# getObjectValue(_:for:errorDescription:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

This method is not supported for the `NSEnergyFormatter` class.

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
func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>?, for string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

```objc
- (BOOL) getObjectValue:(id*) obj forString:(NSString *) string errorDescription:(NSString **) error;
```

#### Return Value

[`true`](../../Swift/true.md) if the conversion from string was successful; otherwise, [`false`](../../Swift/false.md).

#### Discussion

You can override this method in a subclass. For more information, see [`Formatter`](../formatter.md).

## Parameters

- `obj`: An output parameter. If overridden, this parameter should contain the object created from the provided string.
- `string`: A string representation of the object.
- `error`: An output parameter. If overridden, this parameter should contain a description of any errors that occur. If you do not want to receive error messages, set this parameter to `NULL`.

## See Also

### Related Documentation
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](../formatter/getobjectvalue%28_,for,errordescription%29.md)
  The default implementation of this method raises an exception.
### Formatting Energy Strings
- [var isForFoodEnergyUse: Bool](./isforfoodenergyuse.md)
  A Boolean value that indicates whether the energy value is used to measure food energy.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/energyformatter/getobjectvalue(_:for:errordescription:))*