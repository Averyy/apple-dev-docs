# localizedName(_:locale:)

**Framework**: Foundation  
**Kind**: method

Returns the localized name of the time zone.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func localizedName(_ style: NSTimeZone.NameStyle, locale: Locale?) -> String?
```

#### Return Value

The name of the receiver localized for `locale` using `style`.

## Parameters

- `style`: The format style for the returned string.
- `locale`: The locale for which to format the name.

## See Also

- [var description: String](nstimezone/description.md)
  A textual description of the time zone including the name, abbreviation, offset from GMT, and whether or not daylight saving time is currently in effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/localizedname(_:locale:))*