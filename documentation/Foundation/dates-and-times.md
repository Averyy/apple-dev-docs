# Dates and Times

**Framework**: Foundation

Compare dates and times, and perform calendar and time zone calculations.

## Topics

### Date Representations
- [struct Date](date.md)
  A specific point in time, independent of any calendar or time zone.
- [struct DateInterval](dateinterval.md)
  The span of time between a specific start date and end date.
- [typealias TimeInterval](timeinterval.md)
  A number of seconds.
### Calendrical Calculations
- [struct DateComponents](datecomponents.md)
  A date or time specified in terms of units (such as year, month, day, hour, and minute) to be evaluated in a calendar system and time zone.
- [struct Calendar](calendar.md)
  A definition of the relationships between calendar units and absolute points in time, providing features for calculation and comparison of dates.
- [struct TimeZone](timezone.md)
  Information about standard time conventions associated with a specific geopolitical region.
### Date Formatting
- [class DateFormatter](dateformatter.md)
  A formatter that converts between dates and their textual representations.
- [class DateComponentsFormatter](datecomponentsformatter.md)
  A formatter that creates string representations of quantities of time.
- [class DateIntervalFormatter](dateintervalformatter.md)
  A formatter that creates string representations of time intervals.
- [class ISO8601DateFormatter](iso8601dateformatter.md)
  A formatter that converts between dates and their ISO 8601 string representations.
### Internationalization
- [struct Locale](locale.md)
  Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.

## See Also

- [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md)
  Work with primitive values and other fundamental types used throughout Cocoa.
- [Strings and Text](strings-and-text.md)
  Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](collections.md)
  Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Units and Measurement](units-and-measurement.md)
  Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](data-formatting.md)
  Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](filters-and-sorting.md)
  Use predicates, expressions, and sort descriptors to examine elements in collections and other services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dates-and-times)*