# attributedStringForNil

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The attributed string the receiver uses to display `nil` values.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@NSCopying
var attributedStringForNil: NSAttributedString { get set }
```

```objc
@property (copy) NSAttributedString * attributedStringForNil;
```

#### Discussion

By default `nil` values are displayed as an empty string.

##### Special Considerations

This method is for use with formatters using `NSNumberFormatterBehavior10_0` behavior.

## See Also

### Configuring the Display of Numeric Values
- [var textAttributesForNegativeValues: [String : Any]?](./textattributesfornegativevalues.md)
  The text attributes to be used in displaying negative values.
- [var textAttributesForPositiveValues: [String : Any]?](./textattributesforpositivevalues.md)
  The text attributes to be used in displaying positive values.
- [var attributedStringForZero: NSAttributedString](./attributedstringforzero.md)
  The attributed string that the receiver uses to display zero values.
- [var textAttributesForZero: [String : Any]?](./textattributesforzero.md)
  The text attributes used to display a zero value.
- [var textAttributesForNil: [String : Any]?](./textattributesfornil.md)
  The text attributes used to display the `nil` symbol.
- [var attributedStringForNotANumber: NSAttributedString](./attributedstringfornotanumber.md)
  The attributed string the receiver uses to display “not a number” values.
- [var textAttributesForNotANumber: [String : Any]?](./textattributesfornotanumber.md)
  The text attributes used to display the NaN (“not a number”) string.
- [var textAttributesForPositiveInfinity: [String : Any]?](./textattributesforpositiveinfinity.md)
  The text attributes used to display the positive infinity symbol.
- [var textAttributesForNegativeInfinity: [String : Any]?](./textattributesfornegativeinfinity.md)
  The text attributes used to display the negative infinity symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/attributedstringfornil)*