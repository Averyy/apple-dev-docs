# thousandSeparator

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The character the receiver uses as a thousand separator.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var thousandSeparator: String! { get set }
```

```objc
@property (copy, null_resettable) NSString * thousandSeparator;
```

## Discussion

If you don’t have thousand separators enabled through any other means (such as [`format`](./format.md)), using this method enables them.

### Special Considerations

This method is for use with formatters using `NSNumberFormatterBehavior10_0` behavior.

## See Also

### Configuring Separators and Grouping Size
- [var groupingSeparator: String!](./groupingseparator.md)
  The string used by the receiver for a grouping separator.
- [var usesGroupingSeparator: Bool](./usesgroupingseparator.md)
  Determines whether the receiver displays the group separator.
- [var hasThousandSeparators: Bool](./hasthousandseparators.md)
  Determines whether the receiver uses thousand separators.
- [var decimalSeparator: String!](./decimalseparator.md)
  The character the receiver uses as a decimal separator.
- [var alwaysShowsDecimalSeparator: Bool](./alwaysshowsdecimalseparator.md)
  Determines whether the receiver always shows the decimal separator, even for integer numbers.
- [var currencyDecimalSeparator: String!](./currencydecimalseparator.md)
  The string used by the receiver as a currency decimal separator.
- [var groupingSize: Int](./groupingsize.md)
  The grouping size of the receiver.
- [var secondaryGroupingSize: Int](./secondarygroupingsize.md)
  The secondary grouping size of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/thousandseparator)*