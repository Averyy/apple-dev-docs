# Search modifiers

**Framework**: SwiftUI

Enable people to search for content in your app.

#### Overview

Use search view modifiers to add search capability to your app. For more information, see [`Search`](search.md).

## Topics

### Displaying a search interface
- [func searchable(text:placement:prompt:)](view/searchable(text:placement:prompt:).md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text:isPresented:placement:prompt:)](view/searchable(text:ispresented:placement:prompt:).md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) -> some View](view/searchpresentationtoolbarbehavior(_:).md)
  Configures the search toolbar presentation behavior for any searchable modifiers within this view.
### Searching with tokens
- [func searchable(text:tokens:placement:prompt:token:)](view/searchable(text:tokens:placement:prompt:token:).md)
  Marks this view as searchable with text and tokens.
- [func searchable(text:tokens:isPresented:placement:prompt:token:)](view/searchable(text:tokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
### Searching with editable tokens
- [func searchable(text:editableTokens:isPresented:placement:prompt:token:)](view/searchable(text:editabletokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text:editableTokens:placement:prompt:token:)](view/searchable(text:editabletokens:placement:prompt:token:).md)
  Marks this view as searchable, which configures the display of a search field.
### Making search suggestions
- [func searchSuggestions<S>(() -> S) -> some View](view/searchsuggestions(_:).md)
  Configures the search suggestions for this view.
- [func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) -> some View](view/searchsuggestions(_:for:).md)
  Configures how to display search suggestions within this view.
- [func searchCompletion(_:)](view/searchcompletion(_:).md)
  Associates a fully formed string with the value of this view when used as a search suggestion.
- [func searchable(text:tokens:suggestedTokens:placement:prompt:token:)](view/searchable(text:tokens:suggestedtokens:placement:prompt:token:).md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](view/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
### Limiting search scope
- [func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View](view/searchscopes(_:scopes:).md)
  Configures the search scopes for this view.
- [func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () -> S) -> some View](view/searchscopes(_:activation:_:).md)
  Configures the search scopes for this view with the specified activation strategy.
### Searching through dictation
- [func searchDictationBehavior(TextInputDictationBehavior) -> some View](view/searchdictationbehavior(_:).md)
  Configures the dictation behavior for any search fields configured by the searchable modifier.

## See Also

- [Input and event modifiers](view-input-and-events.md)
  Supply actions for a view to perform in response to user input and system events.
- [Presentation modifiers](view-presentation.md)
  Define additional views for the view to present under specified conditions.
- [State modifiers](view-state.md)
  Access storage and provide child views with configuration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-search)*