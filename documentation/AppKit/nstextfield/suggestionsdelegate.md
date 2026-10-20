# suggestionsDelegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate that provides text suggestions for the receiving text field and responds to the user highlighting and selecting items.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
@preconcurrency weak var suggestionsDelegate: (any NSTextSuggestionsDelegate)? { get set }
```

## See Also

### Supporting text completion and suggestions
- [var isAutomaticTextCompletionEnabled: Bool](./isautomatictextcompletionenabled.md)
  A Boolean value that indicates whether the text field automatically completes text as the user types.
- [protocol NSTextSuggestionsDelegate](../nstextsuggestionsdelegate.md)
  A protocol for suggestion delegates of text fields to conform to in order to provide text suggestions in response to the user typing.
- [struct NSSuggestionItem](../nssuggestionitem.md)
  The items that appear in suggestion menus.
- [struct NSSuggestionItemResponse](../nssuggestionitemresponse.md)
  Describes the result of a batch of suggestion items from a search
- [struct NSSuggestionItemSection](../nssuggestionitemsection.md)
  Describes a section of suggestions items in a suggestions menu


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/suggestionsdelegate)*