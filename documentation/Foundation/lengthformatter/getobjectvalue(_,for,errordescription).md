# getObjectValue(_:for:errorDescription:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) getObjectValue:(id*) obj forString:(NSString *) string errorDescription:(NSString **) error;
```

## Return Value

[`true`](../../Swift/true.md) if the conversion from string was successful; otherwise, [`false`](../../Swift/false.md).

## Discussion

You can override this method in a subclass. For more information, see [`Formatter`](../formatter.md).

## Parameters

- `obj`: An output parameter. If overridden, this parameter should contain the object created from the provided string.
- `string`: A string representation of the object.
- `error`: An output parameter. If overridden, this parameter should contain a description of any errors that occur. If you do not want to receive error messages, set this parameter to `NULL`.

## See Also

### Related Documentation
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](../formatter/getobjectvalue%28_,for,errordescription%29.md)
  The default implementation of this method raises an exception.
### Formatting Length Strings
- [var isForPersonHeightUse: Bool](./isforpersonheightuse.md)
  A Boolean value that indicates whether the resulting string represents a person’s height.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/lengthformatter/getobjectvalue(_:for:errordescription:))*