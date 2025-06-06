# setDefaultFormatterBehavior(_:)

**Framework**: Foundation  
**Kind**: method

Sets the default formatter behavior for new instances of `NSNumberFormatter` .

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
class func setDefaultFormatterBehavior(_ behavior: NumberFormatter.Behavior)
```

## Parameters

- `behavior`: An   constant that indicates the revision of the class providing the default behavior.

## See Also

- [var formatterBehavior: NumberFormatter.Behavior](numberformatter/formatterbehavior.md)
  The formatter behavior of the receiver.
- [class func defaultFormatterBehavior() -> NumberFormatter.Behavior](numberformatter/defaultformatterbehavior.md)
  Returns an `NSNumberFormatterBehavior` constant that indicates default formatter behavior for new instances of `NSNumberFormatter`.
- [var numberStyle: NumberFormatter.Style](numberformatter/numberstyle.md)
  The number style used by the receiver.
- [var generatesDecimalNumbers: Bool](numberformatter/generatesdecimalnumbers.md)
  Determines whether the receiver creates instances of [`NSDecimalNumber`](nsdecimalnumber.md) when it converts strings to number objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/setdefaultformatterbehavior(_:))*