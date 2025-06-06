# formattingContext

**Framework**: Foundation  
**Kind**: property

The capitalization formatting context used when formatting a date.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var formattingContext: Formatter.Context { get set }
```

#### Discussion

The formatting context allows the formatter to apply appropriate capitalization depending on how the how the string will be used, and whether the locale makes capitalization distinctions.

## See Also

- [var dateStyle: DateFormatter.Style](dateformatter/datestyle.md)
  The date style of the receiver.
- [var timeStyle: DateFormatter.Style](dateformatter/timestyle.md)
  The time style of the receiver.
- [var dateFormat: String!](dateformatter/dateformat.md)
  The date format string used by the receiver.
- [func setLocalizedDateFormatFromTemplate(String)](dateformatter/setlocalizeddateformatfromtemplate(_:).md)
  Sets the date format from a template using the specified locale for the receiver.
- [class func dateFormat(fromTemplate: String, options: Int, locale: Locale?) -> String?](dateformatter/dateformat(fromtemplate:options:locale:).md)
  Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/formattingcontext)*