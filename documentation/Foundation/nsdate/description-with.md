# description(with:)

**Framework**: Foundation  
**Kind**: method

Returns a string representation of the date using the given locale.

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
func description(with locale: Any?) -> String
```

#### Return Value

A string representation of the receiver, using the given locale, or if the locale argument is `nil`, in the international format `YYYY-MM-DD HH:MM:SS ±HHMM`, where `±HHMM` represents the time zone offset in hours and minutes from UTC (for example, “`2001-03-24 10:45:32 +0600`”)

#### Discussion

In OS X v10.4 and earlier, `localeDictionary` is an `NSDictionary` object containing locale data. To use the user’s preferences, you can use `[[NSUserDefaults standardUserDefaults] dictionaryRepresentation].`

## Parameters

- `locale`: An `NSLocale` object. If you pass `nil`, `NSDate` formats the date in the same way as the [`description`](nsdate/description.md) property. In OS X v10.4 and earlier, this parameter was an `NSDictionary` object. If you pass in an `NSDictionary` object in OS X v10.5, `NSDate` uses the default user locale—the same as if you passed in `[NSLocale currentLocale].`

## See Also

- [var description: String](nsdate/description.md)
  A string representation of the date object.
- [var customPlaygroundQuickLook: PlaygroundQuickLook](nsdate/customplaygroundquicklook.md)
  A custom playground Quick Look for this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/description(with:))*