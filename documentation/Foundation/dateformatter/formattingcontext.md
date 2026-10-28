# formattingContext

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property NSFormattingContext formattingContext;
```

## Discussion

The formatting context allows the formatter to apply appropriate capitalization depending on how the how the string will be used, and whether the locale makes capitalization distinctions.

## See Also

### Managing Formats and Styles
- [var dateStyle: DateFormatter.Style](./datestyle.md)
  The date style of the receiver.
- [var timeStyle: DateFormatter.Style](./timestyle.md)
  The time style of the receiver.
- [var dateFormat: String!](./dateformat.md)
  The date format string used by the receiver.
- [func setLocalizedDateFormatFromTemplate(String)](./setlocalizeddateformatfromtemplate%28_%29.md)
  Sets the date format from a template using the specified locale for the receiver.
- [class func dateFormat(fromTemplate: String, options: Int, locale: Locale?) -> String?](./dateformat%28fromtemplate,options,locale%29.md)
  Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/formattingcontext)*