# Searching for information in your app

**Framework**: Core Spotlight

Search for app-specific content and refine search results using predicates and filters.

#### Overview

Add search capabilities to your app to find relevant information quickly. Instead of building your own custom search tools, index your content using the Core Spotlight APIs and use the framework-provided queries to retrieve information. Indexing your content makes it available to both your app and to the system’s Spotlight search feature.

Use a [`CSSearchQuery`](cssearchquery.md) object to execute a search of your app’s indexed content. With this query object, you specify which attributes of an item to match, and the values that constitute a match. For example, you might tell the query to look for media clips with a duration in a specific range. Although you might incorporate input from your app’s UI when building your query string, use this query type to match specific attributes of your indexed content. For information about how to search based solely on input from a person, see [`Building a search interface for your app`](building-a-search-interface-for-your-app.md).

##### Select the Attributes You Want the Query to Retrieve

When you execute a query, the system doesn’t automatically retrieve every property of your [`CSSearchableItem`](cssearchableitem.md) objects. Instead, it retrieves only the properties you specifically request. This behavior improves performance by not spending time to retrieve information your app doesn’t need.

Identify the properties you want, and specify the property names as strings when you initialize your query. For example, to fetch the title and display name of each item, include “title” and “displayName” strings in the [`fetchAttributes`](cssearchquerycontext/fetchattributes.md) property of your context object.

##### Create a Query String for Your Search

When you execute a query, Core Spotlight evaluates each item in the index against a query string you provide. Construct your query string from one or more predicates, and use each predicate to evaluate an attribute of the indexed item. If the predicates in the overall query string evaluate to true for an item, the query object returns the item in the search results. For each predicate in your query string, use one of the following formats:

- `attributeName operator value[modifiers]`
- `InRange(attributeName, minValue, maxValue)`

In both formats, `attributeName` is a property name from the [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) class. For example, to evaluate the [`title`](cssearchableitemattributeset/title.md) property of the item, use “title” as the attribute name. The `InRange` predicate determines whether a property with a numeric value is between the specified minimum and maxium values. Other predicates compare the attribute to the value you specify using one of the following operators:

| Operator | Definition |
| --- | --- |
| == | Equal. |
| != | Not equal. |
| < | Less than. Works only for numeric and date values. |
| > | Greater than. Works only for numeric and date values. |
| <= | Less than or equal. Works only for numeric and date values. |
| >= | Greater than or equal. Works only for numeric and date values. |

When comparing text values, use modifiers to change the matching behavior the query applies to the comparison. Queries support the following modifiers:

| Modifier | Behavior |
| --- | --- |
| c | Performs a case-insensitive search. |
| d | Performs a search that ignores diacritical marks. |
| w | Matches on word boundaries. This modifier treats transitions from lowercase to uppercase as word boundaries. |
| t | Performs a search on a tokenized value. For example, a search field can contain tokenized values. |
| * | Performs a wildcard search. Match a substring at the beginning, end, or middle. |
| \ | Don’t interpret the character that follows. Use this to include special characters. Examples include `\’` and `\”`. |

Combine two predicates using either an AND or OR operation, listed in the table below. Use parentheses to prioritize the evaluation of predicates.

| Combination operator | Definition |
| --- | --- |
| `&&` | AND operator. If both predicates are true, the entire result is true. If one predicate is false, the result is false. |
| `||` | OR operator. If either predicate is true, the entire result is true. Otherwise, the result is false. |

The following examples show how operators, modifiers, and parentheses work for query strings. When trying to match a specific word, notice that the `w` modifier is more precise than a wildcard because of how it matches word boundaries.

| Query string | Example matches |
| --- | --- |
| `title == “Paris”` | Matches “Paris” but not “paris” or “I love Paris”. |
| `title == “Paris”c` | Matches “Paris” and “paris”, but not “I love Paris”. |
| `title == “Paris”wc` | Matches “Paris”, “paris”, “I love Paris”, and “paris-france.jpg”, but not “Comparison”. |
| `title == “Window”w` | Matches “MyWindowClass” and “Broken Window”, but not “NSWindow”. |
| `authorNames == “Frédéric”` | Matches “Frédéric”, but not “Frederic”. |
| `authorNames == “Frédéric”cd` | Matches “Frédéric” and “Frederic”, regardless of case. |
| `title == “paris*”` | Matches words that begin with “paris” like “paris” and “parisol” but not “comparison”. |
| `title == “*paris”` | Matches words that end with “paris”. |
| `title == “*paris*”` | Matches words that contain “paris” anywhere in the string, including “paris”, “parisol”, and “comparison”. |
| `title == ‘paris’` | Matches a value that is exactly equal to “paris”. |
| `authorNames == “Steve”wc && contentType == “audio”wc’` | Matches audio items that Steve authored. |
| `authorNames == "Steve"wc && (contentType == "audio"wc || contentType == "video"wc)` | Matches any audio or video items that Steve authored. |

##### Match Dates and Times in a Query String

When an attribute contains a date or time value, there are two ways you can specify the value portion of your predicate:

- Specify a floating-point value with the number of seconds relative to January 1, 2001. You can get this value from a doc://com.apple.documentation/documentation/corefoundation/cfdate-rv5 or [`Date`](https://developer.apple.com/documentation/Foundation/Date) type using the [`CFDateGetAbsoluteTime(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFDateGetAbsoluteTime(_:)) function.
- Specify a property of the built-in `$time` variable.

[`CSSearchQuery`](cssearchquery.md) provides the `$time` variable as a convenient way to specify date values in your query strings. When you start a query, the system initializes this variable to the current date and time. Include this variable in the value portion of your predicate to compare a date-based attribute to the date you specify. The following table lists the properties of the variable you can use in your predicates and how the query matches them against attributes.

