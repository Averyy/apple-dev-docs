# complete

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A time style with all components represented.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let complete: Date.FormatStyle.TimeStyle
```

#### Discussion

A `complete` time style represents the hour, minute, second, day period, and time zone components in the format. For example, `9:54:29 PM CDT`, ``for locale `en_US`.

## See Also

### Modifying a Time Style
- [static let omitted: Date.FormatStyle.TimeStyle](./omitted.md)
  A time style with no time-related components represented.
- [static let shortened: Date.FormatStyle.TimeStyle](./shortened.md)
  A shortened time style with only the hour, minute, and day period components represented.
- [static let standard: Date.FormatStyle.TimeStyle](./standard.md)
  A time style with all components except the time zone represented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/timestyle/complete)*