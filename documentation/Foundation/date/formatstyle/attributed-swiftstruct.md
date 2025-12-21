# Date.FormatStyle.Attributed

**Framework**: Foundation  
**Kind**: struct

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
- [func day(Date.FormatStyle.Symbol.Day) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/day(_:).md)
  Change the representation of the day of the month in the format.
- [func dayOfYear(Date.FormatStyle.Symbol.DayOfYear) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/dayofyear(_:).md)
  Change the representation of the day of the year in the format.
- [func era(Date.FormatStyle.Symbol.Era) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/era(_:).md)
  Change the representation of the era in the format.
- [func hour(Date.FormatStyle.Symbol.Hour) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/hour(_:).md)
  Change the representation of the hour in the format.
- [func minute(Date.FormatStyle.Symbol.Minute) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/minute(_:).md)
  Change the representation of the minute in the format.
- [func month(Date.FormatStyle.Symbol.Month) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/month(_:).md)
  Change the representation of the month in the format.
- [func quarter(Date.FormatStyle.Symbol.Quarter) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/quarter(_:).md)
  Change the representation of the quarter in the format.
- [func second(Date.FormatStyle.Symbol.Second) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/second(_:).md)
  Change the representation of the second in the format.
- [func secondFraction(Date.FormatStyle.Symbol.SecondFraction) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/secondfraction(_:).md)
  Change the representation of the second fraction in the format.
- [func timeZone(Date.FormatStyle.Symbol.TimeZone) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/timezone(_:).md)
  Change the representation of the time zone in the format.
- [func week(Date.FormatStyle.Symbol.Week) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/week(_:).md)
  Change the representation of the week in the format.
- [func weekday(Date.FormatStyle.Symbol.Weekday) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/weekday(_:).md)
  Change the representation of the weekday in the format.
- [func year(Date.FormatStyle.Symbol.Year) -> Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct/year(_:).md)
  Change the representation of the year in the format.
### Subscripts
- [subscript<T>(dynamicMember _: WritableKeyPath<Date.FormatStyle, T>) -> T](date/formatstyle/attributed-swift.struct/subscript(dynamicmember:)-5y393.md)
- [subscript<T>(dynamicMember _: KeyPath<Date.FormatStyle, T>) -> T](date/formatstyle/attributed-swift.struct/subscript(dynamicmember:)-8es0v.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [DiscreteFormatStyle](discreteformatstyle.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/attributed-swift.struct)*