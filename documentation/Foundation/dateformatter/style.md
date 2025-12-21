# DateFormatter.Style

**Framework**: Foundation  
**Kind**: enum

The following constants specify predefined format styles for dates and times.

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
enum Style
```

#### Overview

The format for these date and time styles is not exact because they depend on the locale, user preference settings, and the operating system version. Do not use these constants if you want an exact format.

## Topics

### Constants
- [DateFormatter.Style.none](dateformatter/style/none.md)
- [DateFormatter.Style.short](dateformatter/style/short.md)
- [DateFormatter.Style.medium](dateformatter/style/medium.md)
- [DateFormatter.Style.long](dateformatter/style/long.md)
- [DateFormatter.Style.full](dateformatter/style/full.md)
### Initializers
- [init?(rawValue: UInt)](dateformatter/style/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DateFormatter.Behavior](dateformatter/behavior.md)
  Constants that specify the behavior `NSDateFormatter` should exhibit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/style)*