# string(fromValue:unit:)

**Framework**: Foundation  
**Kind**: method

Returns a properly formatted length string for the given value and unit.

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
func string(fromValue value: Double, unit: LengthFormatter.Unit) -> String
```

#### Return Value

A localized string that combines the provided value and unit.

## Parameters

- `value`: The length’s value in the given unit.
- `unit`: The unit used in the resulting length string.

## See Also

- [var isForPersonHeightUse: Bool](lengthformatter/isforpersonheightuse.md)
  A Boolean value that indicates whether the resulting string represents a person’s height.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](lengthformatter/getobjectvalue(_:for:errordescription:).md)
  This method is not supported for the `NSLengthFormatter` class.
- [var numberFormatter: NumberFormatter!](lengthformatter/numberformatter.md)
  The number formatter used to format the numbers in length strings.
- [func string(fromMeters: Double) -> String](lengthformatter/string(frommeters:).md)
  Returns a length string for the provided value.
- [func unitString(fromMeters: Double, usedUnit: UnsafeMutablePointer<LengthFormatter.Unit>?) -> String](lengthformatter/unitstring(frommeters:usedunit:).md)
  Returns the unit string for the provided value.
- [func unitString(fromValue: Double, unit: LengthFormatter.Unit) -> String](lengthformatter/unitstring(fromvalue:unit:).md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](lengthformatter/unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/lengthformatter/string(fromvalue:unit:))*