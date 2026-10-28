# numberFormatter

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number formatter used to format the numbers in length strings.

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
@NSCopying
var numberFormatter: NumberFormatter! { get set }
```

```objc
@property (copy, null_resettable) NSNumberFormatter * numberFormatter;
```

## Discussion

This property defaults to a number formatter using the [`NumberFormatter.Style.decimal`](../numberformatter/style/decimal.md). You can provide a different number formatter to customize the length string’s appearance.

## See Also

### Formatting Length Strings
- [var isForPersonHeightUse: Bool](./isforpersonheightuse.md)
  A Boolean value that indicates whether the resulting string represents a person’s height.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getobjectvalue%28_,for,errordescription%29.md)
  This method is not supported for the `NSLengthFormatter` class.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/lengthformatter/numberformatter)*