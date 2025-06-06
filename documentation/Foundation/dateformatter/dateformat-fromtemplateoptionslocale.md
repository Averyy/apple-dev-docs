# dateFormat(fromTemplate:options:locale:)

**Framework**: Foundation  
**Kind**: method

Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func dateFormat(fromTemplate tmplate: String, options opts: Int, locale: Locale?) -> String?
```

#### Return Value

A localized date format string representing the date format components given in `template`, arranged appropriately for the locale specified by `locale`. The returned string may not contain exactly those components given in `template`, but may—for example—have locale-specific adjustments applied.

#### Discussion

Different locales have different conventions for the ordering of date components. You use this method to get an appropriate format string for a given set of components for a specified locale (typically you use the current locale—see [`current`](nslocale/current.md)).

The following example shows the difference between the date formats for British and American English:

## Parameters

- `tmplate`: For full details, see  .
- `opts`: No options are currently defined.
- `locale`: The locale for which the template is required.

## See Also

- [var dateStyle: DateFormatter.Style](dateformatter/datestyle.md)
  The date style of the receiver.
- [var timeStyle: DateFormatter.Style](dateformatter/timestyle.md)
  The time style of the receiver.
- [var dateFormat: String!](dateformatter/dateformat.md)
  The date format string used by the receiver.
- [func setLocalizedDateFormatFromTemplate(String)](dateformatter/setlocalizeddateformatfromtemplate(_:).md)
  Sets the date format from a template using the specified locale for the receiver.
- [var formattingContext: Formatter.Context](dateformatter/formattingcontext.md)
  The capitalization formatting context used when formatting a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/dateformat(fromtemplate:options:locale:))*