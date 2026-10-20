# ISO8601DateFormatter.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Options used to generate and parse ISO 8601 date representations.

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
struct Options
```

```c
enum NSISO8601DateFormatOptions : NSUInteger;
```

## Topics

### Constants
- [static var withYear: ISO8601DateFormatter.Options](./options/withyear.md)
- [static var withMonth: ISO8601DateFormatter.Options](./options/withmonth.md)
- [static var withWeekOfYear: ISO8601DateFormatter.Options](./options/withweekofyear.md)
- [static var withDay: ISO8601DateFormatter.Options](./options/withday.md)
- [static var withTime: ISO8601DateFormatter.Options](./options/withtime.md)
- [static var withTimeZone: ISO8601DateFormatter.Options](./options/withtimezone.md)
- [static var withSpaceBetweenDateAndTime: ISO8601DateFormatter.Options](./options/withspacebetweendateandtime.md)
- [static var withDashSeparatorInDate: ISO8601DateFormatter.Options](./options/withdashseparatorindate.md)
- [static var withColonSeparatorInTime: ISO8601DateFormatter.Options](./options/withcolonseparatorintime.md)
- [static var withColonSeparatorInTimeZone: ISO8601DateFormatter.Options](./options/withcolonseparatorintimezone.md)
- [static var withFullDate: ISO8601DateFormatter.Options](./options/withfulldate.md)
- [static var withFullTime: ISO8601DateFormatter.Options](./options/withfulltime.md)
- [static var withInternetDateTime: ISO8601DateFormatter.Options](./options/withinternetdatetime.md)
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)
### Type Properties
- [static var withFractionalSeconds: ISO8601DateFormatter.Options](./options/withfractionalseconds.md)
  The date representation uses the colon separator (`:`) in the time zone.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/iso8601dateformatter/options)*