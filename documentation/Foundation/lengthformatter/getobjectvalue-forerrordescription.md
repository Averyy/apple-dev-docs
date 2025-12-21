# getObjectValue(_:for:errorDescription:)

**Framework**: Foundation  
**Kind**: method

This method is not supported for the `NSLengthFormatter` class.

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

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the conversion from string was successful; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

You can override this method in a subclass. For more information, see [`Formatter`](formatter.md).

## Parameters

- `obj`: An output parameter. If overridden, this parameter should contain the object created from the provided string.
- `string`: A string representation of the object.
- `error`: An output parameter. If overridden, this parameter should contain a description of any errors that occur. If you do not want to receive error messages, set this parameter to  .

## See Also

- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](formatter/getobjectvalue(_:for:errordescription:).md)
  The default implementation of this method raises an exception.
- [var isForPersonHeightUse: Bool](lengthformatter/isforpersonheightuse.md)
  A Boolean value that indicates whether the resulting string represents a person’s height.
- [var numberFormatter: NumberFormatter!](lengthformatter/numberformatter.md)
  The number formatter used to format the numbers in length strings.
- [func string(fromMeters: Double) -> String](lengthformatter/string(frommeters:).md)
  Returns a length string for the provided value.
- [func string(fromValue: Double, unit: LengthFormatter.Unit) -> String](lengthformatter/string(fromvalue:unit:).md)
  Returns a properly formatted length string for the given value and unit.
- [func unitString(fromMeters: Double, usedUnit: UnsafeMutablePointer<LengthFormatter.Unit>?) -> String](lengthformatter/unitstring(frommeters:usedunit:).md)
  Returns the unit string for the provided value.
- [func unitString(fromValue: Double, unit: LengthFormatter.Unit) -> String](lengthformatter/unitstring(fromvalue:unit:).md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](lengthformatter/unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/lengthformatter/getobjectvalue(_:for:errordescription:))*