# formatterBehavior

**Framework**: Foundation  
**Kind**: property

The formatter behavior of the receiver.

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
var formatterBehavior: NumberFormatter.Behavior { get set }
```

## See Also

- [Data Formatting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)
- [class func setDefaultFormatterBehavior(NumberFormatter.Behavior)](numberformatter/setdefaultformatterbehavior(_:).md)
  Sets the default formatter behavior for new instances of `NSNumberFormatter` .
- [class func defaultFormatterBehavior() -> NumberFormatter.Behavior](numberformatter/defaultformatterbehavior.md)
  Returns an `NSNumberFormatterBehavior` constant that indicates default formatter behavior for new instances of `NSNumberFormatter`.
- [var numberStyle: NumberFormatter.Style](numberformatter/numberstyle.md)
  The number style used by the receiver.
- [var generatesDecimalNumbers: Bool](numberformatter/generatesdecimalnumbers.md)
  Determines whether the receiver creates instances of [`NSDecimalNumber`](nsdecimalnumber.md) when it converts strings to number objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/formatterbehavior)*