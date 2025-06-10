# NSTextSuggestionsDelegate

**Framework**: AppKit  
**Kind**: protocol

A protocol for suggestion delegates of text fields to conform to in order to provide text suggestions in response to the user typing.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
protocol NSTextSuggestionsDelegate<SuggestionItemType> : AnyObject
```

## Topics

### Associated Types
- [associatedtype SuggestionItemType](nstextsuggestionsdelegate/suggestionitemtype.md)
  The type of the `representedValue` property of the provided suggestion items (`NSSuggestionItem`).
### Instance Methods
- [func appending(some NSTextSuggestionsDelegate<Self.SuggestionItemType>) -> some NSTextSuggestionsDelegate<Self.SuggestionItemType>
](nstextsuggestionsdelegate/appending(_:)-1gb8y.md)
  Returns a new text suggestions delegate of the same suggestion item type with the items and behaviors of the receiving delegate and `other` concatenated. When the returned delegate is connected to a text field, all suggestion items provided from the first suggestions delegate appear before all those from the second suggestions delegate, visually separated by a separator.
- [func appending<T>(some NSTextSuggestionsDelegate) -> some NSTextSuggestionsDelegate<AnyHashable>
](nstextsuggestionsdelegate/appending(_:)-5x8a.md)
  Returns a new text suggestions delegate of a different, but `Hashable` suggestion item type with the items and behaviors of the receiving delegate and `other` concatenated. When the returned delegate is connected to a text field, all suggestion items provided from the first suggestions delegate appear before all those from the second suggestions delegate, visually separated by a separator.
- [func textField(NSTextField, didSelect: Self.Item)](nstextsuggestionsdelegate/textfield(_:didselect:).md)
  Called when an item in the suggestions menu has been selected.
- [func textField(NSTextField, provideUpdatedSuggestions: (Self.ItemResponse) -> Void)](nstextsuggestionsdelegate/textfield(_:provideupdatedsuggestions:).md)
  Called when the text field’s text (or tokens) have changed and when the text field is going to display a new list of suggestion items.
- [func textField(NSTextField, textCompletionFor: Self.Item) -> String?](nstextsuggestionsdelegate/textfield(_:textcompletionfor:).md)
  Returns the full completion text for a particular item to use when the item is highlighted or selected.
### Type Aliases
- [NSTextSuggestionsDelegate.Item](nstextsuggestionsdelegate/item.md)
  A suggestion item with the same suggestion item type as the delegate.
- [NSTextSuggestionsDelegate.ItemResponse](nstextsuggestionsdelegate/itemresponse.md)
  A suggestion item response with the same generic type as the delegate.
- [NSTextSuggestionsDelegate.ItemSection](nstextsuggestionsdelegate/itemsection.md)
  A suggestion item section with the same suggestion item type as the controller.

## See Also

- [var isAutomaticTextCompletionEnabled: Bool](nstextfield/isautomatictextcompletionenabled.md)
  A Boolean value that indicates whether the text field automatically completes text as the user types.
- [struct NSSuggestionItem](nssuggestionitem.md)
  The items that appear in suggestion menus.
- [struct NSSuggestionItemResponse](nssuggestionitemresponse.md)
  Describes the result of a batch of suggestion items from a search
- [struct NSSuggestionItemSection](nssuggestionitemsection.md)
  Describes a section of suggestions items in a suggestions menu


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextsuggestionsdelegate)*