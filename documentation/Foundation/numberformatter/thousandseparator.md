# thousandSeparator

**Framework**: Foundation  
**Kind**: property

The character the receiver uses as a thousand separator.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var thousandSeparator: String! { get set }
```

#### Discussion

If you don’t have thousand separators enabled through any other means (such as [`format`](numberformatter/format.md)), using this method enables them.

##### Special Considerations

This method is for use with formatters using `NSNumberFormatterBehavior10_0` behavior.

## See Also

- [var groupingSeparator: String!](numberformatter/groupingseparator.md)
  The string used by the receiver for a grouping separator.
- [var usesGroupingSeparator: Bool](numberformatter/usesgroupingseparator.md)
  Determines whether the receiver displays the group separator.
- [var hasThousandSeparators: Bool](numberformatter/hasthousandseparators.md)
  Determines whether the receiver uses thousand separators.
- [var decimalSeparator: String!](numberformatter/decimalseparator.md)
  The character the receiver uses as a decimal separator.
- [var alwaysShowsDecimalSeparator: Bool](numberformatter/alwaysshowsdecimalseparator.md)
  Determines whether the receiver always shows the decimal separator, even for integer numbers.
- [var currencyDecimalSeparator: String!](numberformatter/currencydecimalseparator.md)
  The string used by the receiver as a currency decimal separator.
- [var groupingSize: Int](numberformatter/groupingsize.md)
  The grouping size of the receiver.
- [var secondaryGroupingSize: Int](numberformatter/secondarygroupingsize.md)
  The secondary grouping size of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/thousandseparator)*