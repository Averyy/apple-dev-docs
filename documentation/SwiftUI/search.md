# Search

**Framework**: SwiftUI

Enable people to search for text or other content within your app.

#### Overview

To present a search field in your app, create and manage storage for search text and optionally for discrete search terms known as . Then bind the storage to the search field by applying the searchable view modifier to a view in your app.

![None](https://docs-assets.developer.apple.com/published/366a90bfb4ab3aea60848d447e01a437/search-hero%402x.png)

As people interact with the field, they implicitly modify the underlying storage and, thereby, the search parameters. Your app correspondingly updates other parts of its interface. To enhance the search interaction, you can also:

- Offer suggestions during search, for both text and tokens.
- Implement search scopes that help people to narrow the search space.
- Detect when people activate the search field, and programmatically dismiss the search field using environment values.

For design guidance, see [`Searching`](https://developer.apple.com/design/Human-Interface-Guidelines/searching) in the Human Interface Guidelines.

## Topics

### Searching your app’s data model
- [Adding a search interface to your app](adding-a-search-interface-to-your-app.md)
  Present an interface that people can use to search for content in your app.
- [Performing a search operation](performing-a-search-operation.md)
  Update search results based on search text and optional tokens that you store.
- [func searchable(text:placement:prompt:)](view/searchable(text:placement:prompt:).md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text:tokens:placement:prompt:token:)](view/searchable(text:tokens:placement:prompt:token:).md)
  Marks this view as searchable with text and tokens.
- [func searchable(text:editableTokens:placement:prompt:token:)](view/searchable(text:editabletokens:placement:prompt:token:).md)
  Marks this view as searchable, which configures the display of a search field.
- [struct SearchFieldPlacement](searchfieldplacement.md)
  The placement of a search field in a view hierarchy.
### Making search suggestions
- [Suggesting search terms](suggesting-search-terms.md)
  Provide suggestions to people searching for content in your app.
- [func searchSuggestions<S>(() -> S) -> some View](view/searchsuggestions(_:).md)
  Configures the search suggestions for this view.
- [func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) -> some View](view/searchsuggestions(_:for:).md)
  Configures how to display search suggestions within this view.
- [func searchCompletion(_:)](view/searchcompletion(_:).md)
  Associates a fully formed string with the value of this view when used as a search suggestion.
- [func searchable(text:tokens:suggestedTokens:placement:prompt:token:)](view/searchable(text:tokens:suggestedtokens:placement:prompt:token:).md)
  Marks this view as searchable with text, tokens, and suggestions.
- [struct SearchSuggestionsPlacement](searchsuggestionsplacement.md)
  The ways that SwiftUI displays search suggestions.
### Limiting search scope
- [Scoping a search operation](scoping-a-search-operation.md)
  Divide the search space into a few broad categories.
- [func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View](view/searchscopes(_:scopes:).md)
  Configures the search scopes for this view.
- [func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () -> S) -> some View](view/searchscopes(_:activation:_:).md)
  Configures the search scopes for this view with the specified activation strategy.
- [struct SearchScopeActivation](searchscopeactivation.md)
  The ways that searchable modifiers can show or hide search scopes.
### Detecting, activating, and dismissing search
- [Managing search interface activation](managing-search-interface-activation.md)
  Programmatically detect and dismiss a search field.
- [var isSearching: Bool](environmentvalues/issearching.md)
  A Boolean value that indicates when the user is searching.
- [var dismissSearch: DismissSearchAction](environmentvalues/dismisssearch.md)
  An action that ends the current search interaction.
- [struct DismissSearchAction](dismisssearchaction.md)
  An action that can end a search interaction.
- [func searchable(text:isPresented:placement:prompt:)](view/searchable(text:ispresented:placement:prompt:).md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text:tokens:isPresented:placement:prompt:token:)](view/searchable(text:tokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable(text:editableTokens:isPresented:placement:prompt:token:)](view/searchable(text:editabletokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](view/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
### Displaying toolbar content during search
- [func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) -> some View](view/searchpresentationtoolbarbehavior(_:).md)
  Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [struct SearchPresentationToolbarBehavior](searchpresentationtoolbarbehavior.md)
  A type that defines how the toolbar behaves when presenting search.
### Searching for text in a view with find and replace
- [func findNavigator(isPresented: Binding<Bool>) -> some View](view/findnavigator(ispresented:).md)
  Programmatically presents the find and replace interface for text editor views.
- [func findDisabled(Bool) -> some View](view/finddisabled(_:).md)
  Prevents find and replace operations in a text editor.
- [func replaceDisabled(Bool) -> some View](view/replacedisabled(_:).md)
  Prevents replace operations in a text editor.

## See Also

- [App organization](app-organization.md)
  Define the entry point and top-level structure of your app.
- [Scenes](scenes.md)
  Declare the user interface groupings that make up the parts of your app.
- [Windows](windows.md)
  Display user interface content in a window or a collection of windows.
- [Immersive spaces](immersive-spaces.md)
  Display unbounded content in a person’s surroundings.
- [Documents](documents.md)
  Enable people to open and manage documents.
- [Navigation](navigation.md)
  Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](modal-presentations.md)
  Present content in a separate view that offers focused interaction.
- [Toolbars](toolbars.md)
  Provide immediate access to frequently used commands and controls.
- [App extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system, like by adding a Widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/search)*