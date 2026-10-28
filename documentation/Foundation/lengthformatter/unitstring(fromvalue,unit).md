# unitString(fromValue:unit:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the unit string based on the provided value and unit.

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
func unitString(fromValue value: Double, unit: LengthFormatter.Unit) -> String
```

```objc
- (NSString *) unitStringFromValue:(double) value unit:(NSLengthFormatterUnit) unit;
```

## Return Value

A localized string representing the given unit. The provided value determines whether the unit is plural or singular.

## Parameters

- `value`: The length’s value for the provided unit.
- `unit`: The unit to use in the resulting length string.

## See Also

### Formatting Length Strings
- [var isForPersonHeightUse: Bool](./isforpersonheightuse.md)
  A Boolean value that indicates whether the resulting string represents a person’s height.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getobjectvalue%28_,for,errordescription%29.md)
  This method is not supported for the `NSLengthFormatter` class.
- [var numberFormatter: NumberFormatter!](./numberformatter.md)
  The number formatter used to format the numbers in length strings.
- [func string(fromMeters: Double) -> String](./string%28frommeters%29.md)
  Returns a length string for the provided value.
- [func string(fromValue: Double, unit: LengthFormatter.Unit) -> String](./string%28fromvalue,unit%29.md)
  Returns a properly formatted length string for the given value and unit.
- [func unitString(fromMeters: Double, usedUnit: UnsafeMutablePointer<LengthFormatter.Unit>?) -> String](./unitstring%28frommeters,usedunit%29.md)
  Returns the unit string for the provided value.
- [var unitStyle: Formatter.UnitStyle](./unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/lengthformatter/unitstring(fromvalue:unit:))*