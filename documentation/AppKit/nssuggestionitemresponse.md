# NSSuggestionItemResponse

**Framework**: AppKit  
**Kind**: struct

Describes the result of a batch of suggestion items from a search

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct NSSuggestionItemResponse<SuggestionItemType>
```

## Topics

### Initializers
- [init()](nssuggestionitemresponse/init.md)
- [init(itemSections: [NSSuggestionItemResponse<SuggestionItemType>.ItemSection])](nssuggestionitemresponse/init(itemsections:).md)
- [init(items: [NSSuggestionItemResponse<SuggestionItemType>.Item])](nssuggestionitemresponse/init(items:).md)
### Instance Properties
- [var itemSections: [NSSuggestionItemResponse<SuggestionItemType>.ItemSection]](nssuggestionitemresponse/itemsections.md)
  The items (organized in sections) representing the results of the search request
- [var phase: NSSuggestionItemResponse<SuggestionItemType>.Phase](nssuggestionitemresponse/phase-swift.property.md)
  Describes the phase of results. In other words, whether this batch of items represents an intermediate set of results–and more are coming, or whether these results are complete/final. Defaults to `.final`.
- [var preferredHighlight: NSSuggestionItemResponse<SuggestionItemType>.Highlight](nssuggestionitemresponse/preferredhighlight.md)
  The preferred response that the control should take when this batch of results comes in (like whether or not to highlight the first selectable item). Defaults to `.automatic`.
### Type Aliases
- [NSSuggestionItemResponse.Item](nssuggestionitemresponse/item.md)
  A suggestion item with the same suggestion item type as the response
- [NSSuggestionItemResponse.ItemSection](nssuggestionitemresponse/itemsection.md)
  A suggestion item section with the same suggestion item type as the response
### Enumerations
- [NSSuggestionItemResponse.Highlight](nssuggestionitemresponse/highlight.md)
  Describes the possible ways the highlighted item may be impacted by these results
- [NSSuggestionItemResponse.Phase](nssuggestionitemresponse/phase-swift.enum.md)
  Describes the different possible phases of results

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
- [struct NSSuggestionItem](nssuggestionitem.md)
  The items that appear in suggestion menus.
- [struct NSSuggestionItemSection](nssuggestionitemsection.md)
  Describes a section of suggestions items in a suggestions menu


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssuggestionitemresponse)*