| `$time` property | Description |
| --- | --- |
| `$time.now` | Matches an attribute set to the current date and time. |
| `$time.today` | Matches an attribute set to the current date. |
| `$time.yesterday` | Matches an attribute set to yesterday’s date. |
| `$time.last_week` | Matches an attribute set to a date from the week before the current week. |
| `$time.this_week` | Matches an attribute set to a date from this week. |
| `$time.this_month` | Matches an attribute set to a date in the current month. |
| `$time.this_year` | Matches an attribute set to a date in the current year. |
| `$time.now(NUMBER)` | Adds `NUMBER` seconds to the current date and time and matches the attribute against that value. You can specify negative or positive numbers. |
| `$time.today(NUMBER)` | Adds `NUMBER` days to the current date and matches the attribute against that value. You can specify negative or positive numbers. |
| `$time.this_week(NUMBER)` | Adds `NUMBER` weeks to the current date and matches the attribute against that value. You can specify negative or positive numbers. |
| `$time.this_month(NUMBER)` | Adds `NUMBER` months to the current date and matches the attribute against that value. You can specify negative or positive numbers. |
| `$time.this_year(NUMBER)` | Adds `NUMBER` years to the current date and matches the attribute against that value. You can specify negative or positive numbers. |
| `$time.iso(ISO-8601-STR)` | Matches the date you specify using an [`ISO-8601-STR`](https://developer.apple.comhttps://www.iso.org/iso-8601-date-and-time-format.html) compliant string. |

The following example shows a query string that includes different types of predicates and modifiers and uses the `$time` variable. The predicate matches an item if author is either Tim or Steve and the item’s completion date occurred within the past 10 days. For the completion date check, adding a negative number to the `$time.today` variable creates a date in the past.

```swift
(authorNames == “Tim”wc || authorNames == “Steve”wc) &&
 InRange(completionDate,$time.today(-10),$time.today)
```

##### Start the Query and Process the Results

Search queries are one-shot objects. While they run, they deliver matching items asynchronously to the handlers you provide. When there are no more items, the query stops. You can also stop a query early by calling its [`cancel()`](cssearchquery/cancel().md) method before the system delivers all matching results.

Create a new query using a query string and a [`CSSearchQueryContext`](cssearchquerycontext.md) object, which contains the query configuration parameters. Start the query by fetching the [`results`](cssearchquery/results-swift.property.md) property of the query object and iterating over the results. The property contains an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence), and fetching it starts the query and begins the delivery of the results. The following function searches for items with a specific title and processes the results in an asynchronous task:

```swift
import CoreSpotlight

class QueryExample {
    func executeQuery(withTitle title : String) {
        var results = [CSSearchableItem]()
        // Fetch the items with a title that starts with the
        // specified string. Perform a case-insensitive comparison.
        let queryString = "title == '\(title)*'c"
    
        let context = CSSearchQueryContext()
        context.fetchAttributes = ["title", "displayName", "keywords", "contentType"]
    
       // Create the query and specify a handler for the results.
        let query = CSSearchQuery(queryString: queryString, queryContext: context)
    
        // Process the results asynchronously.
        Task {
            do {
                // Start the query and iterate over the results.
                for try await result in query.results {
                    let attributeSet = result.item.attributeSet
                    let foundTitle = attributeSet.title
                    let foundDisplayName = attributeSet.displayName
                
                    // Use the results here.
                }
            } catch {
                // Handle any errors.
            }
        }
    }
}
```

If you prefer not to process the results using an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence), specify values for the [`foundItemsHandler`](cssearchquery/founditemshandler.md) and [`completionHandler`](cssearchquery/completionhandler.md) properties. When using handler blocks, you’re responsible for calling the [`start()`](cssearchquery/start().md) method to start the query. To deliver results, the query calls your  [`foundItemsHandler`](cssearchquery/founditemshandler.md) block one or more times, delivering new results with each call. The system executes your completion handler block only once after it finishes delivering all the results.

> ❗ **Important**: Process results using either the [`results`](cssearchquery/results-swift.property.md) property or handler blocks, but not both.

The following code shows a version of the previous method that uses handler blocks to process the results.

```swift
import CoreSpotlight

class QueryExample {
    private var query : CSSearchQuery? = nil
    mutating func executeQueryWithHandlers(withTitle title : String) {
        var results = [CSSearchableItem]()
        // Fetch the items with a title that starts with the
        // specified string. Perform a case-insensitive comparison.
        let queryString = "title == '\(title)*'c"
        
        let context = CSSearchQueryContext()
        context.fetchAttributes = ["title", "displayName", "keywords", "contentType"]
        
        // Create the query and specify a handler for the results.
        self.query = CSSearchQuery(queryString: queryString, queryContext: context)
        self.query?.foundItemsHandler = { (items : [CSSearchableItem]) -> Void in
            results.append(contentsOf: items)
        }
        
        // Display the results when the query finishes.
        self.query?.completionHandler = { (error) -> Void in
            if error == nil {
                for item in results {
                    let attributeSet = item.attributeSet
                    let foundTitle = attributeSet.title
                    let foundDisplayName = attributeSet.displayName
                    
                    // Use the results here.
                }
            } else {
                // Handle the error.
            }
        }
                      
        // Start the query.
        self.query?.start()
    }
}
```

## See Also

- [Building a search interface for your app](building-a-search-interface-for-your-app.md)
  Add a search interface to your app to execute Spotlight queries and offer suggested text completions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searching-for-information-in-your-app)*