# ListFormatStyle.ListType

**Framework**: Foundation  
**Kind**: enum

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

The possible values of a [`listType`](listformatstyle/listtype-swift.property.md) are `and` and `or`.

## Topics

### List types
- [ListFormatStyle.ListType.and](listformatstyle/listtype-swift.enum/and.md)
  Specifies an *and* list type.
- [ListFormatStyle.ListType.or](listformatstyle/listtype-swift.enum/or.md)
  Specifies an *or* list type.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var width: ListFormatStyle<Style, Base>.Width](listformatstyle/width-swift.property.md)
  The size of the list.
- [ListFormatStyle.Width](listformatstyle/width-swift.enum.md)
  The type representing the width of a list.
- [var listType: ListFormatStyle<Style, Base>.ListType](listformatstyle/listtype-swift.property.md)
  The type of the list.
- [var locale: Locale](listformatstyle/locale.md)
  The locale to use when formatting items in the list.
- [func locale(Locale) -> ListFormatStyle<Style, Base>](listformatstyle/locale(_:).md)
  Modifies the list format style to use the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatstyle/listtype-swift.enum)*