# textAttributesForZero

**Framework**: Foundation  
**Kind**: property

The text attributes used to display a zero value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var textAttributesForZero: [String : Any]? { get set }
```

#### Discussion

This property is a dictionary that contains the text attributes used to display zero values.

## See Also

- [var textAttributesForNegativeValues: [String : Any]?](numberformatter/textattributesfornegativevalues.md)
  The text attributes to be used in displaying negative values.
- [var textAttributesForPositiveValues: [String : Any]?](numberformatter/textattributesforpositivevalues.md)
  The text attributes to be used in displaying positive values.
- [var attributedStringForZero: NSAttributedString](numberformatter/attributedstringforzero.md)
  The attributed string that the receiver uses to display zero values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/textattributesforzero)*