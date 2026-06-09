# locale(_:)

**Framework**: Foundation  
**Kind**: method

Modifies the person name components format style to use the specified locale.

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
func locale(_ locale: Locale) -> PersonNameComponents.FormatStyle
```

#### Return Value

A person name components format style with the provided locale.

## Parameters

- `locale`: The locale to use when formatting person name components.

## See Also

- [var style: PersonNameComponents.FormatStyle.Style](personnamecomponents/formatstyle/style-swift.property.md)
  Specifies the style of the formatted result.
- [PersonNameComponents.FormatStyle.Style](personnamecomponents/formatstyle/style-swift.enum.md)
  The type that represents the style of the formatted result.
- [var locale: Locale](personnamecomponents/formatstyle/locale.md)
  The locale to use when formatting the person name components.
- [var attributed: PersonNameComponents.AttributedStyle](personnamecomponents/formatstyle/attributed.md)
  The style used to create a locale-aware attributed string representation of an instance of person name components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponents/formatstyle/locale(_:))*