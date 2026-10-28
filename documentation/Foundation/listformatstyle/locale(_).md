# locale(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the list format style to use the specified locale.

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
func locale(_ locale: Locale) -> ListFormatStyle<Style, Base>
```

## Return Value

A list format style with the provided locale.

## Parameters

- `locale`: The locale to use when formatting items in the list.

## See Also

### Modifying a list format style
- [var width: ListFormatStyle<Style, Base>.Width](./width-swift.property.md)
  The size of the list.
- [ListFormatStyle.Width](./width-swift.enum.md)
  The type representing the width of a list.
- [var listType: ListFormatStyle<Style, Base>.ListType](./listtype-swift.property.md)
  The type of the list.
- [ListFormatStyle.ListType](./listtype-swift.enum.md)
  A type that describes whether the returned list contains cumulative or alternative elements.
- [var locale: Locale](./locale.md)
  The locale to use when formatting items in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatstyle/locale(_:))*