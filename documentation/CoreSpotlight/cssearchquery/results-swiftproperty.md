# results

**Framework**: Core Spotlight  
**Kind**: property

The results that match the current query string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var results: CSSearchQuery.Results { get }
```

## Mentions

- [Searching for information in your app](searching-for-information-in-your-app.md)

#### Discussion

Getting the value of this property starts the query automatically and begins the delivery of results. Typically, you get this property as part of a `for..in` loop and iterate over the responses, as shown in the following example:

```swift
var results: [String] = []
let query = CSSearchQuery(queryString: searchText, queryContext: queryContext)

for try await element in query.results {
    if let title = element.item.attributeSet.title {
    results.append(title)
    }
}
```

## See Also

- [CSSearchQuery.Results](cssearchquery/results-swift.struct.md)
  An asynchronous sequence that contains the results that match the query string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/results-swift.property)*