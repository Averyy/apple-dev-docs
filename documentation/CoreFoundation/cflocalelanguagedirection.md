# CFLocaleLanguageDirection

**Framework**: Core Foundation  
**Kind**: enum  
**Role**: Enumeration

These constants describe the text direction for a language. They are returned by the functions [`CFLocaleGetLanguageCharacterDirection(_:)`](./cflocalegetlanguagecharacterdirection%28_%29.md) and [`CFLocaleGetLanguageLineDirection(_:)`](./cflocalegetlanguagelinedirection%28_%29.md).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum CFLocaleLanguageDirection
```

```c
enum CFLocaleLanguageDirection : CFIndex;
```

## Topics

### Constants
- [CFLocaleLanguageDirection.unknown](./cflocalelanguagedirection/unknown.md)
- [CFLocaleLanguageDirection.leftToRight](./cflocalelanguagedirection/lefttoright.md)
- [CFLocaleLanguageDirection.rightToLeft](./cflocalelanguagedirection/righttoleft.md)
- [CFLocaleLanguageDirection.topToBottom](./cflocalelanguagedirection/toptobottom.md)
- [CFLocaleLanguageDirection.bottomToTop](./cflocalelanguagedirection/bottomtotop.md)
### Initializers
- [init?(rawValue: CFIndex)](./cflocalelanguagedirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [Locale Property Keys](./locale-property-keys.md)
  Predefined locale keys used to get property values.
- [Locale Calendar Identifiers](./locale-calendar-identifiers.md)
  Predefined locale keys used to get calendar values—values for `kCFLocaleCalendarIdentifier`.
- [Locale Change Notification](./locale-change-notification.md)
  Identifier for notification sent if the current locale changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalelanguagedirection)*