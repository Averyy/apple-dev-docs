# DateFormatter.Style

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSDateFormatterStyle : NSUInteger;
```

#### Overview

The format for these date and time styles is not exact because they depend on the locale, user preference settings, and the operating system version. Do not use these constants if you want an exact format.

## Topics

### Constants
- [DateFormatter.Style.none](./style/none.md)
- [DateFormatter.Style.short](./style/short.md)
- [DateFormatter.Style.medium](./style/medium.md)
- [DateFormatter.Style.long](./style/long.md)
- [DateFormatter.Style.full](./style/full.md)
### Initializers
- [init?(rawValue: UInt)](./style/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [DateFormatter.Behavior](./behavior.md)
  Constants that specify the behavior `NSDateFormatter` should exhibit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/style)*