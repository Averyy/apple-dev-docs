# unitString(fromValue:unit:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

A localized string representing the given unit. The provided value determines whether the unit is plural or singular.

## Parameters

- `value`: The length’s value for the provided unit.
- `unit`: The unit to use in the resulting length string.

## See Also

- [var isForPersonHeightUse: Bool](lengthformatter/isforpersonheightuse.md)
  A Boolean value that indicates whether the resulting string represents a person’s height.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](lengthformatter/getobjectvalue(_:for:errordescription:).md)
  This method is not supported for the `NSLengthFormatter` class.
- [var numberFormatter: NumberFormatter!](lengthformatter/numberformatter.md)
  The number formatter used to format the numbers in length strings.
- [func string(fromMeters: Double) -> String](lengthformatter/string(frommeters:).md)
  Returns a length string for the provided value.
- [func string(fromValue: Double, unit: LengthFormatter.Unit) -> String](lengthformatter/string(fromvalue:unit:).md)
  Returns a properly formatted length string for the given value and unit.
- [func unitString(fromMeters: Double, usedUnit: UnsafeMutablePointer<LengthFormatter.Unit>?) -> String](lengthformatter/unitstring(frommeters:usedunit:).md)
  Returns the unit string for the provided value.
- [var unitStyle: Formatter.UnitStyle](lengthformatter/unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/lengthformatter/unitstring(fromvalue:unit:))*