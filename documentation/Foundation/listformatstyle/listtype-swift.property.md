# listType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The type of the list.

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
var listType: ListFormatStyle<Style, Base>.ListType
```

#### Discussion

The list type determines the semantics used in the return string.

For example, for en_US:

```swift
["One", "Two", "Three"].formatted(.list(type: .and))
// “One, Two, and Three”

["One", "Two", "Three"].formatted(.list(type: .or))
// “One, Two, or Three” 
```

The default value is [`ListFormatStyle.ListType.and`](./listtype-swift.enum/and.md).

## See Also

### Modifying a list format style
- [var width: ListFormatStyle<Style, Base>.Width](./width-swift.property.md)
  The size of the list.
- [ListFormatStyle.Width](./width-swift.enum.md)
  The type representing the width of a list.
- [ListFormatStyle.ListType](./listtype-swift.enum.md)
  A type that describes whether the returned list contains cumulative or alternative elements.
- [var locale: Locale](./locale.md)
  The locale to use when formatting items in the list.
- [func locale(Locale) -> ListFormatStyle<Style, Base>](./locale%28_%29.md)
  Modifies the list format style to use the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatstyle/listtype-swift.property)*