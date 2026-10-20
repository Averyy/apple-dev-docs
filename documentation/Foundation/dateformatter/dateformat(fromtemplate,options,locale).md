# dateFormat(fromTemplate:options:locale:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSString *) dateFormatFromTemplate:(NSString *) tmplate options:(NSUInteger) opts locale:(NSLocale *) locale;
```

#### Return Value

A localized date format string representing the date format components given in `template`, arranged appropriately for the locale specified by `locale`. The returned string may not contain exactly those components given in `template`, but may—for example—have locale-specific adjustments applied.

#### Discussion

Different locales have different conventions for the ordering of date components. You use this method to get an appropriate format string for a given set of components for a specified locale (typically you use the current locale—see [`current`](../nslocale/current.md)).

The following example shows the difference between the date formats for British and American English:

**Swift**:

```swift
let usLocale = Locale(identifier: "en_US")
let gbLocale = Locale(identifier: "en_GB")
let template = "yMMMMd"
 
let usDateFormat = DateFormatter.dateFormat(fromTemplate: template, options: 0, locale: usLocale)!
// Date format for English (United States): "MMMM d, y"
let gbDateFormat = DateFormatter.dateFormat(fromTemplate: template, options: 0, locale: gbLocale)!
// Date format for English (United Kingdom): "d MMMM y"
```

**Objective-C**:

```objc
NSLocale *usLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_US"];
NSLocale *gbLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_GB"];
 
NSString *template = @"yMMMMd";
 
NSString *enDateFormat = [NSDateFormatter dateFormatFromTemplate:template options:0 locale:usLocale];
NSLog(@"Date format for %@: %@",
    [usLocale displayNameForKey:NSLocaleIdentifier value:[usLocale localeIdentifier]], enDateFormat);
 
NSString *gbDateFormat = [NSDateFormatter dateFormatFromTemplate:template options:0 locale:gbLocale];
NSLog(@"Date format for %@: %@",
    [gbLocale displayNameForKey:NSLocaleIdentifier value:[gbLocale localeIdentifier]], gbDateFormat);
 
// Output:
// Date format for English (United States): MMMM d, y
// Date format for English (United Kingdom): d MMMM y
```

## Parameters

- `tmplate`: A string containing date format patterns (such as “MM” or “h”).

  For full details, see [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).
- `opts`: No options are currently defined.
- `locale`: The locale for which the template is required.

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
- [var formattingContext: Formatter.Context](./formattingcontext.md)
  The capitalization formatting context used when formatting a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/dateformat(fromtemplate:options:locale:))*