# Date.FormatStyle.Attributed

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

The type preserving attributed variant of this style.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
@dynamicMemberLookup
struct Attributed
```

#### Overview

This style attributes the formatted date with the `AttributeScopes.FoundationAttributes.DateFormatFieldAttribute`.

## Topics

### Instance Methods
- [func day(Date.FormatStyle.Symbol.Day) -> Date.FormatStyle.Attributed](./attributed-swift.struct/day%28_%29.md)
  Change the representation of the day of the month in the format.
- [func dayOfYear(Date.FormatStyle.Symbol.DayOfYear) -> Date.FormatStyle.Attributed](./attributed-swift.struct/dayofyear%28_%29.md)
  Change the representation of the day of the year in the format.
- [func era(Date.FormatStyle.Symbol.Era) -> Date.FormatStyle.Attributed](./attributed-swift.struct/era%28_%29.md)
  Change the representation of the era in the format.
- [func format(Date) -> AttributedString](./attributed-swift.struct/format%28_%29.md)
- [func hour(Date.FormatStyle.Symbol.Hour) -> Date.FormatStyle.Attributed](./attributed-swift.struct/hour%28_%29.md)
  Change the representation of the hour in the format.
- [func locale(Locale) -> Date.FormatStyle.Attributed](./attributed-swift.struct/locale%28_%29.md)
- [func minute(Date.FormatStyle.Symbol.Minute) -> Date.FormatStyle.Attributed](./attributed-swift.struct/minute%28_%29.md)
  Change the representation of the minute in the format.
- [func month(Date.FormatStyle.Symbol.Month) -> Date.FormatStyle.Attributed](./attributed-swift.struct/month%28_%29.md)
  Change the representation of the month in the format.
- [func quarter(Date.FormatStyle.Symbol.Quarter) -> Date.FormatStyle.Attributed](./attributed-swift.struct/quarter%28_%29.md)
  Change the representation of the quarter in the format.
- [func second(Date.FormatStyle.Symbol.Second) -> Date.FormatStyle.Attributed](./attributed-swift.struct/second%28_%29.md)
  Change the representation of the second in the format.
- [func secondFraction(Date.FormatStyle.Symbol.SecondFraction) -> Date.FormatStyle.Attributed](./attributed-swift.struct/secondfraction%28_%29.md)
  Change the representation of the second fraction in the format.
- [func timeZone(Date.FormatStyle.Symbol.TimeZone) -> Date.FormatStyle.Attributed](./attributed-swift.struct/timezone%28_%29.md)
  Change the representation of the time zone in the format.
- [func week(Date.FormatStyle.Symbol.Week) -> Date.FormatStyle.Attributed](./attributed-swift.struct/week%28_%29.md)
  Change the representation of the week in the format.
- [func weekday(Date.FormatStyle.Symbol.Weekday) -> Date.FormatStyle.Attributed](./attributed-swift.struct/weekday%28_%29.md)
  Change the representation of the weekday in the format.
- [func year(Date.FormatStyle.Symbol.Year) -> Date.FormatStyle.Attributed](./attributed-swift.struct/year%28_%29.md)
  Change the representation of the year in the format.
### Subscripts
- [subscript<T>(dynamicMember _: WritableKeyPath<Date.FormatStyle, T>) -> T](./attributed-swift.struct/subscript%28dynamicmember%29-5y393.md)
- [subscript<T>(dynamicMember _: KeyPath<Date.FormatStyle, T>) -> T](./attributed-swift.struct/subscript%28dynamicmember%29-8es0v.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Decodable](../../../Swift/decodable.md)
- [DiscreteFormatStyle](../../discreteformatstyle.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [FormatStyle](../../formatstyle.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/attributed-swift.struct)*