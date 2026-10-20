# isForPersonHeightUse

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (getter=isForPersonHeightUse) BOOL forPersonHeightUse;
```

#### Discussion

Returns [`true`](../../Swift/true.md) if the value passed to [`string(fromMeters:)`](./string%28frommeters%29.md) or [`unitString(fromMeters:usedUnit:)`](./unitstring%28frommeters,usedunit%29.md) is a person’s height; otherwise, [`false`](../../Swift/false.md). By default, this property returns [`false`](../../Swift/false.md).

The length formatter uses this property when determining the best unit for a given locale (for example, in the [`string(fromMeters:)`](./string%28frommeters%29.md) method).

## See Also

### Formatting Length Strings
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
- [func unitString(fromValue: Double, unit: LengthFormatter.Unit) -> String](./unitstring%28fromvalue,unit%29.md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](./unitstyle.md)
  The unit style used by this formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/lengthformatter/isforpersonheightuse)*