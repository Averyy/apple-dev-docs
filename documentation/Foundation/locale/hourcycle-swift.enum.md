# Locale.HourCycle

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum HourCycle
```

## Topics

### Using defined hour cycles
- [Locale.HourCycle.zeroToEleven](./hourcycle-swift.enum/zerotoeleven.md)
  A twelve hour cycle, counted from 0 to 11.
- [Locale.HourCycle.oneToTwelve](./hourcycle-swift.enum/onetotwelve.md)
  A twelve hour cycle, counted from 1 to 12.
- [Locale.HourCycle.zeroToTwentyThree](./hourcycle-swift.enum/zerototwentythree.md)
  A twenty-four hour cycle, counted from 0 to 23.
- [Locale.HourCycle.oneToTwentyFour](./hourcycle-swift.enum/onetotwentyfour.md)
  A twenty-four hour cycle, counted from 1 to 24.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting date and time components
- [var firstDayOfWeek: Locale.Weekday](./firstdayofweek.md)
  The first day of the week as represented by this locale.
- [Locale.Weekday](./weekday.md)
  A type that represents weekdays, used for indicating a locale’s first day of the week.
- [var hourCycle: Locale.HourCycle](./hourcycle-swift.property.md)
  The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone associated with the locale, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/hourcycle-swift.enum)*