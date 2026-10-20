# dateStyle

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The date style of the receiver.

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
var dateStyle: DateFormatter.Style { get set }
```

```objc
@property NSDateFormatterStyle dateStyle;
```

## See Also

### Managing Formats and Styles
- [var timeStyle: DateFormatter.Style](./timestyle.md)
  The time style of the receiver.
- [var dateFormat: String!](./dateformat.md)
  The date format string used by the receiver.
- [func setLocalizedDateFormatFromTemplate(String)](./setlocalizeddateformatfromtemplate%28_%29.md)
  Sets the date format from a template using the specified locale for the receiver.
- [class func dateFormat(fromTemplate: String, options: Int, locale: Locale?) -> String?](./dateformat%28fromtemplate,options,locale%29.md)
  Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.
- [var formattingContext: Formatter.Context](./formattingcontext.md)
  The capitalization formatting context used when formatting a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/datestyle)*