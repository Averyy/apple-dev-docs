# textAttributesForNotANumber

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The text attributes used to display the NaN (“not a number”) string.

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
var textAttributesForNotANumber: [String : Any]? { get set }
```

```objc
@property (copy, nullable) NSDictionary<NSString *,id> * textAttributesForNotANumber;
```

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
- [var attributedStringForNil: NSAttributedString](./attributedstringfornil.md)
  The attributed string the receiver uses to display `nil` values.
- [var textAttributesForNil: [String : Any]?](./textattributesfornil.md)
  The text attributes used to display the `nil` symbol.
- [var attributedStringForNotANumber: NSAttributedString](./attributedstringfornotanumber.md)
  The attributed string the receiver uses to display “not a number” values.
- [var textAttributesForPositiveInfinity: [String : Any]?](./textattributesforpositiveinfinity.md)
  The text attributes used to display the positive infinity symbol.
- [var textAttributesForNegativeInfinity: [String : Any]?](./textattributesfornegativeinfinity.md)
  The text attributes used to display the negative infinity symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/textattributesfornotanumber)*