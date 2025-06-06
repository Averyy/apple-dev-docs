# listType

**Framework**: Foundation  
**Kind**: property

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

The default value is [`ListFormatStyle.ListType.and`](listformatstyle/listtype-swift.enum/and.md).

## See Also

- [var width: ListFormatStyle<Style, Base>.Width](listformatstyle/width-swift.property.md)
  The size of the list.
- [ListFormatStyle.Width](listformatstyle/width-swift.enum.md)
  The type representing the width of a list.
- [ListFormatStyle.ListType](listformatstyle/listtype-swift.enum.md)
  A type that describes whether the returned list contains cumulative or alternative elements.
- [var locale: Locale](listformatstyle/locale.md)
  The locale to use when formatting items in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatstyle/listtype-swift.property)*