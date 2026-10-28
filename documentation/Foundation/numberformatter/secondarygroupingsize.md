# secondaryGroupingSize

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The secondary grouping size of the receiver.

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
var secondaryGroupingSize: Int { get set }
```

```objc
@property NSUInteger secondaryGroupingSize;
```

## Discussion

Some locales allow the specification of another grouping size for larger numbers. For example, some locales may represent a number such as 61, 242, 378.46 (as in the United States) as 6,12,42,378.46. In this case, the secondary grouping size (covering the groups of digits furthest from the decimal point) is 2.

## See Also

### Configuring Separators and Grouping Size
- [var groupingSeparator: String!](./groupingseparator.md)
  The string used by the receiver for a grouping separator.
- [var usesGroupingSeparator: Bool](./usesgroupingseparator.md)
  Determines whether the receiver displays the group separator.
- [var thousandSeparator: String!](./thousandseparator.md)
  The character the receiver uses as a thousand separator.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/secondarygroupingsize)*