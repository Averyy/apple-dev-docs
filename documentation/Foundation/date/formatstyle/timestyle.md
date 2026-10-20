# Date.FormatStyle.TimeStyle

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Type that defines time styles varied in length or components included.

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
struct TimeStyle
```

#### Overview

The exact format depends on the locale. Possible time styles include [`omitted`](./timestyle/omitted.md), [`shortened`](./timestyle/shortened.md), [`standard`](./timestyle/standard.md), and [`complete`](./timestyle/complete.md).

The following code sample shows a variety of time style format results using the `en_US` locale.

```swift
let meetingDate = Date()
meetingDate.formatted(date: .numeric, time: .omitted)
// 10/17/2020
 
meetingDate.formatted(date: .numeric, time: .shortened)
// 10/17/2020, 9:54 PM
 
meetingDate.formatted(date: .numeric, time: .standard)
// 10/17/2020, 9:54:29 PM
 
meetingDate.formatted(date: .numeric, time: .complete)
// 10/17/2020, 9:54:29 PM CDT

meetingDate.formatted()
// 10/17/2020, 9:54 PM

```

The default time style is [`shortened`](./timestyle/shortened.md).

## Topics

### Modifying a Time Style
- [static let complete: Date.FormatStyle.TimeStyle](./timestyle/complete.md)
  A time style with all components represented.
- [static let omitted: Date.FormatStyle.TimeStyle](./timestyle/omitted.md)
  A time style with no time-related components represented.
- [static let shortened: Date.FormatStyle.TimeStyle](./timestyle/shortened.md)
  A shortened time style with only the hour, minute, and day period components represented.
- [static let standard: Date.FormatStyle.TimeStyle](./timestyle/standard.md)
  A time style with all components except the time zone represented.
### Comparing Time Styles
- [static func == (Date, Date) -> Bool](../eqeq%28_,_%29.md)
  Returns true if the two `Date` values represent the same point in time.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Specifying the Time Format
- [func hour(Date.FormatStyle.Symbol.Hour) -> Date.FormatStyle](./hour%28_%29.md)
  Modifies the date format style to use the specified hour format style.
- [func minute(Date.FormatStyle.Symbol.Minute) -> Date.FormatStyle](./minute%28_%29.md)
  Modifies the date format style to use the specified minute format style.
- [func second(Date.FormatStyle.Symbol.Second) -> Date.FormatStyle](./second%28_%29.md)
  Modifies the date format style to use the specified second format style.
- [func secondFraction(Date.FormatStyle.Symbol.SecondFraction) -> Date.FormatStyle](./secondfraction%28_%29.md)
  Modifies the date format style to use the specified second fraction format style.
- [func timeZone(Date.FormatStyle.Symbol.TimeZone) -> Date.FormatStyle](./timezone%28_%29.md)
  Modifies the date format style to use the specified time zone format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/timestyle)*