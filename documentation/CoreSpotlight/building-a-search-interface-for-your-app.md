# Building a search interface for your app

**Framework**: Corespotlight

Add a search interface to your app to execute Spotlight queries and offer suggested text completions.

#### Overview

Adding search tools to your app gives people a way to find content more easily. Whether you add search controls to an app window or to one of the views in your interface, use Spotlight to generate the search results for your content. Spotlight searches the content you already indexed, and provides relevant text completions and results for you to display. In iOS 18 and macOS 15 and later, Spotlight also supports semantic searches of your content, in addition to lexical matching of a search term.

To take full advantage of search into your interface, make sure you index your app’s content and provide it to Spotlight. As your app generates or changes its content, send the details of those changes to Spotlight so it can update its indexes. It’s also important to provide an app extension that Spotlight can call to regenerate those details on demand. For more information about providing Spotlight with your app’s data, see [`Adding your app’s content to Spotlight indexes`](adding-your-app-s-content-to-spotlight-indexes.md).

##### Add a Search Field to Your Interface

Apple’s UI frameworks provide search controls you can add to your interface, and support to provide a consistent search experience. Incorporate these controls into your views and use the built-in support to initiate searches and display the results.

- In SwiftUI, add a `searchable` modifier to a view in your interface. This modifier creates an implicit search field to your interface and binds it to the string you use to initiate queries. For more information, see [`Adding a search interface to your app`](https://developer.apple.com/documentation/SwiftUI/Adding-a-search-interface-to-your-app).
- In UIKit, add a [`UISearchBar`](https://developer.apple.com/documentation/UIKit/UISearchBar) control to your interface, and display results using an associated [`UISearchController`](https://developer.apple.com/documentation/UIKit/UISearchController).
- In AppKit, [`NSSearchField`](https://developer.apple.com/documentation/AppKit/NSSearchField) provides a text field with search-related behaviors.

The built-in search controls provide features that people expect when searching for content, such as text completions and text tokens. You can also apply filters to limit the scope of the search to a particular part of your app. Core Spotlight helps you implement these features by providing the data you need for your app’s interface in a compatible format.

##### Prepare the Search System

To ensure initial searches happen quickly, call the [`prepare()`](csuserquery/prepare().md) class method. Call this method before you need to perform queries, such as when the view that presents your search interface first appears. You don’t need to call the method more than once when your app is running, and you don’t need to execute the query itself. The method prepares Core Spotlight resources, which can take a noticeable amount of time. It also increases your app’s memory footprint, so call it as late as possible to minimize the performance impact.

##### Execute a Query and Receive the Responses

When someone types a value into your app’s search control, don’t execute the query immediately. Instead, give the person a small amount of time to type more text into the search field. For example, wait 0.3 seconds after each new keystroke before starting a query with the current text. If a new keystroke arrives before the time elapses, reset the waiting period. Starting the query on a delay keeps your app responsive to keystrokes, and doesn’t waste time executing searches and throwing away the results.

To configure a query with text from a search control, use a [`CSUserQuery`](csuserquery.md) object. User queries are for situations where your app takes input directly from a person. Pass the search text directly to the query object, along with a [`CSUserQueryContext`](csuserquerycontext.md) object with any additional query parameters. The following example configures a context object with the attributes to fetch for search results and configures some additional search parameters. The `searchText` variable contains the string from the search control.

```swift
let queryContext = CSUserQueryContext()
queryContext.fetchAttributes = ["title", "textContent", "authorNames", "contentDescription"]
queryContext.maxSuggestionCount = 10
queryContext.enableRankedResults = true

let query = CSUserQuery(userQueryString: searchText, userQueryContext: queryContext)
```

To execute the query in Swift and get the results, fetch the [`responses`](csuserquery/responses-swift.property.md) property of the query object. This property contains an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) that delivers values to your app as they become available. Fetching this sequence starts the query and begins delivering both results and suggestions asynchronously to your code. For each response, determine whether it is a search result or a suggested text completion and update your interface appropriately. The following example shows a template to use to process responses from the query:

```swift
Task {
    do {
        // Start the query and get the results.
        for try await element in query.responses {
            switch(element) {
                case .item(let item):
                    // Add the item to the list of search results to display.
                    break
                case .suggestion(let suggestion):
                    // Pass suggestions back to the search interface to display.
                    break
                @unknown default:
                    break
            }
        }
    } catch {
        // Handle any errors.
    }
}
```

If you’re not using Swift or prefer to use process results and suggestions separately, configure the appropriate handlers for your query object and call the [`start()`](csuserquery/start().md) method. As Spotlight generates results, it delivers them to the handlers in the [`foundItemsHandler`](cssearchquery/founditemshandler.md) and  [`foundSuggestionsHandler`](csuserquery/foundsuggestionshandler.md) properties of the query object. Use those handlers to process results and suggestions and display them in your interface. You can also add a completion handler to the query to determine when Spotlight finishes delivering results.

When someone interacts with your search control, you typically create multiple query objects to generate results. Query objects run only once, and you don’t reuse them by changing the query string. When the person types more text into your search control, cancel the previous query and create a new one for the new string.

For more information about how to configure query parameters, see [`CSUserQueryContext`](csuserquerycontext.md).

##### Display Completions for Typed Text

Suggestions make it easier for someone to discover relevant search terms from your search interface. The [`CSUserQuery`](csuserquery.md) object you use to fetch results also generates suggestions that you can use to populate your search interface. You can display these suggestions any time someone interacts with your search control. When you execute a query, Spotlight offers a set of ranked suggestions based on the query text and your app’s content.

To display suggested text completions from a SwiftUI, add a [`searchSuggestions(_:)`](https://developer.apple.com/documentation/SwiftUI/View/searchSuggestions(_:)) modifier to your view. The modifier takes a closure, which you use to build views for the suggestions. When collecting responses using the [`responses`](csuserquery/responses-swift.property.md) asynchronous sequence, save the [`CSUserQuery.Suggestion`](csuserquery/suggestion.md) structures you receive and use them to create your views. Each structure contains a [`CSSuggestion`](cssuggestion.md) object with the details of the suggestion. The following example iterates over the list of structures and builds a set of text views from the provided suggestions.

```swift
List {
    // Your view’s content.
}
.searchable(text: $searchText)
.searchSuggestions({
    ForEach($suggestions, id: \.self) { item in
        let title = String(item.suggestion.localizedAttributedSuggestion.characters)
        Text(title)
            .searchCompletion(title)
    }
})
```

> **Note**: If you receive suggestions using the [`foundSuggestionsHandler`](csuserquery/foundsuggestionshandler.md) closure, the system provides the [`CSSuggestion`](cssuggestion.md) objects directly. Extract the data from those objects and use it to build your views.

To display suggestions from a [`UISearchController`](https://developer.apple.com/documentation/UIKit/UISearchController) in your UIKit app, create [`UISearchSuggestionItem`](https://developer.apple.com/documentation/UIKit/UISearchSuggestionItem) objects for each suggestion you receive from your query. When you add those suggestion items to the [`searchSuggestions`](https://developer.apple.com/documentation/UIKit/UISearchController/searchSuggestions) property of the search controller, it automatically displays them from its interface. Each time you execute a new query, clear the old search suggestions from this property and add the new ones.

For more information on adding search suggestions to your SwiftUI views, see [`Suggesting search terms`](https://developer.apple.com/documentation/SwiftUI/Suggesting-search-terms).

## See Also

- [Searching for information in your app](searching-for-information-in-your-app.md)
  Search for app-specific content and refine search results using predicates and filters.
- [class CSUserQuery](csuserquery.md)
  A type you use to initiate searches from your interface and offer suggested text completions.
- [class CSUserQueryContext](csuserquerycontext.md)
  The configuration details to apply to a user query.
- [class CSSearchQuery](cssearchquery.md)
  A type you use to programmatically search the indexed app content.
- [class CSSearchQueryContext](cssearchquerycontext.md)
  The behavior configuration to use for a search query.
- [class CSSuggestion](cssuggestion.md)
  The kind of suggestion to use in a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreSpotlight/building-a-search-interface-for-your-app)*