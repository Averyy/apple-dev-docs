# Suggesting search terms

**Framework**: SwiftUI

Provide suggestions to people searching for content in your app.

#### Overview

You can suggest query text during a search operation by providing a collection of search suggestion views. Because suggestion views are not limited to plain text, you must also provide the search string that each suggestion view represents. You can also provide suggestions for tokens, if your search interface includes them. SwiftUI presents the suggestions in a list below the search field.

![A wide rectangle with rounded corners and outlined in blue that contains a magnifying glass on the left, followed by the text, Search in a gray color. A list appears below the rectangle in another rectangle with a drop shadow. The list contains three items, each of which consists of a word and an emoji that displays an image that matches the word. The items are Apple, Pear, and Banana.](https://docs-assets.developer.apple.com/published/f4425da92b699d3b9f0292f1c8c053e8/Search-suggest-0-macOS%402x.png)

For both text and tokens, you manage the list of suggestions, so you have complete flexibility to decide what to suggest. For example, you can:

- Offer a static list of suggestions.
- Remember previous searches and offer the most recent or most common ones.
- Update the list of suggestions in real time based on the current search text.
- Employ some combination of these and other strategies, possibly changing over time.

##### Suggest Search Text

Suggest search text by providing a collection of views to the [`searchSuggestions(_:)`](view/searchsuggestions(_:).md) view modifier. This modifier applies to the [`searchable(text:placement:prompt:)`](view/searchable(text:placement:prompt:).md) modifier that appears before it.

When someone activates the search interface, it presents the suggestion views as a list of choices below the query string. Associate a string with each suggestion view by adding the [`searchCompletion(_:)`](view/searchcompletion(_:).md) modifier to the view inside the search suggestions closure. For example, you can include emoji with fruit types that you suggest as possible products to search for, and provide the corresponding search string as a search completion in each case:

```swift
ProductList(departmentId: departmentId, productId: $productId)
    .searchable(text: $model.searchText)
    .searchSuggestions {
        Text("🍎 Apple").searchCompletion("apple")
        Text("🍐 Pear").searchCompletion("pear")
        Text("🍌 Banana").searchCompletion("banana")
    }
```

When someone chooses a suggestion, SwiftUI replaces the text in the search field with the search completion string. In the above example, choosing “🍐 Pear” puts the text “pear” in the search query.

![A macOS window with three navigation panes. The pane on the left lists the items Produce, Frozen, and Bakery. The middle pane has a long list of fruits and vegetables. The pane on the right has the placeholder text Select a Product. The toolbar has a search field in the upper right of the window that has the placeholder text Search. A list appears attached to the search field, floating above the window. The list contains the items Apple, Pear, and Banana, each represented by an emoji and the corresponding text.](https://docs-assets.developer.apple.com/published/29b5c6ee93212663a69e0d993a7eacbd/Search-suggest-1-macOS%402x.png)

If you omit the search completion modifier for a particular suggestion view, SwiftUI displays the view, but the view doesn’t react to taps or clicks. However, you can group the views with [`Section`](section.md) containers that have headers, enabling you to distinguish different kinds of suggestions, like recent searches and common search terms.

> ❗ **Important**: In tvOS, searchable modifiers only support suggestion views of type [`Text`](text.md), like in the above example. Other platforms can use arbitrary views for the suggestions, including custom views.

Certain events or actions, like when someone moves a macOS window, might dismiss the suggestion list.

##### Suggest Tokens

You can also suggest tokens for the search field. In this case, associate a suggestion view with a token using the version of the [`searchCompletion(_:)`](view/searchcompletion(_:).md) modifier that takes tokens as input:

```swift
ProductList(departmentId: departmentId, productId: $productId)
    .searchable(text: $model.searchText, tokens: $model.tokens) { token in
        switch token {
        case .apple: Text("Apple")
        case .pear: Text("Pear")
        case .banana: Text("Banana")
        }
    }
    .searchSuggestions {
        Text("Apple").searchCompletion(FruitToken.apple)
        Text("Pear").searchCompletion(FruitToken.pear)
        Text("Banana").searchCompletion(FruitToken.banana)
    }
```

You can use any type that conforms to the [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) protocol as a token. For more information about using tokens in the search query, see [`Performing a search operation`](performing-a-search-operation.md).

##### Simplify Token Suggestions

As a convenience when you have a collection of suggestions that exactly matches the list of tokens, you can create a collection of possible tokens to suggest. For example, you can add a published `suggestions` property to your model that contains all the possible tokens:

```swift
@Published var suggestions: [FruitToken] = FruitToken.allCases
```

Then you can provide this array to one of the searchable modifiers that takes a `suggestedTokens` input parameter, like [`searchable(text:tokens:suggestedTokens:placement:prompt:token:)`](view/searchable(text:tokens:suggestedtokens:placement:prompt:token:).md). SwiftUI uses this to generate the suggestions automatically:

```swift
ProductList(departmentId: departmentId, productId: $productId)
    .searchable(
        text: $model.searchText,
        tokens: $model.tokens,
        suggestedTokens: $model.suggestions
    ) { token in
        switch token {
        case .apple: Text("Apple")
        case .pear: Text("Pear")
        case .banana: Text("Banana")
        }
    }
```

In this version of the searchable modifier, SwiftUI uses one view builder to describe the appearance of the tokens in both the search field and the suggestions container.

##### Update Suggestions Dynamically

You can update the suggestions that you provide as conditions change. For example, you can specify an array of `suggestedSearches` that you store in your app’s model:

```swift
ProductList(departmentId: departmentId, productId: $productId)
    .searchable(text: $model.searchText)
    .searchSuggestions {
        ForEach(model.suggestedSearches) { suggestion in
            Label(suggestion.title,  image: suggestion.image)
                .searchCompletion(suggestion.text)
        }
    }
```

If `suggestedSearches` begins as an empty array, the interface doesn’t display any suggestions to start. You can then update the array as conditions change, like when you want to include previous searches.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/suggesting-search-terms)*