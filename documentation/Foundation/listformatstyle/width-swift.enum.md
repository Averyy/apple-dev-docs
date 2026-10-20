# ListFormatStyle.Width

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

The type representing the width of a list.

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
enum Width
```

#### Overview

The possible values of a [`width`](./width-swift.property.md) are `standard`, `short`, and `narrow`.

## Topics

### Widths
- [ListFormatStyle.Width.standard](./width-swift.enum/standard.md)
  Specifies a standard list style.
- [ListFormatStyle.Width.short](./width-swift.enum/short.md)
  Specifies a short list style.
- [ListFormatStyle.Width.narrow](./width-swift.enum/narrow.md)
  Specifies a narrow list style, the shortest list style.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Modifying a list format style
- [var width: ListFormatStyle<Style, Base>.Width](./width-swift.property.md)
  The size of the list.
- [var listType: ListFormatStyle<Style, Base>.ListType](./listtype-swift.property.md)
  The type of the list.
- [ListFormatStyle.ListType](./listtype-swift.enum.md)
  A type that describes whether the returned list contains cumulative or alternative elements.
- [var locale: Locale](./locale.md)
  The locale to use when formatting items in the list.
- [func locale(Locale) -> ListFormatStyle<Style, Base>](./locale%28_%29.md)
  Modifies the list format style to use the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatstyle/width-swift.enum)*