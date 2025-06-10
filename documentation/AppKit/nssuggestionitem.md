# NSSuggestionItem

**Framework**: AppKit  
**Kind**: struct

The items that appear in suggestion menus.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct NSSuggestionItem<SuggestionItemType>
```

## Topics

### Initializers
- [init(representedValue: SuggestionItemType, attributedTitle: AttributedString)](nssuggestionitem/init(representedvalue:attributedtitle:).md)
- [init(representedValue: SuggestionItemType, title: String)](nssuggestionitem/init(representedvalue:title:).md)
### Instance Properties
- [var attributedSecondaryTitle: AttributedString?](nssuggestionitem/attributedsecondarytitle.md)
  An optional second attributed string to display for a suggestion menu item. This value should be localized. This value is an attributed string representation of `secondaryTitle`.
- [var attributedTitle: AttributedString](nssuggestionitem/attributedtitle.md)
  An attributed string to display for a suggestion menu item. This value should be localized. This value is an attributed string representation of `title`.
- [var image: NSImage?](nssuggestionitem/image.md)
  An optional image to display before the title. This value should be localized.
- [var representedValue: SuggestionItemType](nssuggestionitem/representedvalue.md)
  The value represented by the receiver.
- [var secondaryTitle: String?](nssuggestionitem/secondarytitle.md)
  An optional second string to display for a suggestion menu item. This value should be localized. This value is a non-attributed string representation of `attributedSecondaryTitle`.
- [var title: String](nssuggestionitem/title.md)
  A string to display for a suggestion menu item. This value should be localized. This value is a non-attributed string representation of `attributedTitle`.
- [var toolTip: String?](nssuggestionitem/tooltip.md)
  An optional tool tip to display on hover for a suggestion menu item. This value should be localized.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var isAutomaticTextCompletionEnabled: Bool](nstextfield/isautomatictextcompletionenabled.md)
  A Boolean value that indicates whether the text field automatically completes text as the user types.
- [protocol NSTextSuggestionsDelegate](nstextsuggestionsdelegate.md)
  A protocol for suggestion delegates of text fields to conform to in order to provide text suggestions in response to the user typing.
- [struct NSSuggestionItemResponse](nssuggestionitemresponse.md)
  Describes the result of a batch of suggestion items from a search
- [struct NSSuggestionItemSection](nssuggestionitemsection.md)
  Describes a section of suggestions items in a suggestions menu


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssuggestionitem)*