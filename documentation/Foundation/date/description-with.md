# description(with:)

**Framework**: Foundation  
**Kind**: method

Returns a string representation of the receiver using the given locale.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func description(with locale: Locale?) -> String
```

#### Return Value

A string representation of the `Date`, using the given locale, or if the locale argument is `nil`, in the international format `YYYY-MM-DD HH:MM:SS ±HHMM`, where `±HHMM` represents the time zone offset in hours and minutes from UTC (for example, “`2001-03-24 10:45:32 +0600`”).

## Parameters

- `locale`: A  . If you pass  ,   formats the date in the same way as the   property.

## See Also

- [var description: String](date/description.md)
  The representation is useful for debugging only. There are a number of options to acquire a formatted string for a date including: date formatters (see [`NSDateFormatter`](https://developer.apple.com//apple_ref/occ/cl/NSDateFormatter) and [`Data Formatting Guide`](https://developer.apple.com//apple_ref/doc/uid/10000029i)), and the `Date` function `description(locale:)`.
- [var customPlaygroundQuickLook: PlaygroundQuickLook](date/customplaygroundquicklook.md)
  A custom playground Quick Look for the date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/description(with:))*