# CFLocaleLanguageDirection

**Framework**: Core Foundation  
**Kind**: enum

These constants describe the text direction for a language. They are returned by the functions [`CFLocaleGetLanguageCharacterDirection(_:)`](cflocalegetlanguagecharacterdirection(_:).md) and [`CFLocaleGetLanguageLineDirection(_:)`](cflocalegetlanguagelinedirection(_:).md).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CFLocaleLanguageDirection
```

## Topics

### Constants
- [CFLocaleLanguageDirection.unknown](cflocalelanguagedirection/unknown.md)
- [CFLocaleLanguageDirection.leftToRight](cflocalelanguagedirection/lefttoright.md)
- [CFLocaleLanguageDirection.rightToLeft](cflocalelanguagedirection/righttoleft.md)
- [CFLocaleLanguageDirection.topToBottom](cflocalelanguagedirection/toptobottom.md)
- [CFLocaleLanguageDirection.bottomToTop](cflocalelanguagedirection/bottomtotop.md)
### Initializers
- [init?(rawValue: CFIndex)](cflocalelanguagedirection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Locale Property Keys](locale-property-keys.md)
  Predefined locale keys used to get property values.
- [Locale Calendar Identifiers](locale-calendar-identifiers.md)
  Predefined locale keys used to get calendar values—values for `kCFLocaleCalendarIdentifier`.
- [Locale Change Notification](locale-change-notification.md)
  Identifier for notification sent if the current locale changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalelanguagedirection)*