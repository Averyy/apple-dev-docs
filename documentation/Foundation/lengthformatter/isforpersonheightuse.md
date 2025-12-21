# isForPersonHeightUse

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the resulting string represents a person’s height.

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
var isForPersonHeightUse: Bool { get set }
```

#### Discussion

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the value passed to [`string(fromMeters:)`](lengthformatter/string(frommeters:).md) or [`unitString(fromMeters:usedUnit:)`](lengthformatter/unitstring(frommeters:usedunit:).md) is a person’s height; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). By default, this property returns [`false`](https://developer.apple.com/documentation/Swift/false).

The length formatter uses this property when determining the best unit for a given locale (for example, in the [`string(fromMeters:)`](lengthformatter/string(frommeters:).md) method).

## See Also

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
- [func unitString(fromValue: Double, unit: LengthFormatter.Unit) -> String](lengthformatter/unitstring(fromvalue:unit:).md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](lengthformatter/unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/lengthformatter/isforpersonheightuse)*