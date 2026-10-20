# dateFormat

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The date format string used by the receiver.

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
var dateFormat: String! { get set }
```

```objc
@property (copy, null_resettable) NSString * dateFormat;
```

#### Discussion

See [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i) for a list of the conversion specifiers permitted in date format strings.

You should only set this property when working with fixed format representations, as discussed in [Working With Fixed Format Date Representations](../dateformatter.md#Working-With-Fixed-Format-Date-Representations). For user-visible representations, you should use the [`dateStyle`](./datestyle.md) and [`timeStyle`](./timestyle.md) properties, or the [`setLocalizedDateFormatFromTemplate(_:)`](./setlocalizeddateformatfromtemplate%28_%29.md) method if your desired format cannot be achieved using the predefined styles; both of these properties and this method provide a localized date representation appropriate for display to the user.

## See Also

### Managing Formats and Styles
- [var dateStyle: DateFormatter.Style](./datestyle.md)
  The date style of the receiver.
- [var timeStyle: DateFormatter.Style](./timestyle.md)
  The time style of the receiver.
- [func setLocalizedDateFormatFromTemplate(String)](./setlocalizeddateformatfromtemplate%28_%29.md)
  Sets the date format from a template using the specified locale for the receiver.
- [class func dateFormat(fromTemplate: String, options: Int, locale: Locale?) -> String?](./dateformat%28fromtemplate,options,locale%29.md)
  Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.
- [var formattingContext: Formatter.Context](./formattingcontext.md)
  The capitalization formatting context used when formatting a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/dateformat)*