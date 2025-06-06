# setLocalizedDateFormatFromTemplate(_:)

**Framework**: Foundation  
**Kind**: method

Sets the date format from a template using the specified locale for the receiver.

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
func setLocalizedDateFormatFromTemplate(_ dateFormatTemplate: String)
```

#### Discussion

See [`Data Formatting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i) for a list of the conversion specifiers permitted in date format strings.

Calling this method is equivalent to, but not necessarily implemented as, setting the [`dateFormat`](dateformatter/dateformat.md) property to the result of calling the [`dateFormat(fromTemplate:options:locale:)`](dateformatter/dateformat(fromtemplate:options:locale:).md) method, passing no options and the [`locale`](dateformatter/locale.md) property value.

> ❗ **Important**:  You should call this method only after setting the [`locale`](dateformatter/locale.md) of the receiver.

 You should call this method only after setting the [`locale`](dateformatter/locale.md) of the receiver.

## Parameters

- `dateFormatTemplate`: For full details, see  .

## See Also

- [var locale: Locale!](dateformatter/locale.md)
  The locale for the receiver.
- [var dateStyle: DateFormatter.Style](dateformatter/datestyle.md)
  The date style of the receiver.
- [var timeStyle: DateFormatter.Style](dateformatter/timestyle.md)
  The time style of the receiver.
- [var dateFormat: String!](dateformatter/dateformat.md)
  The date format string used by the receiver.
- [class func dateFormat(fromTemplate: String, options: Int, locale: Locale?) -> String?](dateformatter/dateformat(fromtemplate:options:locale:).md)
  Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.
- [var formattingContext: Formatter.Context](dateformatter/formattingcontext.md)
  The capitalization formatting context used when formatting a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/setlocalizeddateformatfromtemplate(_:))*