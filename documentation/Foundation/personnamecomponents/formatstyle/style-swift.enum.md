# PersonNameComponents.FormatStyle.Style

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

The type that represents the style of the formatted result.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum Style
```

#### Overview

The style type describes a length of the string representation of the name. The available values are [`PersonNameComponents.FormatStyle.Style.long`](./style-swift.enum/long.md), [`PersonNameComponents.FormatStyle.Style.medium`](./style-swift.enum/medium.md), [`PersonNameComponents.FormatStyle.Style.short`](./style-swift.enum/short.md), and [`PersonNameComponents.FormatStyle.Style.abbreviated`](./style-swift.enum/abbreviated.md).

## Topics

### Enumeration Cases
- [PersonNameComponents.FormatStyle.Style.abbreviated](./style-swift.enum/abbreviated.md)
  Specifies an abbreviated person name components style.
- [PersonNameComponents.FormatStyle.Style.long](./style-swift.enum/long.md)
  Specifies a long person name components style.
- [PersonNameComponents.FormatStyle.Style.medium](./style-swift.enum/medium.md)
  Specifies a medium person name components style.
- [PersonNameComponents.FormatStyle.Style.short](./style-swift.enum/short.md)
  Specifies a short person name components style.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Modifying a Format Style
- [var style: PersonNameComponents.FormatStyle.Style](./style-swift.property.md)
  Specifies the style of the formatted result.
- [var locale: Locale](./locale.md)
  The locale to use when formatting the person name components.
- [var attributed: PersonNameComponents.AttributedStyle](./attributed.md)
  The style used to create a locale-aware attributed string representation of an instance of person name components.
- [func locale(Locale) -> PersonNameComponents.FormatStyle](./locale%28_%29.md)
  Modifies the person name components format style to use the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponents/formatstyle/style-swift.enum)*