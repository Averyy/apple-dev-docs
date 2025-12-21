# NumberFormatter.Behavior

**Framework**: Foundation  
**Kind**: enum

These constants specify the behavior of a number formatter. These constants are returned by the [`defaultFormatterBehavior()`](numberformatter/defaultformatterbehavior().md) class method and the [`formatterBehavior`](numberformatter/formatterbehavior.md) property.

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
enum Behavior
```

## Topics

### Constants
- [NumberFormatter.Behavior.default](numberformatter/behavior/default.md)
  The number-formatter behavior set as the default for new instances. You can set the default formatter behavior with the class method [`setDefaultFormatterBehavior(_:)`](numberformatter/setdefaultformatterbehavior(_:).md).
- [NumberFormatter.Behavior.behavior10_0](numberformatter/behavior/behavior10_0.md)
  The number-formatter behavior as it existed prior to macOS 10.4.
- [NumberFormatter.Behavior.behavior10_4](numberformatter/behavior/behavior10_4.md)
  The number-formatter behavior since macOS 10.4.
### Initializers
- [init?(rawValue: UInt)](numberformatter/behavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NumberFormatter.Style](numberformatter/style.md)
  The predefined number format styles used by the [`numberStyle`](numberformatter/numberstyle.md) property.
- [NumberFormatter.PadPosition](numberformatter/padposition.md)
  These constants are used to specify how numbers should be padded. These constants are used by the [`paddingPosition`](numberformatter/paddingposition.md) property.
- [NumberFormatter.RoundingMode](numberformatter/roundingmode-swift.enum.md)
  These constants are used to specify how numbers should be rounded. These constants are used by the [`roundingMode`](numberformatter/roundingmode-swift.property.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/behavior)*