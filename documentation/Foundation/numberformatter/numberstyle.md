# numberStyle

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number style used by the receiver.

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
var numberStyle: NumberFormatter.Style { get set }
```

```objc
@property NSNumberFormatterStyle numberStyle;
```

## Discussion

Styles are essentially predetermined sets of values for certain properties. Examples of number-formatter styles are those used for decimal values, percentage values, and currency.

## See Also

### Configuring Formatter Behavior and Style
- [var formatterBehavior: NumberFormatter.Behavior](./formatterbehavior.md)
  The formatter behavior of the receiver.
- [class func setDefaultFormatterBehavior(NumberFormatter.Behavior)](./setdefaultformatterbehavior%28_%29.md)
  Sets the default formatter behavior for new instances of `NSNumberFormatter` .
- [class func defaultFormatterBehavior() -> NumberFormatter.Behavior](./defaultformatterbehavior%28%29.md)
  Returns an `NSNumberFormatterBehavior` constant that indicates default formatter behavior for new instances of `NSNumberFormatter`.
- [var generatesDecimalNumbers: Bool](./generatesdecimalnumbers.md)
  Determines whether the receiver creates instances of [`NSDecimalNumber`](../nsdecimalnumber.md) when it converts strings to number objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/numberstyle)*