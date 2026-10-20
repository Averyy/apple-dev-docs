# ListFormatStyle.ListType

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A type that describes whether the returned list contains cumulative or alternative elements.

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
enum ListType
```

#### Overview

The possible values of a [`listType`](./listtype-swift.property.md) are `and` and `or`.

## Topics

### List types
- [ListFormatStyle.ListType.and](./listtype-swift.enum/and.md)
  Specifies an *and* list type.
- [ListFormatStyle.ListType.or](./listtype-swift.enum/or.md)
  Specifies an *or* list type.

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
- [ListFormatStyle.Width](./width-swift.enum.md)
  The type representing the width of a list.
- [var listType: ListFormatStyle<Style, Base>.ListType](./listtype-swift.property.md)
  The type of the list.
- [var locale: Locale](./locale.md)
  The locale to use when formatting items in the list.
- [func locale(Locale) -> ListFormatStyle<Style, Base>](./locale%28_%29.md)
  Modifies the list format style to use the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatstyle/listtype-swift.enum)*