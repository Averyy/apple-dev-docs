# attributedStringForZero

**Framework**: Foundation  
**Kind**: property

The attributed string that the receiver uses to display zero values.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@NSCopying
var attributedStringForZero: NSAttributedString { get set }
```

#### Discussion

By default zero values are displayed according to the format specified for positive values; for more discussion of this subject see [`Data Formatting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

##### Special Considerations

This method is for use with formatters using `NSNumberFormatterBehavior10_0` behavior.

## See Also

- [var textAttributesForNegativeValues: [String : Any]?](numberformatter/textattributesfornegativevalues.md)
  The text attributes to be used in displaying negative values.
- [var textAttributesForPositiveValues: [String : Any]?](numberformatter/textattributesforpositivevalues.md)
  The text attributes to be used in displaying positive values.
- [var textAttributesForZero: [String : Any]?](numberformatter/textattributesforzero.md)
  The text attributes used to display a zero value.
- [var attributedStringForNil: NSAttributedString](numberformatter/attributedstringfornil.md)
  The attributed string the receiver uses to display `nil` values.
- [var textAttributesForNil: [String : Any]?](numberformatter/textattributesfornil.md)
  The text attributes used to display the `nil` symbol.
- [var attributedStringForNotANumber: NSAttributedString](numberformatter/attributedstringfornotanumber.md)
  The attributed string the receiver uses to display “not a number” values.
- [var textAttributesForNotANumber: [String : Any]?](numberformatter/textattributesfornotanumber.md)
  The text attributes used to display the NaN (“not a number”) string.
- [var textAttributesForPositiveInfinity: [String : Any]?](numberformatter/textattributesforpositiveinfinity.md)
  The text attributes used to display the positive infinity symbol.
- [var textAttributesForNegativeInfinity: [String : Any]?](numberformatter/textattributesfornegativeinfinity.md)
  The text attributes used to display the negative infinity symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/attributedstringforzero)*